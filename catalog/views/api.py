from django_mako_plus import view_function
from django.http import HttpResponse

@view_function
def process_request(request):
    return request.dmp.render('api.html', {})


def getdata(request):
    return HttpResponse("hey hey hey")