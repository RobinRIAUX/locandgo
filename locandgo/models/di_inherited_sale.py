
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
   
    di_nbvelos = fields.Integer(string='Nb vélo', help="Nombre de vélos")
    di_nbmois = fields.Integer(string='Nb mois', help="Nombre de mois")    
    
    @api.multi
    @api.onchange('di_nbvelos', 'di_nbmois')
    def _di_onchange_qte(self):
        for sol in self:
            sol.product_uom_qty=sol.di_nbvelos*sol.di_nbmois