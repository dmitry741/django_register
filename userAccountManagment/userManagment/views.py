from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from .forms import MyRegistrationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'auth.html', {'username': username, 'errors': True})
    raise Http404


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/')
    raise Http404


def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'register.html', context)
    context = {'form': MyRegistrationForm()}
    return render(request, 'register.html', context)


def myauthuser(request):
    return render(request, 'auth.html')