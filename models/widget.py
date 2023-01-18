import shopify
import time
from odoo import models, fields, api
from odoo.http import request
from odoo.tools.safe_eval import datetime


class Widget(models.Model):
    _name = 'widget.info'
    _description = 'Widget Info'

    shopify_shop = fields.One2many('shopify.api', 'widget' , ondelete='cascade')



    widget_title = fields.Char(index=True,default='Hello wolrd')
    widget_description = fields.Char(index=True,default='Hello wolrd')
    num_product = fields.Char(index=True,default='0')
    total_price = fields.Char(index=True,default='0')
    status = fields.Char(index=True,default=False)
    title_color = fields.Char(index=True,default='#000000')
    des_color = fields.Char(index=True,default='#000000')
    text_color = fields.Char(index=True,default='#000000')
    background_color = fields.Char(index=True,default='#000000')
    border_color = fields.Char(index=True,default='#000000')
    title_font_size_value = fields.Char(index=True,default='10px')
    description_font_size_value = fields.Char(index=True,default='10px')
    button_text = fields.Char(index=True,default='Hi')
    layout_style = fields.Char(index=True,default='Hello wolrd')
    number_product_show = fields.Char(index=True,default='3')
    list_product = fields.Char(index=True)











