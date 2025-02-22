{
    'name': 'Contact Quick Edit from Kanban',
    'version': '17.0.0.1',
    'summary': 'Allows quick editing of contacts directly from the Kanban view.',
    'category': 'Contacts',
    'author': 'Shalom Poulose',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/contact_edit_wiz_views.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
