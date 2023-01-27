# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import shopify

from odoo import fields, models, api

import time

from odoo.http import request


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    api_version_bought_together = fields.Char(string='Api version', config_parameter="bought_together.api_version_bought_together")
    redirect_url_bought_together = fields.Char(string="Redirect URL", config_parameter="bought_together.redirect_url_bought_together")
    sp_api_key_bought_together = fields.Char(string='API Key', config_parameter="bought_together.sp_api_key_bought_together")
    sp_api_secret_key_bought_together = fields.Char(string='API secret key', config_parameter="bought_together.sp_api_secret_key_bought_together")
    cdn_tag_bought_together = fields.Char(string='CDN tag', config_parameter="bought_together.cdn_tag_bought_together")




    # def add_script_tag_to_shop_bought_together(self):
    #     src = self.cdn_tag_bought_together
    #
    #     #TODO sua shop url
    #     #shop_url = request.env['ir.config_parameter'].sudo().get_param('bought_together.shop_url_bought_together')
    #
    #     api_version = request.env['ir.config_parameter'].sudo().get_param('bought_together.api_version_bought_together')
    #
    #     #TODO sua shop url
    #     shopify_app_exist = request.env['shopify.api'].sudo().search([('shop_url', '=', "shoplify-odoo.myshopify.com")], limit=1)
    #
    #     new_session = shopify.Session("shoplify-odoo.myshopify.com", api_version, token=shopify_app_exist.sp_access_token)
    #     shopify.ShopifyResource.activate_session(new_session)
    #
    #     scripTag = shopify.ScriptTag.find()
    #     for script in scripTag:
    #         if "scriptag.js" in script.src:
    #             script.destroy()
    #     if src:
    #         scripTagCreate = shopify.ScriptTag.create({
    #             "event": "onload",
    #             "src": src + "?v=" + str(time.time())
    #         })
    #         return scripTagCreate.id

    def add_script_tag_to_shop_bought_together(self):
        request.env['shopify.api'].sudo().search([]).write({'is_update_script_tag':False})
