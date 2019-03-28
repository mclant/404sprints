# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553719181.833915
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/catalog/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        allProductImages = context.get('allProductImages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        def site_center():
            return render_site_center(context)
        allProductImages = context.get('allProductImages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</h1>\n\n    <div>\n')
        for detailimage in allProductImages:
            __M_writer('        <img class="product_detail" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(detailimage.image_url()))
            __M_writer('"/>\n')
        __M_writer('\n        <div class="product-tile">\n\n            <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</div>\n            <div class="product-price">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</div>\n            <div class="product-description">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.description))
        __M_writer('</div>\n\n        </div>\n    </div>\n    <div>\n        <h1>Click here to purchase this item</h1>\n')
        if product.quantity == 0:
            __M_writer('        <p>quantity not available</p>\n')
        else:
            __M_writer('        <p>Quantity: ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.quantity))
            __M_writer('</p>\n')
        __M_writer('\n        <form method="POST" action="">\n            <table>\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
        __M_writer('\n            </table>\n            <input type="submit" value="Submit">\n        </form>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 4, "62": 4, "63": 7, "64": 8, "65": 8, "66": 8, "67": 10, "68": 13, "69": 13, "70": 14, "71": 14, "72": 15, "73": 15, "74": 21, "75": 22, "76": 23, "77": 24, "78": 24, "79": 24, "80": 26, "81": 29, "82": 29, "88": 82}}
__M_END_METADATA
"""
