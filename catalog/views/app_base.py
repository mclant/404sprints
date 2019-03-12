from django_mako_plus import view_function
from django.http import HttpResponse

@view_function
def process_request(request):
    return request.dmp.render('app_base.html', {})
