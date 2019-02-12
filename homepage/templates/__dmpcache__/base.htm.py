# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549914228.0406091
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title_block', 'menu_list_items', 'site_left', 'site_center', 'site_right']


 
from datetime import datetime 


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title_block():
            return render_title_block(context._locals(__M_locals))
        def menu_list_items():
            return render_menu_list_items(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n        <link rel="icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" />\n        \n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL))
        __M_writer('homepage/media/node_modules/jquery-3.3.1.min.js"></script>\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL))
        __M_writer('homepage/media/node_modules/bootstrap/css/bootstrap.min.css" />\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL))
        __M_writer('homepage/media/node_modules/bootstrap/js/bootstrap.min.js"></script>\n       \n')
        __M_writer('\n        <title>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title_block'):
            context['self'].title_block(**pageargs)
        

        __M_writer('\n        </title>\n\n')
        __M_writer('        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n        <div id="maintenance_message" class="alert alert-danger">The server will explode tonight. sorry</div>\n        \n        \n        <header>\n            <nav class="navbar navbar-expand-lg navbar-dark bg-dark" id="my_navbar">\n                <img id="top_left_icon" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" />\n                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">\n                    <span class="navbar-toggler-icon"></span>\n                </button>\n                <div class="collapse navbar-collapse" id="navbarNavDropdown">\n                    <ul class="navbar-nav">\n                        <li class="nav-item ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else ''))
        __M_writer('">\n                            <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>\n                        </li>\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_list_items'):
            context['self'].menu_list_items(**pageargs)
        

        __M_writer('\n                    </ul>\n                </div>\n            </nav>\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="python" />\n            <div class="title">Welcome to <br/> DMP!</div>\n        </header>\n\n        <main>\n\n            <div id="site_left">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\n            </div>\n\n            <div id="site_center">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n            </div>\n\n            <div id="site_right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\n            </div>\n        </main>\n\n        <footer>\n            <div>Current Year: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().year ))
        __M_writer('</div>\n            <div>&copy; Copyright Matt Lant</div>\n        </footer>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title_block():
            return render_title_block(context)
        __M_writer = context.writer()
        __M_writer('\n                DMP\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_list_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_list_items():
            return render_menu_list_items(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n                    Left Side\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n                    Center this text will be replaced\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\n                    Right Side\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 3, "22": 0, "40": 2, "41": 5, "42": 10, "43": 10, "44": 12, "45": 12, "46": 13, "47": 13, "48": 14, "49": 14, "50": 17, "55": 21, "56": 25, "57": 28, "58": 29, "59": 29, "60": 38, "61": 38, "62": 44, "63": 44, "68": 47, "69": 51, "70": 51, "75": 60, "80": 66, "85": 72, "86": 77, "87": 77, "93": 19, "99": 19, "105": 47, "116": 58, "122": 58, "128": 64, "134": 64, "140": 70, "146": 70, "152": 146}}
__M_END_METADATA
"""