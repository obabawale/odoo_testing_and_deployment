# -*- coding: utf-8 -*-
{
    'name': "Testing Application",

    'summary': """
        Demonstrate testing...""",

    'description': """
        Demonstrate testing...
    """,

    'author': "Olalekan Babawale",
    'website': "http://obabawale.github.io",

    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['mail'],

    'data': [
        'security/blogger_app_security.xml',
        'security/ir.model.access.csv',
        'views/blog_views.xml',
    ]
}
