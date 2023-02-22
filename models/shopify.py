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
    script_tag = fields.Char(string='Script Tag')
    is_update_script_tag = fields.Boolean(default=True)




    @api.model
    def initShopifySession(self,shop):
        # sp_api_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_key')
        # sp_api_secret_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_secret_key')

        api_version = self.env['ir.config_parameter'].sudo().get_param('bought_together.api_version_bought_together')


        new_session = shopify.Session(self.shop_url, api_version, token=self.sp_access_token)
        shopify.ShopifyResource.activate_session(new_session)
        return new_session

    # Todo: Thêm một field Boolean tên là is_update_script_tag (default=True)

    # Todo: Viết một hàm cron job check mỗi 30 phút. Trong hàm này sẽ tìm các shop mà có is_update_script_tag = False (giới hạn tìm 30 bản ghi).
    # Với mỗi shop tìm được thì chạy hàm update_script_tag

    # Todo: viết hàm update script tag bên này

    def auto_update_script_tag(self):
        shop_scrip_tag_false =  self.search([('is_update_script_tag', '=', False)], limit=30)
        for shop in shop_scrip_tag_false:
            if shop:
                shop.update_script_tag(shop)
    def update_script_tag(self,shop):
        # Todo: Đưa phần này sang model shopify.api

        self.initShopifySession(shop)
        scripTag = shopify.ScriptTag.find()
        for script in scripTag:
            if self.script_tag.split('/')[len(self.script_tag.split('/'))-1] in script.src:
                script.destroy()
        if self.script_tag:
            scripTagCreate = shopify.ScriptTag.create({
                "event": "onload",
                "src": self.script_tag + "?v=" + str(time.time())
            })
            return scripTagCreate.id
        # ===============================================


