# -*- coding: utf-8 -*-

from datetime import date
from odoo import models, fields
from odoo.exceptions import UserError


class blogger_app(models.Model):
    _name = 'blogger_app.blog'
    _description = 'Blog'

    name = fields.Char(string="Blog Title")
    description = fields.Text(string="Blog Content")
    author_id = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.uid)
    reviewer_id = fields.Many2one('res.users', string='Reviewed By')
    date_approved = fields.Date('Approved On')
    date_published = fields.Date('Date Published')
    state = fields.Selection([
        ('draft', 'New'),
        ('submit', 'Submitted'),
        ('review', 'Reviewed'),
        ('publish', 'Published'),
        ('cancel', 'Cancelled'),
        ('reject', 'Rejected'),
    ], string='State', default="draft", readonly=True, help="""
    When in 'draft', record has just been created
    When in 'submit', record has just been submitted for review
    When in 'review', record has just been reviewed and approved
    When in 'publish', record has just been published by the creator
    When in 'cancel', record has just been cancelled by author
    When in 'reject', record has just been rejected by author
    """)

    def action_submit(self):
        if not self.env.user == self.author_id:
            raise UserError("Blog can only be submitted by the author!")
        self.state = 'submit'
    
    def action_approve(self):
        if not self.env.user.has_group('blogger_app.group_blog_manager'):
            raise UserError("Only Blog Manager is allowed to do this!")
        self.reviewer_id = self.env.uid
        self.date_approved = date.today()
        self.state = 'review'
    
    def action_publish(self):
        self.date_published = date.today()
        self.state = 'publish'
    
    def action_cancel(self):
        self.state = 'cancel'
    
    def action_reject(self):
        self.state = 'reject'

    def unlink(self):
        for blog in self:
            if not blog.state == 'draft':
                raise UserError("Cannot delete blog not in draft state!")
