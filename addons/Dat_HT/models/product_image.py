from odoo import models, fields

class ProductImage(models.Model):
    _name = 'product.image'
    _description = 'Product Image'

    name = fields.Char(string='Image Name')  # Optional field for image name
    image = fields.Binary(string='Image')  # Field for storing the image
    product_tmpl_id = fields.Many2one(
        'product.template',  # Linking back to product.template
        string='Product Template',
        ondelete='cascade'  # Deletes images when the related product template is deleted
    )
