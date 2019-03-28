# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552939689.9004061
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content', 'site_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        numpages = context.get('numpages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        numpages = context.get('numpages', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <h1 class="text-center">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Products' if category is None else category.name))
        __M_writer('</h1>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        numpages = context.get('numpages', UNDEFINED)
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="catalog">\n')
        for product in products:
            __M_writer('            <span class="product_container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\n')
        __M_writer('    </div>\n    <div id="page-btn">\n')
        if page == 1:
            __M_writer('        <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('">Next Page</a>\n')
        elif page == numpages:
            __M_writer('        <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('">Previous Page</a>\n')
        else:
            __M_writer('        <a id="left-btn" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('">Previous Page</a>\n        <a id="right-btn" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id if category is not None else 0 ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('">Next Page</a>\n')
        __M_writer('    </div>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 23, "54": 3, "67": 3, "68": 5, "69": 5, "74": 22, "80": 6, "91": 6, "92": 8, "93": 9, "94": 9, "95": 9, "96": 11, "97": 13, "98": 14, "99": 14, "100": 14, "101": 14, "102": 14, "103": 15, "104": 16, "105": 16, "106": 16, "107": 16, "108": 16, "109": 17, "110": 18, "111": 18, "112": 18, "113": 18, "114": 18, "115": 19, "116": 19, "117": 19, "118": 19, "119": 21, "125": 119}}
__M_END_METADATA
"""
