from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestBlog(TransactionCase):

    def setUp(self):
        super(TestBlog, self).setUp()

        # Create blog user1.
        blog_user = self.env['res.users'].create({
            'name': 'Blog User',
            'email': 'bloguser@example.com',
            'login': 'bloguser',
            'password': 'bloguser',
            'groups_id': [(6, 0, self.env.user.groups_id.ids), (4, self.env.ref('blogger_app.group_blog_user').id)],
        })
        blog_user.partner_id.email = 'bloguser@example.com'
        self.blog_user = blog_user

        # Create blog user2.
        self.blog_user2 = self.env['res.users'].with_context(notification=False).create({
            'name': 'Blog User2',
            'login': 'bloguser2@example.com',
            'password': 'bloguser2',
            'groups_id': [(6, 0, self.env.user.groups_id.ids), (4, self.env.ref('blogger_app.group_blog_user').id)],
        })
        self.blog_user2.partner_id.email = 'bloguser2@example.com'

        # Create blog manager
        self.blog_manager = self.env['res.users'].create({
            'name': 'Blog Manager',
            'login': 'blogmanager@example.com',
            'password': 'blogmanager',
            'groups_id': [(6, 0, self.env.user.groups_id.ids), (4, self.env.ref('blogger_app.group_blog_manager').id)],
        })

        self.cr = self.env.cr

        # Create blog
        self.env = self.env(user=blog_user)
        self.blog1 = self.env['blogger_app.blog'].create({
            'name': 'Blog One',
            'description': "Blog1 Contents",
        })

        self.env = self.env(user=self.blog_user2)
        self.blog2 = self.env['blogger_app.blog'].create({
            'name': 'Blog Two',
            'description': "Blog2 Contents",
        })

    def test_blog_is_created_with_right_title_and_description(self):
        self.assertTrue(self.blog1.name)
        self.assertEqual(self.blog1.name, "Blog One")
        self.assertEqual(self.blog1.description, "Blog1 Contents")

    def test_author_is_set(self):
        self.assertTrue(self.blog1.author_id)
        self.assertTrue(self.blog2.author_id)

    def test_right_author_is_set(self):
        self.assertEqual(self.blog2.author_id, self.blog_user2)
        self.assertEqual(self.blog1.author_id, self.blog_user)

    def test_asset_raises_user_error(self):
        self.env = self.env(user=self.blog_user)
        # submit blog2 by blog user1
        with self.assertRaises(UserError), self.cr.savepoint():
            self.blog2.with_env(self.env).action_submit()
            self.blog.with_env(user=self.blog_user2).action_submit()

    def test_error_raised_if_approver_is_not_admin(self):
        with self.assertRaises(UserError), self.cr.savepoint():
            self.blog1.with_context(user=self.blog_user).action_approve()
            self.blog1.with_context(user=self.blog_user2).action_approve()
            self.blog2.with_context(user=self.blog_user).action_approve()
            self.blog2.with_context(user=self.blog_user2).action_approve()

    def test_assertion_error_not_raised_if_admin(self):
        self.env = self.env(user=self.blog_manager)
        self.blog1.with_env(self.env).action_approve()
        self.assertEqual(self.blog1.state, 'review')

    def test_error_raised_when_blog_is_deleted_in_non_draft(self):
        self.assertEqual(self.blog1.state, 'draft')
        # change the state to submit
        self.blog1.action_submit()
        # confirm that the state of the blog is now in submit
        self.assertEqual(self.blog1.state, 'submit')
        with self.assertRaises(UserError), self.cr.savepoint():
            self.blog1.unlink()

    def test_blog_cancel(self):
        self.assertEqual(self.blog1.state, 'draft')
        self.blog1.action_cancel()
        self.assertEqual(self.blog1.state, 'cancel')
