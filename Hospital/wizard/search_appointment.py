# -*- coding: utf-8 -*-
from odoo import api, fields, models,_



class SearchAppointmentWizard(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = " Search Appointment Wizard"



    patient_id=fields.Many2one('hospital.patient',string="Patient",required=True)
    def action_search_appointment_m1(self):
        # method 1
        action = self.env.ref('Hospital.action_hospital_appointment').read()[0]  # this action returns all appointments

        action['domain'] = [('patient_id', '=', self.patient_id.id)]  # we override the domain of action
        # method 2
        return  action

    def action_search_appointment_m2(self):
        action = self.env["ir.actions.actions"]._for_xml_id("Hospital.action_hospital_appointment")
        action['domain']=[('patient_id','=' ,self.patient_id.id )]#we override the domain of action
        return  action

    def action_search_appointment_m3(self):

       return {
           'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain':[('patient_id','=' ,self.patient_id.id )],
   '        view_mode': 'tree,form',
            'target': 'current',

      }
        #return  action



