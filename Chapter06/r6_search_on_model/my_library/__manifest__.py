# -*- coding: utf-8 -*-
{
    'name': "Chapter6_06",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """Long description""",  # You can also rst format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '12.0.1',
    'depends': ['base'],
    # This data files will be loaded at the installation (commented becaues file is not added in this example)
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_loan.xml',
        'views/library_book.xml',
        'views/library_member.xml',
        'views/library_book_categ.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
