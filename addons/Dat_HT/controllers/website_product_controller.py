from odoo import http
from odoo.http import request

class WebsiteProductController(http.Controller):
    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, **kwargs):
        # Fetch images linked to the product
        image_urls = []
        for attachment in product.product_image_ids:
            image_url = "/web/image/ir.attachment/%s/datas" % attachment.id
            image_urls.append(image_url)

        # Pass the image URLs to the template
        return request.render('your_module.product_template', {
            'product': product,
            'image_urls': image_urls,
        })
