from odoo import fields, models

class AppointmentWizard(models.TransientModel):

    _name = 'appointment.wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    date = fields.Date(string='Date')

    def create_appointment(self):
        vals={
            'patient_id':self.patient_id.id,
            'appointment_date':self.date,
        }
        self.patient_id.message_post(body='appointment created successfully',subject='Appointment Creation')
        self.env['hospital.appointment'].create(vals)
        print('record Created Successfully!')