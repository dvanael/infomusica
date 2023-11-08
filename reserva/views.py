from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User, Group 
from django.contrib.auth import authenticate, login, forms, views

from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView

from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import UsuarioForm, PerfilForm, ProfileEditForm, SolicitacaoForm, StatusForm
from .models import Solicitacao, Perfil

# -- INDEX --
class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(GroupRequiredMixin, ListView):
    group_required = [u'Aluno',u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'dashboard.html' 

    def get_queryset(self):
        queryset = self.model.objects.filter(status = 3)
        return queryset    

# -- SOLICITACAO CRUD --
# -- FUNCTION BASED VIEWS -- 
# SAVE FORM
def save_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            
            if request.user.groups.filter(name = u'Admin'):
                solicitacoes = Solicitacao.objects.all().order_by('-post')

            else:
                solicitacoes = Solicitacao.objects.filter(profile = Perfil.objects.get(user = request.user)).order_by('-post')
            
            paginator = Paginator(solicitacoes, 7)
            page = request.GET.get('page')

            try:
                solicitacoes = paginator.page(page)
            except PageNotAnInteger:
                solicitacoes = paginator.page(1)
            except EmptyPage:
                solicitacoes = paginator.page(paginator.num_pages)


            if request.user.groups.filter(name = u'Admin'):
                data['html_list'] = render_to_string("lista/adm-parcial-list.html", {'object_list': solicitacoes})
            else:
                data['html_list'] = render_to_string("lista/parcial-list.html", {'object_list': solicitacoes})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)

# SOLICITACO CREATE
def solicitacao_create(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        form.instance.profile = Perfil.objects.get(user=request.user)

    else:
        form = SolicitacaoForm()
        form.instance.profile = Perfil.objects.get(user=request.user)
    
    return save_form(request, form, "lista/parcial-create.html")

# SOLICITACAO UPDATE
def solicitacao_update(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, instance=solicitacao)
        
    else:
        form = SolicitacaoForm(instance=solicitacao)

    return save_form(request, form, "lista/parcial-update.html")


# SOLICITACAO DELETE
def solicitacao_delete(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    data = dict()

    if request.method == 'POST':
        solicitacao.delete()
        data['form_is_valid'] = True
        
        if request.user.groups.filter(name = u'Admin'):
            solicitacoes = Solicitacao.objects.all().order_by('-post')

        else:
            solicitacoes = Solicitacao.objects.filter(profile = Perfil.objects.get(user = request.user)).order_by('-post')

        paginator = Paginator(solicitacoes, 7)  
        page = request.GET.get('page')

        try:
            solicitacoes = paginator.page(page)
        except PageNotAnInteger:
            solicitacoes = paginator.page(1)
        except EmptyPage:
            solicitacoes = paginator.page(paginator.num_pages)

        if request.user.groups.filter(name = u'Admin'):
            data['html_list'] = render_to_string("lista/adm-parcial-list.html", {'object_list': solicitacoes})
        else:
            data['html_list'] = render_to_string("lista/parcial-list.html", {'object_list': solicitacoes})  
    else:
        context = {'solicitacao': solicitacao}
        data['html_form'] = render_to_string('lista/parcial-delete.html', context, request=request)
    
    return JsonResponse(data)

# SOLICITACAO STATUS UPDATE
def status_update(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=solicitacao)
        
    else:
        form = StatusForm(instance=solicitacao)

    return save_form(request, form, "lista/status-parcial-update.html")

# -- CLASS BASED VIEWS -- 

# LIST
class SolicitacaoList(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'lista/solicitacao.html'
    content_object_name = 'object_list'

    paginate_by = 7
        
    def get_queryset(self):
        if self.request.user.groups.filter(name = u'Admin'):
            queryset = Solicitacao.objects.all().order_by('-post')

        else:
            queryset = Solicitacao.objects.filter(profile = Perfil.objects.get(user = self.request.user)).order_by('-post')
            
        filtro_data = self.request.GET.get('filtro_data', None)

        if filtro_data == 'ultima_semana':
            queryset = queryset.filter(data__range=[timezone.now()- timezone.timedelta(days=7), timezone.now()])

        elif filtro_data == 'ultimo_mes':
            queryset = queryset.filter(data__range=[timezone.now()- timezone.timedelta(days=30), timezone.now()])

        elif filtro_data == 'prox_semana':
            queryset = queryset.filter(data__range=[timezone.now(), timezone.now()+ timezone.timedelta(days=7)])

        elif filtro_data == 'prox_mes':
            queryset = queryset.filter(data__range=[timezone.now(), timezone.now()+ timezone.timedelta(days=30)])
        
        return queryset
    
class SolicitacaoDetail(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'lista/detail.html'

    def get_queryset(self): 
        queryset = self.model.objects.get(pk = self.kwargs['pk'])
        return queryset

# -- CRUD DE USUARIO -- 
# REGISTRO
def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        profile_form = PerfilForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            group = get_object_or_404(Group, name = "Aluno")
            user.groups.add(group)

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('inicio')
        
    else:
        form = UsuarioForm()
        profile_form = PerfilForm()

    context = {'form': form, 'profile_form': profile_form} 
    return render(request, 'sing-up.html',  context)

# UPDATE
class UsuarioUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = User
    fields = ['username', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-usuario')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Editar Usuário: {}".format(self.object)
        return context

    def get_object(self, query=None): 
        self.object = get_object_or_404(User, pk = self.kwargs['pk'])
        return self.object
    
# DELETE
class UsuarioDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = User
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-usuario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Excluir Usuário: {}".format(self.object)
        return context

# LIST
class UsuarioList(GroupRequiredMixin, ListView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'lista/usuario.html'
    content_object_name = 'object_list'

    paginate_by = 7

# EDIT PROFILE
class ProfileEdit(UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile.html'    
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Meu Perfil"
        return context

class PasswordEdit(views.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy('perfil')
