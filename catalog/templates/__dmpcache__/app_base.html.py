# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552434781.186338
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/app_base.html'
_template_uri = 'app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_left']



from catalog import models as cmod 


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        self = context.get('self', UNDEFINED)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul id="category_list">\n        <li class=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category is None else ''))
        __M_writer('><a href="/catalog/index">All Products</li>\n')
        for cat in cmod.Category.objects.order_by('id'):
            __M_writer('            <li class=')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if category is None else ''))
            __M_writer('><a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cat.id ))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(django.utils.html.escape(cat.name )))
            __M_writer('</a></li>')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/catalog/templates/app_base.html", "uri": "app_base.html", "source_encoding": "utf-8", "line_map": {"18": 2, "33": 0, "42": 1, "43": 4, "53": 6, "61": 6, "62": 8, "63": 8, "64": 9, "65": 10, "66": 10, "67": 10, "68": 10, "69": 10, "70": 10, "71": 10, "72": 12, "78": 72}}
__M_END_METADATA
"""
