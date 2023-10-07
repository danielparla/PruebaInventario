from odoo import models, fields

class ResPartner(models.Model):
    _name = 'new_res_partner.res_partner'
    _description = 'New Res Partner'

    id = fields.Integer(string='ID', readonly=True)
    name = fields.Char(string='Name')

    # Relación inversa con el modelo sale_order
    sale_order_ids = fields.One2many('new_sale_order.sale_order', 'partner_id', string='Sale Orders')
