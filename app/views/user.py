from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

from app.utils.ajax import AjaxListView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from app.forms.user import UserLoginForm, UserRegisterForm, UserForm, PermissionForm
from app.models import Profile

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

class UserList(AjaxListView):
    model = Profile
    template_name = 'user/list.html'
    partial_list = 'partials/user/list.html'


class UserUpdate(AjaxUpdateView):
  form_class = UserForm
  template_name = 'partials/user/update.html'
  success_url = reverse_lazy('user-list')

class UserDelete(AjaxDeleteView):
  model = Profile
  template_name = 'partials/user/delete.html'
  success_url = reverse_lazy('user-list')

class UserUpdatePermission(UpdateView):
    model = Profile
    form_class = PermissionForm
    template_name = 'user/change-permission.html'
    success_url = reverse_lazy('user-list')

    def get_initial(self):
        initial = super().get_initial()
        initial['is_staff'] = True   
        if self.object.is_staff:
            initial['is_staff'] = False  
        return initial

    def form_valid(self, form):
        # messages.success(self.request, f'A permissão de {form.instance} foi alterada com sucesso!')
        return super().form_valid(form)