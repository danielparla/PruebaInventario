from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _name = 'new_sale_order_line.sale_order_line'
    _description = 'Sale Order Line'

    id = fields.Char(string='ID', readonly=True)
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    product_uom_qty = fields.Float(string='Quantity', digits=(12, 1))
    discount = fields.Float(string='Discount (%)', digits=(12, 2))
    price_unit = fields.Float(string='Unit Price (€)', digits=(12, 2))
    price_subtotal = fields.Float(string='Subtotal (€)', digits=(12, 2), compute='_compute_subtotal', store=True)
    order_id = fields.Many2one('new_sale_order.sale_order', string='Sale Order')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')

    # Calcula el subtotal en euros
    @api.depends('product_uom_qty', 'discount', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.price_subtotal = line.price_unit * line.product_uom_qty * (1 - line.discount / 100)
