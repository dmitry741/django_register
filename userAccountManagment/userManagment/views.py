from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
            #render_to_response('index.html', {'username': username, 'errors': True}, context_instance=RequestContext(request))

    raise Http404


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/')
    raise Http404

def register(request):
    return render(request, 'register.html')

def auth(request):
    return render(request, 'auth.html')