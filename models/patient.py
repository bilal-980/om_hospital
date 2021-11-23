from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    patient = fields.Many2one("hospital.patient", string="Patient")


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient record table"
    _order = 'name desc'

    name = fields.Char(string="Name", required=True,track_visibility="onchange")
    age = fields.Integer(string="Age", default=0)
    age_group = fields.Selection(
        [("minor", "Minor"), ("major", "Major")],
        string="Age Group",
        compute="_age_group",
        store=True,
        inverse='_inverse_age_gorup'
    )

    description = fields.Text(string="Description")
    patient_email = fields.Char(string='Email')
    user_email_id = fields.Many2one('res.users', string='Pro')
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Doctor Gender')
    image = fields.Binary(string="Image")
    ser_seq = fields.Char(
        string="Reference Order",
        readonly=True,
        copy=False,
        default=lambda self: _("New"),
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], string='Status', default='draft')
    appointment_count = fields.Integer(
        string='Total Appointment', compute='_total_appointment')
    active = fields.Boolean(string='Active', default=True)

    def self_patient_appointement(self):
        '''
        button action for creating form of active patients
        '''
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'domain': [('patient_id', '=', self.id)],
        }

    @api.model
    def create(self, vals_list):
        if vals_list.get("ser_seq", _("New")) == _("New"):
            vals_list["ser_seq"] = self.env["ir.sequence"].next_by_code("hospital.patient.sequence") or _("New")
        result = super(HospitalPatient, self).create(vals_list)
        return result

    def _total_appointment(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    def confirm_action(self):
        for rec in self:
            rec.state = 'confirm'

    def done_action(self):
        for rec in self:
            rec.state = 'done'

    def cancel_action(self):
        for rec in self:
            rec.state = 'cancel'

    def send_email(self):
        '''
        send mail to patients
        '''
        temp = self.env.ref('om_hospital.mail_template_patient_card').id
        self.env['mail.template'].browse(temp).send_mail(self.id, force_send=True)
    
    def name_get(self):
        result = []
        for field in self:
            result.append((field.id, f'{field.name} {field.gender}'))
        return result

    def cron_call(self):
        '''
        Method for learning purpose of sequence functionality 
        '''
        print('hello world!')

    @api.depends("age")
    def _age_group(self):
        '''
        compute method of age_group field 
        '''
        for rec in self:
            if rec.age:
                if rec.age > 18:
                    rec.age_group = "major"
                else:
                    rec.age_group = "minor"

    def _inverse_age_gorup(self):
        for rec in self:
            rec = rec

    @api.constrains("age")
    def _check_age(self):
        '''
        constraints method for age validation
        '''
        for rec in self:
            try:
                if rec.age < 5 or None:
                    raise ValidationError("Age must be greater than five ")
            except:
                raise UserError('Unexpected Error ..')
