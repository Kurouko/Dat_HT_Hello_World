from odoo import models, fields

class ProductDocument(models.Model):
    _name = 'product.document'
    _description = 'Product Document'

    name = fields.Char('Document Name')
    datas = fields.Binary('Document File')
    product_tmpl_id = fields.Many2one(
        'product.template',  # Connects to product.template
        string='Product Template',
        required=True,
        ondelete='cascade'  # Ensures documents are deleted if the product template is deleted
    )
