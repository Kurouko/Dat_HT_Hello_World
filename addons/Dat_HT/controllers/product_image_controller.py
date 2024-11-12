import logging
import json
from odoo.http import request
from odoo import http
from ..models.format_response import FormatResponse

_logger = logging.getLogger(__name__)

class ProductImageController(http.Controller):

    @http.route('/api/product_images', type='http', auth='public', methods=['GET'], csrf=False)
    def get_all_product_images(self, **kwargs):
        try:
            # Tìm tất cả hình ảnh sản phẩm
            product_images = request.env['product.image'].sudo().search([])

            _logger.info(f"Number of product images found: {len(product_images)}")

            # Tạo danh sách để lưu kết quả
            image_data = []
            for image in product_images:
                image_data.append({
                    'id': image.id,
                    'name': image.name,
                    'image': image.image,
                    'product_tmpl_id': image.product_tmpl_id.id,
                })

            return FormatResponse(200, "Product images retrieved successfully", image_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
        
    
    @http.route('/api/product_images/<int:image_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_product_image_by_id(self, image_id, **kwargs):
        try:
            # Tìm hình ảnh theo ID
            existing_image = request.env['product.image'].sudo().search([('id', '=', image_id)], limit=1)

            if not existing_image:
                return FormatResponse(404, 'Product image not found').to_response()

            # Chuyển dữ liệu hình ảnh thành dictionary
            image_data = {
                'id': existing_image.id,
                'name': existing_image.name,
                'image': existing_image.image,
                'product_tmpl_id': existing_image.product_tmpl_id.id,
            }

            return FormatResponse(200, 'Product image retrieved successfully', image_data).to_response()

        except Exception as e:
            _logger.error(f"Error in API GET: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
        
        
    @http.route('/api/product_images', type='http', auth='public', methods=['POST'], csrf=False)
    def create_product_image(self, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            
            # Tạo hình ảnh sản phẩm mới
            new_image = request.env['product.image'].sudo().create({
                'name': data.get('name'),
                'image': data.get('image'),
                'product_tmpl_id': data.get('product_tmpl_id'),
            })
            
            return FormatResponse(201, 'Product image created successfully', new_image).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API POST: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/product_images/<int:image_id>', type='http', auth='public', methods=['PUT'], csrf=False)
    def update_product_image(self, image_id, **kwargs):
        try:
            data = json.loads(request.httprequest.data)
            image = request.env['product.image'].sudo().search([('id', '=', image_id)], limit=1)

            if not image:
                return FormatResponse(404, 'Product image not found').to_response()

            # Cập nhật thông tin hình ảnh
            image.write({
                'name': data.get('name', image.name),
                'image': data.get('image', image.image),
                'product_tmpl_id': data.get('product_tmpl_id', image.product_tmpl_id.id),
            })
            
            image_data = {
                'id': image.id,
                'name': image.name,
                'image': image.image,
                'product_tmpl_id': image.product_tmpl_id.id,
            }
            
            return FormatResponse(200, 'Product image updated successfully', image_data).to_response()
        
        except Exception as e:
            _logger.error(f"Error in API PUT: {str(e)}")
            return FormatResponse(400, str(e)).to_response()

    @http.route('/api/product_images/<int:image_id>', type='http', auth='public', methods=['DELETE'], csrf=False)
    def delete_product_image(self, image_id, **kwargs):
        try:
            # Tìm hình ảnh theo ID
            image = request.env['product.image'].sudo().search([('id', '=', image_id)], limit=1)

            if not image:
                return FormatResponse(404, 'Product image not found').to_response()

            image.unlink()
            
            return FormatResponse(200, 'Product image deleted successfully').to_response()

        except Exception as e:
            _logger.error(f"Error in API DELETE: {str(e)}")
            return FormatResponse(400, str(e)).to_response()
