# -*- coding: utf-8 -*-

{
    'name': 'POS product redesign',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Different design for products',
    'description': """Different design for products""",
    'depends': ['point_of_sale'],
    'author': 'Koen Habets',
    'company': 'Koen Habets',
    'maintainer': 'Koen Habets',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {
        'point_of_sale.assets': [
            "POS-product-redesign/static/src/css/style.css",
            "POS-product-redesign/static/src/xml/product.xml",
        ],
    },
}
