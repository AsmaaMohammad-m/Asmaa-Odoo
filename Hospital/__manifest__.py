# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital management',
    'version' : '1.0',
    'summary': 'hospital management software',
    'sequence': -100,
    'description': """
hospital management software
    """,
    'category': 'Productivity',
    'author': 'Asmaa Sobhy',
    'website': 'https://www.odoomates.tech',
    'depends' : ['sale',
                 'mail',
                 'website_slides',
                 'hr',
                 'report_xlsx'],
    'data': [
    'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'wizard/all_patient_report_view.xml',
        'wizard/appointment_report_view.xml',

        'views/patient.xml',
        'views/doctor_view.xml',
        'views/view_kids.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'views/sale.xml',
        'views/partner.xml',
        'report/report.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/appointment_details.xml',
        'report/all_patient_lis.xml',






    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
