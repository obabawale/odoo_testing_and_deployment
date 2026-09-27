from functools import wraps
from odoo import models


def attrsetter(attr, value):
    """ Return a function that sets ``attr`` on its argument and returns it. """
    return lambda method: setattr(method, attr, value) or method


def constrains(*args):
    if args and callable(args[0]):
        args = args[0]
    return attrsetter('_constrains', args)


def log_func(func):
    print("&&&&&&&&&&&&&&&&&&& Hallo!!")
    getattr('create_new_log')()
    return func

# def log_func(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """A wrapper function"""
#         print("this is where the magic happens!!!")
#         return func
#     return wrapper


class Blog(models.Model):
    _inherit = 'blogger_app.blog'

    def create_new_log(self):
        print("I am creating a new log")

    # @constrains("abc")
    def action_submit(self, *args,**kw):
        print("&&&&&&&& 1 &&&&&&&&&&& ", args)
        print("&&&&&&&&& 2&&&&&&&&&& ", kw)
        print("&&&&&&&&& 2&&&&&&&&&& ", dir(self))
        print("This is taking place inside the sibmit function")
