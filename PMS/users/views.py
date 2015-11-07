from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render_to_response('users/index.html', {}, {})


def admin_home(request):
    if request.user.is_authenticated():
        #return HttpResponseRedirect('/users/home')
        #return HttpResponse("You are logged in.")
        return render_to_response('users/homepage-admin.html', {}, {})
    else:
        return HttpResponse("You are not logged in.")

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render_to_response('users/homepage-admin.html', {}, {})
                #return HttpResponse("You are logged in.")
                #return HttpResponseRedirect('/users/home')
            else:
                return HttpResponse("Account disabled.")
        else:
        
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:

        return render_to_response('users/login.html', {}, context)


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')