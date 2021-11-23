from odoo import models, fields, api
from odoo.exceptions import UserError

class Unisntall_module(models.Model):
    _inherit = 'ir.module.module'
    
    def uninstall_(self):

        try:
            print('if any option is to be performed before uninstalling...')

            return super(Unisntall_module,self)._button_immediate_function(type(self).button_uninstall)
        except:
            raise UserError(' Warning something wrong !')
