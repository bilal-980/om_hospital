from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'

    name = fields.Char(string='Doctor Name',required=True, )
    related_user=fields.Many2one('res.users',string='Related Users')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
         string='Gender')