# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import models, fields, api, _
from collections import namedtuple
from odoo.exceptions import UserError

class EstateOdoo(models.Model):
    _name = 'estate.odoo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Bất động sản'
    _Attachment = namedtuple('Attachment', ('fname', 'content', 'info'))
    name = fields.Char(string='Tên bất động sản')
    address = fields.Char(string='Địa chỉ')
    status = fields.Selection(
        [('available', 'Có Sẵn'), ('sold', 'Đã bán'), ('rended', 'Đã cho thuê')],
        string='Trạng thái', default='available', help="Trạng thái của bất động sản"
    )
    description = fields.Text(string='Giới thiệu')
    estate_attachment_count = fields.Integer('Attachment Count', compute='_compute_estate_attachment_count', groups="base.group_user")
    location_id = fields.Many2one(
        comodel_name='location.odoo', 
        string='Vị trí', 
        help="Vị trí của bất động sản",
        ondelete='cascade'
    )
    parent_id = fields.Many2one(
        comodel_name='location.odoo', 
        string='Vị trí', 
        help="Vị trí của bất động sản"
    )
    # Many2many for Estate Attachments
    # estate_attachment_ids = fields.Many2many(
    #     'ir.attachment', 
    #     'estate_odoo_attachment_rel', 
    #     'estate_id', 
    #     'attachment_id', 
    #     string='Estate Attachments', 
    #     domain=[('res_model', '=', 'estate.odoo')]
    # )
     
    Estate_Attachment_ids = fields.One2many('ir.attachment', 'res_id', string='Estate Attachments', domain=[('res_model', '=', 'estate.odoo')])
    
    def _compute_estate_attachment_count(self):
        read_group_var = self.env['ir.attachment']._read_group(
            [('res_id', 'in', self.ids), ('res_model', '=', self._name)],
            groupby=['res_id'],
            aggregates=['__count']
        )

        attachment_count_dict = dict(read_group_var)
        for record in self:
            record.estate_attachment_count = attachment_count_dict.get(record.id, 0)