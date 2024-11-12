from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    Product_Attachment_ids = fields.One2many('ir.attachment', 'res_id', string='Product Attachments', domain=[('res_model', '=', 'product.template')])
    product_attachment_count = fields.Integer('Attachment Count', compute='_compute_product_attachment_count', groups="base.group_user")

    def _compute_product_attachment_count(self):
        read_group_var = self.env['ir.attachment']._read_group(
            [('res_id', 'in', self.ids), ('res_model', '=', self._name)],
            groupby=['res_id'],
            aggregates=['__count']
        )

        attachment_count_dict = dict(read_group_var)
        for record in self:
            record.product_attachment_count = attachment_count_dict.get(record.id, 0)
