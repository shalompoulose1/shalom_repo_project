from odoo import api, fields, models

class ContactEditWizard(models.TransientModel):
    _name = 'contact.edit.wizard'
    _description = 'Quick Edit Contact Wizard'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    state_id = fields.Many2one('res.country.state', string="State")  # Fixed model
    country_id = fields.Many2one('res.country', string="Country")

    @api.model
    def default_get(self, fields):
        res = super(ContactEditWizard,self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if active_id:
            partner = self.env['res.partner'].browse(active_id)
            res.update({
                'name': partner.name,
                'email': partner.email,
                'phone': partner.phone,
                'mobile': partner.mobile,
                'street': partner.street,
                'street2': partner.street2,
                'city': partner.city,
                'state_id': partner.state_id.id,
                'country_id': partner.country_id.id,
            })
        return res

    def update_partner_data(self):
        active_id = self.env.context.get('active_id')
        if active_id:
            partner = self.env['res.partner'].browse(active_id)
            partner.write({
                'name': self.name,
                'email': self.email,
                'phone': self.phone,
                'mobile': self.mobile,
                'street': self.street,
                'street2': self.street2,
                'city': self.city,
                'state_id': self.state_id.id,
                'country_id': self.country_id.id,
            })
