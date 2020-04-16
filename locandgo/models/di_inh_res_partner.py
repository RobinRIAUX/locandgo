
# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    di_horairehs = fields.Char(string='Horaires hors saison', help="Horaires hors saison")
    di_horaireps = fields.Char(string='Horaires pleine saison', help="Horaires pleine saison")
    di_codeacces = fields.Char(string='Code accès', help="Code d'accès pour entrer sur le camping")
    di_cptloceo = fields.Char(string='Code compta Loceo', help="Code compta Loceo")         
    di_dateouv = fields.Date(string="Date d'ouverture", help="Date d'ouverture")
    di_dateferm = fields.Date(string="Date de fermeture", help="Date de fermeture")  
    di_idbase = fields.Char(string='Identifiant Loceo', help="Identifiant Loceo")     
    di_ordre = fields.Integer("Ordre",help="""Permet de gérer un ordre d’affichage (catégorisation géographique des clients)""")
    
    di_pseudo = fields.Char(string='Pseudo', help="Pseudo")     
    di_pwd = fields.Char(string='Mot de passe', help="Mot de passe")
    di_tarif = fields.Char(string='Tarif', help="Tarif")          
    
    di_bloqsite = fields.Boolean(string="Bloquer l'accès au site", help="Bloquer l'accès au site", default=False)
    di_avecsortie = fields.Boolean(string="Avec sortie", help="Avec sortie", default=False)
    
   