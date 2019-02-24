from django import forms
from django_mako_plus import view_function
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


@view_function
def process_request(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    
    return request.dmp.render('login.html',{
        'form': form,
    })

class MyForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Invalid Username or Password')
        return self.cleaned_data
    