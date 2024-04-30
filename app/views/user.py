from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app.forms.user import UserLoginForm, UserRegisterForm

def register(request):
    template_name = 'registration/register.html'
    context = {}

    if request.method == 'GET':
        form = UserRegisterForm()
        context['form'] = form

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                # messages.add_message(request, constants.DEBUG, "Sua conta foi criada com sucesso.")
                return redirect('index')

    return render(request, template_name, context)

def login_view(request):
    template_name = 'registration/login.html'
    context = {}

    # if request.user.is_authenticated:
        # secure_redirect(request)

    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form

    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            
    return render(request, template_name, context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
