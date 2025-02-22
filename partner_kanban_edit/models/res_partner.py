from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    
    def quick_edit_partner(self):
        return {
                'name': 'Contact Edit Wizard',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'contact.edit.wizard',
                'target': 'new',
                'view_id': self.env.ref('partner_kanban_edit.view_contact_edit_wizard').id,
                'context': {
                    'active_model': 'res.partner',
                    'active_ids': self.ids,
                },
                }
        
        
    def archive_partner(self):
        self.action_archive()
        
    def Unarchive_partner(self):
        self.action_unarchive()
        