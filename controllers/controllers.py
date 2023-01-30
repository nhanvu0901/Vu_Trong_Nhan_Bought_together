# -*- coding: utf-8 -*-
import binascii
import os
import json
import random
import requests
import shopify
import werkzeug
import string
from odoo import http
from odoo.http import request


class BoughtTogether(http.Controller):
    @http.route('/bought_together', auth='public' ,type="http", website=True)
    def index(self, **kw):
        shopify_app_exist = request.env['shopify.api'].sudo().search([('shop_url', '=', kw["shop_url"])], limit=1)
        if request.env.user and request.env.user.id == shopify_app_exist.user.id:
            return request.render("bought_together.bought_together")
        elif not shopify_app_exist.user:
            return request.render("bought_together.bought_together")
        else:
            return """<html>
                <head>
                    <style>
                      @import url(https://fonts.googleapis.com/css?family=Roboto:400,100,300,500);

        body { 
          background-color: #007aff; 
          color: #fff;
          font-size: 100%;
          line-height: 1.5;
          font-family: "Roboto", sans-serif;
        }

        .button {
          font-weight: 300;
          color: #fff;
          font-size: 1.2em;
          text-decoration: none;
          border: 1px solid #efefef;
          padding: .5em;
          border-radius: 3px;
          float: left;
          margin: 6em 0 0 -155px;
          left: 50%;
          position: relative;
          transition: all .3s linear;
        }

        .button:hover {
          background-color: #007aff;
          color: #fff;
        }

        p {
          font-size: 2em;
          text-align: center;
          font-weight: 100;
        }

        h1 {
          text-align: center;
          font-size: 15em;
          font-weight: 100;
          text-shadow: #0062cc 1px 1px, #0062cc 2px 2px, #0062cc 3px 3px, #0062cd 4px 4px, #0062cd 5px 5px, #0062cd 6px 6px, #0062cd 7px 7px, #0062ce 8px 8px, #0063ce 9px 9px, #0063ce 10px 10px, #0063ce 11px 11px, #0063cf 12px 12px, #0063cf 13px 13px, #0063cf 14px 14px, #0063cf 15px 15px, #0063d0 16px 16px, #0064d0 17px 17px, #0064d0 18px 18px, #0064d0 19px 19px, #0064d1 20px 20px, #0064d1 21px 21px, #0064d1 22px 22px, #0064d1 23px 23px, #0064d2 24px 24px, #0065d2 25px 25px, #0065d2 26px 26px, #0065d2 27px 27px, #0065d3 28px 28px, #0065d3 29px 29px, #0065d3 30px 30px, #0065d3 31px 31px, #0065d4 32px 32px, #0065d4 33px 33px, #0066d4 34px 34px, #0066d4 35px 35px, #0066d5 36px 36px, #0066d5 37px 37px, #0066d5 38px 38px, #0066d5 39px 39px, #0066d6 40px 40px, #0066d6 41px 41px, #0067d6 42px 42px, #0067d6 43px 43px, #0067d7 44px 44px, #0067d7 45px 45px, #0067d7 46px 46px, #0067d7 47px 47px, #0067d8 48px 48px, #0067d8 49px 49px, #0068d8 50px 50px, #0068d9 51px 51px, #0068d9 52px 52px, #0068d9 53px 53px, #0068d9 54px 54px, #0068da 55px 55px, #0068da 56px 56px, #0068da 57px 57px, #0068da 58px 58px, #0069db 59px 59px, #0069db 60px 60px, #0069db 61px 61px, #0069db 62px 62px, #0069dc 63px 63px, #0069dc 64px 64px, #0069dc 65px 65px, #0069dc 66px 66px, #006add 67px 67px, #006add 68px 68px, #006add 69px 69px, #006add 70px 70px, #006ade 71px 71px, #006ade 72px 72px, #006ade 73px 73px, #006ade 74px 74px, #006bdf 75px 75px, #006bdf 76px 76px, #006bdf 77px 77px, #006bdf 78px 78px, #006be0 79px 79px, #006be0 80px 80px, #006be0 81px 81px, #006be0 82px 82px, #006be1 83px 83px, #006ce1 84px 84px, #006ce1 85px 85px, #006ce1 86px 86px, #006ce2 87px 87px, #006ce2 88px 88px, #006ce2 89px 89px, #006ce2 90px 90px, #006ce3 91px 91px, #006de3 92px 92px, #006de3 93px 93px, #006de3 94px 94px, #006de4 95px 95px, #006de4 96px 96px, #006de4 97px 97px, #006de4 98px 98px, #006de5 99px 99px, #006ee5 100px 100px, #006ee5 101px 101px, #006ee6 102px 102px, #006ee6 103px 103px, #006ee6 104px 104px, #006ee6 105px 105px, #006ee7 106px 106px, #006ee7 107px 107px, #006ee7 108px 108px, #006fe7 109px 109px, #006fe8 110px 110px, #006fe8 111px 111px, #006fe8 112px 112px, #006fe8 113px 113px, #006fe9 114px 114px, #006fe9 115px 115px, #006fe9 116px 116px, #0070e9 117px 117px, #0070ea 118px 118px, #0070ea 119px 119px, #0070ea 120px 120px, #0070ea 121px 121px, #0070eb 122px 122px, #0070eb 123px 123px, #0070eb 124px 124px, #0071eb 125px 125px, #0071ec 126px 126px, #0071ec 127px 127px, #0071ec 128px 128px, #0071ec 129px 129px, #0071ed 130px 130px, #0071ed 131px 131px, #0071ed 132px 132px, #0071ed 133px 133px, #0072ee 134px 134px, #0072ee 135px 135px, #0072ee 136px 136px, #0072ee 137px 137px, #0072ef 138px 138px, #0072ef 139px 139px, #0072ef 140px 140px, #0072ef 141px 141px, #0073f0 142px 142px, #0073f0 143px 143px, #0073f0 144px 144px, #0073f0 145px 145px, #0073f1 146px 146px, #0073f1 147px 147px, #0073f1 148px 148px, #0073f1 149px 149px, #0074f2 150px 150px, #0074f2 151px 151px, #0074f2 152px 152px, #0074f3 153px 153px, #0074f3 154px 154px, #0074f3 155px 155px, #0074f3 156px 156px, #0074f4 157px 157px, #0074f4 158px 158px, #0075f4 159px 159px, #0075f4 160px 160px, #0075f5 161px 161px, #0075f5 162px 162px, #0075f5 163px 163px, #0075f5 164px 164px, #0075f6 165px 165px, #0075f6 166px 166px, #0076f6 167px 167px, #0076f6 168px 168px, #0076f7 169px 169px, #0076f7 170px 170px, #0076f7 171px 171px, #0076f7 172px 172px, #0076f8 173px 173px, #0076f8 174px 174px, #0077f8 175px 175px, #0077f8 176px 176px, #0077f9 177px 177px, #0077f9 178px 178px, #0077f9 179px 179px, #0077f9 180px 180px, #0077fa 181px 181px, #0077fa 182px 182px, #0077fa 183px 183px, #0078fa 184px 184px, #0078fb 185px 185px, #0078fb 186px 186px, #0078fb 187px 187px, #0078fb 188px 188px, #0078fc 189px 189px, #0078fc 190px 190px, #0078fc 191px 191px, #0079fc 192px 192px, #0079fd 193px 193px, #0079fd 194px 194px, #0079fd 195px 195px, #0079fd 196px 196px, #0079fe 197px 197px, #0079fe 198px 198px, #0079fe 199px 199px, #007aff 200px 200px;
        }
                    </style>
                </head>
        <body><h1>404</h1><p>Oops! Something is wrong.</p><a class="button" href="#"><i class="icon-home"></i> Go back in initial page, is better.</a></body></html>"""





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


        current_user = request.env.user

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
                # "user": current_user.id,
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
                # "user": current_user.id,

                "widget":widget_create.id,
                "currency":shop.currency,
                "script_tag": script_tag,
                "is_update_script_tag": True

            })
            # TOdo: Check xem có tồn tại người dùng hay không
            # if request.env.user:
            #   shopify_app_exist.admin = request.env.user

            # TOdo: tạo một trang trên front end để người dùng điền link store vào trong trường hợp store chưa gắn với người dùng nào
            # tao nguoi dung moi
        print(shopify_app_exist)
        web_base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        redirectUrl = web_base_url + '/bought_together'



        # Todo: kiểm tra người dùng hiện tại có trùng với người dùng gắn với store hay không

        return werkzeug.utils.redirect(redirectUrl + "?shop_url=%s" % (shop.domain))

        # else:
        # báo lỗi




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

    @http.route('/make_draft_order', type='json', auth='none', cors='*', csrf=False, save_session=False)
    def make_draft_order(self, **kw):
        print(kw)

        if request.jsonrequest:
            shop_url =request.jsonrequest.get('shop_url')
            product_list = request.jsonrequest.get('product_list')
            shopify_exist = request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)
            shopify_exist.initShopifySession(shopify_exist)
            line_items=[]
            values={}
            for i in product_list:
                product={
                    "title":i.get('item'),
                    "id":i.get('id'),
                    "price": i.get('item_price'),
                    "quantity":1
                }
                line_items.append(product)
            values['line_items'] = line_items
            ordercreate = shopify.DraftOrder.create(values)
            return json.dumps(ordercreate.invoice_url)
    @http.route('/authenticate/user', type='json', auth='user', cors='*', csrf=False, save_session=False)
    def authentocate_user(self, **kw):
        print(request.jsonrequest)

        shop_url = request.jsonrequest.get('shop_url')


        current_user = request.env.user

        # check xem shop da duoc gan voi thang nao chua
        current_shop = request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)


        flag = False
        #neu chua co thi gan thang user hien tai vao
        if not current_shop:
            flag = True
            return json.dumps(flag)
        if not current_shop.user:
            current_shop.write({
                "user":current_user.id
            })
        else:
            flag = True

        return json.dumps(flag)

    @http.route('/get_current_user_info', type='json', auth='user', cors='*', csrf=False, save_session=False)
    def get_current_user_info(self, **kw):
        shop_url = request.jsonrequest.get('shop_url')
        current_user = request.env.user
        current_shop = request.env['shopify.api'].sudo().search([('shop_url', '=', shop_url)], limit=1)
        if current_user.id == current_shop.user.id:
            user = {
                'name':current_user.name,
                "image_url": current_user.image_1920.decode("utf-8")
            }
            return json.dumps(user)







