# -*- coding: utf-8 -*-
 
from odoo import api, fields, models

    
class DiParam(models.Model):
    _name = "di.param"
    _description = "Parametres"
    _order = "name"
        
    di_company_id = fields.Many2one('res.company', string='Société', readonly=True,  default=lambda self: self.env.user.company_id)
    name = fields.Char(string='Name',readonly=True,default=lambda self: self.env.user.company_id.name)
#     di_act_grille_vente = fields.Boolean(string="Activer la grille de vente",help="""Permet l'activation de la grille de vente pour 
#     une saisie plus rapide sur cadencier.""", default=False)
  
    di_compta_prg   = fields.Selection([("INTERNE", "Interne"), ("DIVALTO", "Divalto"),("EBP", "EBP"),("SAGE","Sage")], string="Logiciel de comptabilité",
                                           help="Permet de savoir vers quel logiciel de comptabilité on va exporter (ou non) les écritures.",default="INTERNE")
    di_dos_compt = fields.Char(string='Dossier comptable',default="",help="""Dossier d'intégration pour le logiciel de comptabilité.""")
    di_etb_compt = fields.Char(string='Etablissement comptable',default="",help="""Etablissement d'intégration pour le logiciel de comptabilité.""")        
    di_nom_exp_ecr_compta = fields.Char(string='Nom fichier export écritures',default="ecritures.csv",help="""Nom par défaut du fichier d'export des écritures comptables.""")
   
    #unicité 
    @api.multi
    @api.constrains('di_company_id')
    def _check_di_company_id(self):
        for param in self:
            if param.di_company_id:
                di_company_id = param.search([
                    ('id', '!=', param.id),
                    ('di_company_id', '=', param.di_company_id.id)], limit=1)
                if di_company_id:
                    raise Warning("Le paramétrage pour ce dossier existe déjà.")