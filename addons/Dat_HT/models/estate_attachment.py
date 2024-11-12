from odoo import models, fields, api
class EstateAttachment(models.Model):
    _name = 'estate.attachment'
    _description = 'Estate Attachment'
    _order = 'id desc'

    name = fields.Char(string='Tên tệp')
    file_data = fields.Binary(string='Dữ liệu tệp')
    estate_id = fields.Many2one('estate.odoo', string='Estate', ondelete='cascade')
