# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552320134.884161
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center', 'index_block', 'menu_list_items', 'site_left']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def index_block():
            return render_index_block(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def menu_list_items():
            return render_menu_list_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_list_items'):
            context['self'].menu_list_items(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        def index_block():
            return render_index_block(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index_block'):
            context['self'].index_block(**pageargs)
        

        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_index_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def index_block():
            return render_index_block(context)
        __M_writer = context.writer()
        __M_writer('\n    \n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_list_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_list_items():
            return render_menu_list_items(context)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- the python code inside the $ is making the \'home\' bold only when on the homepage -->\n  \n  <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else ''))
        __M_writer('">\n    <a class="nav-link" href="/homepage/about">About</a>\n  </li>\n  <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else ''))
        __M_writer('">\n    <a class="nav-link" href="/homepage/contact">Contact</a>\n  </li>\n  <li class="nav-item dropdown">\n    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n      Account\n    </a>\n      <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">\n')
        if request.user.is_authenticated:
            __M_writer('        <a class="dropdown-item" href="#">Settings</a>\n        <a class="dropdown-item" href="#">Payment</a>\n        <a class="dropdown-item" href="/account/logout">Logout</a>\n')
        else:
            __M_writer('        <a class="dropdown-item" href="/account/login">Login</a>\n')
        __M_writer('        \n      </div>\n  </li>        \n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n  Left Side. This text will override the text in base. :)<br>\n  <a href="index">Home</a><br>\n  <a href="contact">Contact</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 9, "54": 36, "64": 3, "72": 3, "77": 7, "83": 5, "89": 5, "95": 11, "103": 11, "104": 14, "105": 14, "106": 17, "107": 17, "108": 25, "109": 26, "110": 29, "111": 30, "112": 32, "118": 39, "124": 39, "130": 124}}
__M_END_METADATA
"""
