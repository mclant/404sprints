# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549409097.486733
_enable_loop = True
_template_filename = '/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['index_block']


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
        utc_time = context.get('utc_time', UNDEFINED)
        def index_block():
            return render_index_block(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'index_block'):
            context['self'].index_block(**pageargs)
        

        __M_writer('\n\n<!--\n    It says to assign background colors to all the blocks here so i added it in the index.scss file\n-->')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_index_block(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        utc_time = context.get('utc_time', UNDEFINED)
        def index_block():
            return render_index_block(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n        <h3>Congratulations -- you\'ve successfully created a new DMP appppppp!</h3>\n        <h4 class="utc-time">Current time in UTC: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( utc_time ))
        __M_writer('</h4>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Matt/Documents/School/IS 413/sprint1/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 8, "49": 3, "57": 3, "58": 6, "59": 6, "65": 59}}
__M_END_METADATA
"""
