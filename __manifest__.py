{
    'name': 'Histórico de almacenes',
    'version': '13.0.06.10.23',
    'category': 'Sales',
    'summary': 'Módulo de inventario con histórico de ventas',
    'author': 'Daniel Garia Nieto',
    'depends': ['base'],
    'data': [
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/product_product.xml',
        'views/stock_history.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
