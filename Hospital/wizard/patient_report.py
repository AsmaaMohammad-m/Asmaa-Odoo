from odoo import api, fields, models,_



class PatientRepWizard(models.TransientModel):
    _name = "patient.rep.wizard"
    _description = "Print patient Wizard REP"
    gender = fields.Selection( [('male', 'Male'),('female', 'Female'),('other', 'Other')], string="Gender")



    age = fields.Integer(string="Age")


    def action_print_report(self):
        print('k')