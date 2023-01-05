from odoo import api, fields, models,_



class AllPatientReport(models.AbstractModel):
    _name = "report.hospital.report_all_patient_lis"
    _description = "Print Report"
    @api.model
    def get_report_values(self,docids,data=None):
        docs=self.env['hospital.patient'].search([])
        return {
            'docs':docs,
        }