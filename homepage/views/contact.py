from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if request.method == "POST":
        print('>>>>>')
        print(request.POST)
        return HttpResponseRedirect('/homepage/about/')
    context = {

    }
    return request.dmp.render('contact.html', context)