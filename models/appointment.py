from odoo import models, fields, api
from odoo.tools.translate import _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Appointment model of patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    def _desc_default(self):
        return 'this is default description of Hospital Appointment!'

    name = fields.Char(
        string="Appointment ID",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    patient_age = fields.Integer(string='Patient Age',related='patient_id.age')
    notes = fields.Text(string='Description',default=_desc_default)
    appointment_date = fields.Date(string='Date')
    doctor_precription = fields.Text(string='Doctor Pharmacy')
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment')
    pharmacy = fields.Text(string='Pharmacy')

    @api.model
    def create(self, vals_list):
        if vals_list.get('name',_('New'))==_('New'):
            vals_list['name']=self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')

        return super(HospitalAppointment,self).create(vals_list)    




class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Hospital APpointment Lines'

    product_id = fields.Many2one('product.product', string='Product')
    product_qty=fields.Integer(string="Quantity")
    appointment_id=fields.Many2one('hospital.appointment',string='Appointment ID')
