# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553985018.919075
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        si = context.get('si', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        si = context.get('si', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <h2>your shopping cart:</h2>\n\n    <table style="width:100%">\n        <tr>\n            <th>Product Image</th>\n            <th>Product Name</th>\n            <th>Quantity</th>\n            <th>Price</th>\n            <th>Extended</th>\n            <th>Actions</th>\n        </tr>\n')
        for item in si:
            __M_writer('        <tr>\n            <td></td>\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('</td>\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('</td>\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
            __M_writer('</td>\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.price))
            __M_writer('</td>\n            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.price))
            __M_writer('</td>\n            <td><button>Delete</button></td>\n        </tr>\n')
        __M_writer('    </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 16, "58": 17, "59": 19, "60": 19, "61": 20, "62": 20, "63": 21, "64": 21, "65": 22, "66": 22, "67": 23, "68": 23, "69": 27, "75": 69}}
__M_END_METADATA
"""
