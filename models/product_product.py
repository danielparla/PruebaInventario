from odoo import models, fields, api

class ProductProduct(models.Model):
    _name = 'new_product_product.product_product'
    _description = 'Product Product'

    id = fields.Integer(string='ID', readonly=True)
    default_code = fields.Char(string='Default Code')

    daily_sales_average = fields.Float(string='Daily Sales Average', compute='_compute_daily_sales_average', store=True)

    @api.depends('order_line_ids', 'stock_history_ids')
    def _compute_daily_sales_average(self):
        for product in self:
            order_lines = product.order_line_ids.filtered(lambda ol: ol.state == 'done').sorted(
                key=lambda ol: ol.order_id.date_order, reverse=True)
            stock_history_with_stock = product.stock_history_ids.filtered(lambda sh: sh.quantity > 0).sorted(
                key=lambda sh: sh.date, reverse=True)

            last_60_order_lines = order_lines[:60]
            last_60_stock_history = stock_history_with_stock[:60]

            total_sales = sum(last_60_order_lines.mapped('product_uom_qty'))
            days_with_stock = len(last_60_stock_history)

            if days_with_stock > 0:
                product.daily_sales_average = total_sales / days_with_stock
            else:
                product.daily_sales_average = 0.0
