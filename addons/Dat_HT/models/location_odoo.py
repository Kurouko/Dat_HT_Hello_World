# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models


class EstateOdoo(models.Model):
    _name = 'location.odoo'
    _description = 'Vị trí'

    name = fields.Char(string='Tên vị trí')
    estate_ids = fields.One2many(
        comodel_name='estate.odoo', 
        inverse_name='location_id',  # This should be 'location_id' to establish the relation correctly
        string='Bất động sản'
    )
