import shopify
import time
from odoo import models, fields, api
from odoo.http import request
from odoo.tools.safe_eval import datetime


class SApp(models.Model):
    _name = 'shopify.api'
    _description = 'Shopify App'
    _rec_name = "shop_url"

    shop_url = fields.Char(index=True)

    sp_access_token = fields.Char()
    # cdn_tag = fields.Char()

    currency = fields.Char(string="Currency")
    email = fields.Char(string="Email")
    shop_name = fields.Char(string="Shop name")
    shop_id = fields.Char(string="Shop ID")
    user = fields.Many2one('res.users', "User")
    widget = fields.Many2one("widget.info", string='Widget')

    def initShopifySession(self):
        # sp_api_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_key')
        # sp_api_secret_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_secret_key')

        api_version = request.env['ir.config_parameter'].sudo().get_param('bought_together.api_version_bought_together')


        new_session = shopify.Session(self.shop_url, api_version, token=self.sp_access_token)
        shopify.ShopifyResource.activate_session(new_session)
        return new_session







