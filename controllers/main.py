from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    
    """ 
        Routes:
          /patient_webform: url description
    """
    
    @http.route('/patient_webform', type='http', auth='public',website=True)
    def patient_webform(self, **kw):

        patients=request.env['hospital.patient'].search([])

    
        return request.render('om_hospital.create_patient',{'patients':patients})
    