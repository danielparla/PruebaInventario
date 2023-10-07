from odoo import models, fields

class SaleOrder(models.Model):
    _name = 'new_sale_order.sale_order'
    _description = 'New Sale Order'

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name')
    partner_id = fields.Many2one('new_res_partner.res_partner', string='Customer')
    date = fields.Datetime(string='Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='State', default='draft')
