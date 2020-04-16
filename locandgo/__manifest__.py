# -*- coding: utf-8 -*-
{
    'name': "Loc_And_Go",

    'summary': """
        Spécifiques Loc and Go""",

    'description': """
        Surcharges pour Loc and Go
    """,

    'author': "Difference informatique",
    'website': "http://www.pole-erp-pgi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'locandgo',
    'version': '0.1',

    # any module necessary for this one to work correctly
      'depends': [
        'base',
        'product',
        'sale',
        'sale_management',                                            
        'sale_margin',
        'account',
        'account_accountant',                           
        'l10n_fr_sale_closing',                                
        'base_optional_quick_create',
        'eradicate_quick_create',
        ],


    # always loaded
    'data': [
        "wizard/di_transfertcompta_wiz.xml",         
        "views/di_inh_res_partner_view.xml",
        "views/di_inherited_account_view.xml",
        "views/di_tables_view.xml",
        "views/di_inherited_sale_view.xml",
        "report/di_inh_report_templates.xml",
        "report/di_sale_report_templates.xml", 
        "report/di_report_invoice.xml",                  
        "security/ir.model.access.csv",          
        "locandgo_menu.xml",
              
    ],
    # only loaded in demonstration mode
    'demo': [
       
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}