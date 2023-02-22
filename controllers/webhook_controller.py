from odoo import http
from odoo.http import request, Response


class WebhookController(http.Controller):
    @http.route("/webhook/<string:topic>/<string:shopify_id>", auth="public", type="json", csrf=False, cors="*", save_session=False)
    def webhook_order_create(self, topic, shopify_id):
        try:
            if 'product' in topic:
                print(request.jsonrequest)
                # if 'update' in topic:
                #     exist_product = request.env['shop.product'].sudo().search([('shop_id', '=', request.env['shop.shopify'].sudo().search([("shopify_id", '=', shopify_id)]).id), ("shopify_product_id", '=', request.jsonrequest['id'])])
                #     if exist_product:
                #         for variant in request.jsonrequest['variants']:
                #             if str(variant['id']) == exist_product.variant_id:
                #                 exist_product.sudo().write({
                #                     'name': request.jsonrequest['title'],
                #                     'price': float(variant['price']),
                #                     'shop_id': request.env['shop.shopify'].sudo().search([("shopify_id", '=', shopify_id)]).id
                #                 })
                # if "create" in topic:
                #     request.env['shop.product'].sudo().create({
                #         'name': request.jsonrequest['title'],
                #         'variant_id': request.jsonrequest['variants'][0]['id'],
                #         'shop_id': request.env['shop.shopify'].sudo().search([("shopify_id", '=', shopify_id)]).id,
                #         "shopify_product_id": request.jsonrequest['id'],
                #         "price": float(request.jsonrequest['variants'][0]['price']),
                #         'url_img': request.jsonrequest['image']['src']
                #     })

            return Response("success", status=200)
        except Exception as err:
            print(err)