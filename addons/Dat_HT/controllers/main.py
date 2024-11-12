# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import json
from urllib.parse import urlparse, parse_qs

import requests
from werkzeug import urls
from werkzeug.exceptions import Forbidden
from werkzeug.utils import redirect

from odoo import _, http
from odoo.exceptions import ValidationError
from odoo.tools import html_escape

_logger = logging.getLogger(__name__)


class MainController(http.Controller):

    @http.route('/locations', type='http', auth="user", website=True)
    def get_locations(self):
        records = http.request.env['location.odoo'].search([])

        return http.request.render(
            # Tên templae (Khởi tạo trong views folder)
            "Dat_HT.location_list_template",

            # Object render
            ## Biến đầu tên là tên biến sẽ gọi trong template
            ## Biến thứ 2   là biến đã query ở trên
            {"locations": records},
        )
    
