
# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccounInvoice(models.Model):
    _inherit = "account.invoice"
    
    @api.model
    def _di_get_payments_terms_vals(self):
        aml = self.env['account.move.line'].search(['&', ('debit', '!=', 0.0), ('invoice_id', '=', self.id),('partner_id','=',self.partner_id.id)]).sorted(key=lambda t: t.date_maturity)      
        if not aml:
            return []
        payment_terms_vals = []
        currency_id = self.currency_id
        for payment in aml:            
            payment_terms_vals.append({
                'date_ech': payment.date_maturity,
                'montant_ech': payment.debit,                
            })
        return payment_terms_vals
     
class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"
    
     
    di_nbvelos = fields.Integer(string='Nb vélo', help="Nombre de vélos")
    di_nbmois = fields.Integer(string='Nb mois', help="Nombre de mois")
    
    @api.multi
    @api.onchange('di_nbvelos', 'di_nbmois')
    def _di_onchange_qte(self):
        for ail in self:
            ail.quantity=ail.di_nbvelos*ail.di_nbmois
    
    @api.model
    def create(self, vals):               
        di_avec_sale_line_ids = False  # initialisation d'une variable       
        di_ctx = dict(self._context or {})  # chargement du contexte
        for key in vals.items():  # vals est un dictionnaire qui contient les champs modifiés, on va lire les différents enregistrements                      
            if key[0] == "sale_line_ids":  # si on a modifié sale_line_id
                di_avec_sale_line_ids = True
        if di_avec_sale_line_ids == True:
            qte_a_fac = 0.0
            poib = 0.0
            for id_ligne in vals["sale_line_ids"][0][2]:
                Disaleorderline = self.env['sale.order.line'].search([('id', '=', id_ligne)], limit=1)                                 
                if Disaleorderline.id != False:               
                    #on attribue par défaut les valeurs de la ligne de commande   
                    vals["di_nbvelos"] = Disaleorderline.di_nbvelos  
                    vals["di_nbmois"] = Disaleorderline.di_nbmois                    
                      
        res = super(AccountInvoiceLine, self).create(vals)                           
        return res    