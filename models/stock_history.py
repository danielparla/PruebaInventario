from odoo import models, fields

class StockHistory(models.Model):
    _name = 'new_stock_history.stock_history'
    _description = 'Stock History'

    id = fields.Integer(string='ID', readonly=True)
    product_id = fields.Many2one('new_product_product.product_product', string='Product')
    quantity = fields.Integer(string='Quantity')
    date = fields.Datetime(string='Date')
