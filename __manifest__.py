{
  'name': 'Hospital Management',
  'author': 'Silverdale',
  'version': '0.1',
  'depends': ['base' ,'mail' ,'sale','website'],
  'data': [
    'security/ir.model.access.csv',
    'security/security.xml',
    'data/ir_sequence.xml',
    'data/mail_template.xml',
    'data/patient_data.xml',
    'data/cron.xml',
    'wizard/appointment_wizard_xml.xml',
    'views/patient.xml',
    'views/lab.xml',
    'views/appointment.xml',
    'views/website_form.xml',
    'views/doctor.xml',
    'views/sale.xml',
    'reports/patient_card.xml',
    
  ],
  'images':['static/description/icon.png'],

  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 1,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': '- Arkademy Part 1',
  'summary': 'simple hospital management built in odoo',
  'license': 'OPL-1',
  'website': 'https://www.silverdaletech.com/',
  'description': '-'
}