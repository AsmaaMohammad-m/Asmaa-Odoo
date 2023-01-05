# -*- coding: utf-8 -*-
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError




class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appontment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order="doctor_id,name,age"

    name = fields.Char(string='Order Reference',required=True,copy=False,readonly=True,default=lambda self:_('New'))
    patient_id=fields.Many2one('hospital.patient',string="Patient",required=True)
    patient_name_id=fields.Many2one('hospital.patient',string="Patient Name",required=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status",
                             tracking=True)
    date_appointment=fields.Date(string="Date")
    date_checkup=fields.Datetime(string="Check Up Time")
    age = fields.Integer(string='Age',related='patient_id.age', tracking=True,store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    doctor_id = fields.Many2one('hospital.doctor',string='Doctor', required=True)
    prescription=fields.Text(string="Prescription")
    prescription_line_ids=fields.One2many('appointment.prescription.lines','appointment_id',string="Prescription Lines")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
        # if vals.get('reference', _('New')) == _('New'):

        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender=self.patient_id.gender
            if self.patient_id.note:

                self.note=self.patient_id.note
        else:
            self.gender=''
            self.note=''

    def unlink(self):
        if self.state=='done':
            raise ValidationError(_('You can not delete %s as it is in done state'%self.name))
        return super(HospitalAppointment, self).unlink()
    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://apps.odoo.com/apps/modules/14.0/om_hospital',
        }

class AppointmenPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = " Appointmen Prescription Lines"
    name=fields.Char(string="Medicine",required=True)
    qty=fields.Integer(string="Quantity")
    appointment_id=fields.Many2one('hospital.appointment',string="Appointment")


