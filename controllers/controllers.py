# -*- coding: utf-8 -*-
import binascii
import os
import json

import requests
import shopify
import werkzeug

from odoo import http
from odoo.http import request


class BoughtTogether(http.Controller):
    @http.route('/bought_together', auth='public' ,type="http", website=True)
    def index(self, **kw):
        return request.render("bought_together.bought_together")




    @http.route('/test_bought_together', type='http', auth="public", website=True, method=['GET'], csrf=False)
    def setupApp(self, **kw):
        sp_api_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_key_bought_together')
        sp_api_secret_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_secret_key_bought_together')
        shop_url = kw['shop']

        api_version = request.env['ir.config_parameter'].sudo().get_param('bought_together.api_version_bought_together')
        redirect_url = request.env['ir.config_parameter'].sudo().get_param('bought_together.redirect_url_bought_together')

        shopify.Session.setup(api_key=sp_api_key, secret=sp_api_secret_key)


        state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
        redirect_uri = redirect_url
        scopes = ['read_products', "read_customers", "write_customers", "read_third_party_fulfillment_orders",
                  "write_third_party_fulfillment_orders", "read_orders", "write_orders", "write_products",
                  "write_draft_orders", "read_draft_orders", "write_script_tags", "read_script_tags",
                  "read_shipping", "read_themes", "write_themes", "read_price_rules"]

        newSession = shopify.Session(shop_url, api_version)
        auth_url = newSession.create_permission_url(scopes, redirect_uri, state)

        return werkzeug.utils.redirect(auth_url)

    @http.route('/bought_together_redirect', type='http', auth='public')
    def redirect(self, **kw):

        sp_api_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_key_bought_together')
        sp_api_secret_key = request.env['ir.config_parameter'].sudo().get_param('bought_together.sp_api_secret_key_bought_together')
        api_version = request.env['ir.config_parameter'].sudo().get_param('bought_together.api_version_bought_together')
        script_tag = request.env['ir.config_parameter'].sudo().get_param('bought_together.cdn_tag_bought_together')
        shop_url = kw['shop']



        shopify.Session.setup(
            api_key=sp_api_key,
            secret=sp_api_secret_key)
        shopify_session = shopify.Session(shop_url, api_version)
        access_token = shopify_session.request_token(kw)
        shopify.ShopifyResource.activate_session(shopify_session)

        shop = shopify.Shop.current()


        current_user = request.env['res.users'].sudo().search([('login', '=', kw['shop'])],
                                                              limit=1)
        domain = shop.domain

        shopify_app_enviroment = request.env['shopify.api']
        shopify_app_exist = request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)
        widget = request.env['widget.info']
        if shopify_app_exist:
            shopify_app_exist.write({
                "shop_url": domain,

                "sp_access_token": access_token,
                "email": shop.email,
                "shop_name": shop.name,
                "shop_id": shop.id,
                "user": current_user.id,
                "script_tag":script_tag,
                "is_update_script_tag":True
            })
        else:
            widget_create = widget.create({

                "widget_title": 'Hello wolrd',
                "widget_description": 'Hello wolrd',
                "num_product":'Hello wolrd',
                "total_price":'0',
                "status": False,
                "title_color":'#000000',
                "des_color":'#000000',
                "text_color":'#ffffff',
                "background_color": '#3584e4',
                "border_color": '#3584e4',
                "title_font_size_value": '10px',
                "description_font_size_value":'10px',
                "button_text": 'Buy Now',
                "layout_style": '',
                "number_product_show": '',
                "list_product": '',
            })
            shopify_app_exist = shopify_app_enviroment.create({
                "shop_url": domain,

                "sp_access_token": access_token,
                 "email": shop.email,
                "shop_name": shop.name,
                "shop_id": shop.id,
                "user": current_user.id,

                "widget":widget_create.id,
                "currency":shop.currency,
                "script_tag": script_tag,
                "is_update_script_tag": True

            })

        print(shopify_app_exist)
        web_base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        redirectUrl = web_base_url + '/bought_together'
        return werkzeug.utils.redirect(redirectUrl+"?shop_url=%s"%(shop.domain))



    @http.route('/fetch_product', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def main(self, **kw):
        global product_image, varient_price, varient_quantity,varient_compare_at_price
        if request.jsonrequest:
            shop_url = request.jsonrequest['shop_url']
            shopify_exist = request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)
            shopify_exist.initShopifySession(shopify_exist)
            # data_shopify = shopify.Product.find()
            client = shopify.GraphQL()
            shop = shopify.Shop.current()
            currency = shop.currency
            query = """
            {
                        products(first: 20) {
                            edges {
                                node {
                                    id
                                    title
                                     variants(first: 10) {
                                      edges {
                    			node {
                    			   price
                    			   inventoryQuantity
                                    	   compareAtPrice


                    			}
                    		    }
                                     }
                                     images(first:1){
            		            edges{
            		                node{ url }
            		            }
            		        }
                                }
                            }
                        }    
                    } 
            """
            result = client.execute(query)


            list_product=[]
            products =  json.loads(result)['data']['products']['edges']
            for product in products:
                item = {
                        "product_id": product['node'].get('id').split('/')[len(product['node'].get('id').split('/'))-1],
                        "product_img":product['node'].get("images").get('edges')[0].get('node').get('url'),
                        "product_name":product['node'].get("title"),
                        "product_price": product['node'].get('variants').get("edges")[0].get("node").get("price"),
                        "product_compare_at_price":product['node'].get('variants').get("edges")[0].get("node").get("compareAtPrice"),
                        "quantity": product['node'].get('variants').get("edges")[0].get("node").get("inventoryQuantity"),
                        "currency":currency
                    }
                list_product.append(item)
            # for data in data_shopify:
            #     print(data)
            #     varient = shopify.Product.find(data.get_id()).variants
            #     for i in varient:
            #         varient_price = i.price
            #         varient_quantity = i.inventory_quantity
            #         varient_compare_at_price = i.compare_at_price
            #     images = shopify.Product.find(data.get_id()).images
            #     for i in images:
            #         product_image = i.src
            #     item = {
            #
            #         "product_id": data.id,
            #         "product_img":product_image,
            #         "product_name":shopify.Product.find(data.get_id()).title,
            #         "product_price": varient_price,
            #         "product_compare_at_price":varient_compare_at_price,
            #         "quantity": varient_quantity,
            #         "currency":currency
            #     }



            return json.dumps(list_product)

    @http.route('/widget_data', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def save_widget_data(self, **kw):

        if(request.jsonrequest):
            print(request.jsonrequest)
            shop_url = request.jsonrequest['shop_url']

            widget_exist = request.env['widget.info'].sudo().search(
                [('shopify_shop.shop_url', '=', shop_url)], limit=1)

            keys_to_exclude = ['shop_url','id']
            new_dict = {k: v for k, v in request.jsonrequest.items() if k not in keys_to_exclude}
            print(new_dict)



            if(widget_exist):
                widget_exist.write(
                  new_dict
                    # "widget_title":request.jsonrequest.get('widget_title'),
                    # "widget_description": request.jsonrequest.get('widget_description'),
                    # "num_product": request.jsonrequest.get('num_product'),
                    # "total_price": request.jsonrequest.get('total_price'),
                    # "status": request.jsonrequest.get('status'),
                    # "title_color": request.jsonrequest.get('title_color'),
                    # "des_color": request.jsonrequest.get('des_color'),
                    # "text_color": request.jsonrequest.get('text_color'),
                    # "background_color": request.jsonrequest.get('background_color'),
                    # "border_color": request.jsonrequest.get('border_color'),
                    # "title_font_size_value": request.jsonrequest.get('title_font_size_value'),
                    # "description_font_size_value": request.jsonrequest.get('description_font_size_value'),
                    # "button_text": request.jsonrequest.get('button_text'),
                    # "layout_style": request.jsonrequest.get('layout_style'),
                    # "number_product_show": request.jsonrequest.get('number_product_show'),
                    # "list_product": request.jsonrequest.get('list_product'),
                )
            else:
                widget_exist.create(
                    new_dict
                    # "widget_title": request.jsonrequest.get('widget_title'),
                    # "widget_description": request.jsonrequest.get('widget_description'),
                    # "num_product": request.jsonrequest.get('num_product'),
                    # "total_price": request.jsonrequest.get('total_price'),
                    # "status": request.jsonrequest.get('status'),
                    # "title_color": request.jsonrequest.get('title_color'),
                    # "des_color": request.jsonrequest.get('des_color'),
                    # "text_color": request.jsonrequest.get('text_color'),
                    # "background_color": request.jsonrequest.get('background_color'),
                    # "border_color": request.jsonrequest.get('border_color'),
                    # "title_font_size_value": request.jsonrequest.get('title_font_size_value'),
                    # "description_font_size_value": request.jsonrequest.get('description_font_size_value'),
                    # "button_text": request.jsonrequest.get('button_text'),
                    # "layout_style": request.jsonrequest.get('layout_style'),
                    # "number_product_show": request.jsonrequest.get('number_product_show'),
                    # "list_product": request.jsonrequest.get('list_product'),
                )

    @http.route('/get_widget_data', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def get_widget_data(self, **kw):
        if request.jsonrequest:
            shop_url = request.jsonrequest['shop_url']
            shopify_exist =  request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)
            widget_exist = request.env['widget.info'].sudo().search(
                [('shopify_shop.shop_url', '=',shop_url)], limit=1)
            print(widget_exist)

            data = {

                "widget_title": widget_exist.widget_title,
                "widget_description": widget_exist.widget_description,
                "num_product": widget_exist.num_product,
                "total_price": widget_exist.total_price,
                "status": widget_exist.status,
                "title_color": widget_exist.title_color,
                "des_color": widget_exist.des_color,
                "text_color": widget_exist.text_color,
                "background_color": widget_exist.background_color,
                "border_color": widget_exist.border_color,
                "title_font_size_value": widget_exist.title_font_size_value,
                "description_font_size_value": widget_exist.description_font_size_value,
                "button_text": widget_exist.button_text,
                "layout_style": widget_exist.layout_style,
                "number_product_show": widget_exist.number_product_show,
                "list_product":json.dumps(widget_exist.list_product),
                "currency":shopify_exist.currency
            }
            return json.dumps(data)

    @http.route('/modify_status', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def change_widget_status(self, **kw):
        if request.jsonrequest:
            shop_url = request.jsonrequest['shop_url']

            widget_exist = request.env['widget.info'].sudo().search(
                [('shopify_shop.shop_url', '=', shop_url)], limit=1)
            status = request.jsonrequest.get('status')

            if(widget_exist):
                widget_exist.write({
                    "status": status,
                })
        return "Hello"



    @http.route('/return_api_instagram', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def get_access_token_instagram(self, **kw):
        if request.jsonrequest:
            print("Helloi")
        return "Hello"

