from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.contrib import auth  # 別忘了import auth

def login(request):

    '''
    if request.user.is_authenticated():
        #to index
        return HttpResponseRedirect('/')
    '''
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html')