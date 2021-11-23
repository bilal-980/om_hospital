from odoo import models, fields

class HospitalLab(models.Model):
    _name = 'hospital.lab'

    name = fields.Char(string='Name')
    user_id = fields.Many2one('res.users', string='User')    