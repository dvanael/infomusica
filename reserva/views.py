from django.forms.models import BaseModelForm
from django.shortcuts import render , redirect
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import UsuarioForm, PerfilForm
from .models import Solicitacao, Perfil

#AJAX IMPORT
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import EventoForm
from django.contrib.auth import authenticate, login

# FUNÇÕES DO AJAX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string

def save_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            solicitacoes = Solicitacao.objects.all().order_by('-post')
            paginator = Paginator(solicitacoes, 7) # Define o número de itens por página
            page = request.GET.get('page')

            try:
                solicitacoes = paginator.page(page)
            except PageNotAnInteger:
                solicitacoes = paginator.page(1)
            except EmptyPage:
                solicitacoes = paginator.page(paginator.num_pages)

            data['html_list'] = render_to_string("lista/parcial-list.html", {'object_list': solicitacoes})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        form.instance.usuario = Perfil.objects.get(user=request.user)
        form.instance.post = timezone.now()

    else:
        form = EventoForm()
        form.instance.usuario = Perfil.objects.get(user=request.user)
        form.instance.post = timezone.now()
    
    return save_form(request, form, "lista/parcial-create.html")

def evento_update(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=solicitacao)
        form.instance.usuario = Perfil.objects.get(user=request.user)
        form.instance.post = timezone.now()
        
    else:
        form = EventoForm(instance=solicitacao)
        form.instance.usuario = Perfil.objects.get(user=request.user)
        form.instance.post = timezone.now()

    return save_form(request, form, "lista/parcial-update.html")

def evento_delete(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    data = dict()

    if request.method == 'POST':
        solicitacao.delete()
        data['form_is_valid'] = True
        solicitacoes = Solicitacao.objects.all().order_by('-post')
        paginator = Paginator(solicitacoes, 7)  # Define o número de itens por página
        page = request.GET.get('page')

        try:
            solicitacoes = paginator.page(page)
        except PageNotAnInteger:
            solicitacoes = paginator.page(1)
        except EmptyPage:
            solicitacoes = paginator.page(paginator.num_pages)

        data['html_list'] = render_to_string('lista/parcial-list.html', {'object_list': solicitacoes})
    else:
        context = {'solicitacao': solicitacao}
        data['html_form'] = render_to_string('lista/parcial-delete.html', context, request=request)
    
    return JsonResponse(data)

# INDEX
class IndexView(TemplateView):
    template_name = 'index.html'


# -- CRUD DE USUARIO
def resgister(request):
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

class UsuarioUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = User
    fields = ['username', 'email']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-usuario')

    def get_object(self, query=None): 
        self.object = get_object_or_404(User, pk = self.kwargs['pk'])
        return self.object
    
class UsuarioDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = User
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-usuario')

class UsuarioList(GroupRequiredMixin, ListView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'lista/usuario.html'
    content_object_name = 'object_list'
    

# -- CRUD DE SOLICITÇÕES
# CREATE
class SolicitacaoCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    fields = ['justificativa', 'data', 'hora']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-solicitacao')

    def form_valid(self, form):
        form.instance.usuario = Perfil.objects.get(user=self.request.user)
        url = super().form_valid(form)
        return url 

# UPDATE
class SolicitacaoUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    fields = ['justificativa', 'data', 'hora']
    template_name = 'form.html'
    success_url =  reverse_lazy('listar-solicitacao')

    def form_valid(self, form):
        form.instance.post = timezone.now()
        return super().form_valid(form)

    def get_object(self, query=None):
        if self.request.user.groups.filter(name = u'Admin'):
            self.object = get_object_or_404(Solicitacao, pk = self.kwargs['pk'])
            return self.object
        else:
            self.object = get_object_or_404(Solicitacao, pk = self.kwargs['pk'], usuario = self.request.user)
            return self.object

# DELETE 
class SolicitacaoDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-solicitacao')

    def get_object(self, query=None):
        if self.request.user.groups.filter(name = u'Admin'):
            self.object = get_object_or_404(Solicitacao, pk = self.kwargs['pk'])
            return self.object
        else:
            self.object = get_object_or_404(Solicitacao, pk = self.kwargs['pk'], usuario = self.request.user)
            return self.object
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
            self.object_list = Solicitacao.objects.filter().order_by('-post')

        else:
            self.object_list = Solicitacao.objects.filter(usuario = Perfil.objects.get(user = self.request.user)).order_by('-post')
            
        filtro_data = self.request.GET.get('filtro_data', None)

        if filtro_data == 'ultima_semana':
            self.object_list = self.object_list.filter(data__gte=timezone.now() - timezone.timedelta(days=7))

        elif filtro_data == 'ultimo_mes':
            self.object_list = self.object_list.filter(data__gte=timezone.now() - timezone.timedelta(days=30))


        return self.object_list
    

# GERENCIAMENTO DE SOLICITAÇÕES
class StatusUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    fields = ['status', 'justificativa']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-solicitacao')

    def form_valid(self, form):
        form.instance.post = timezone.now()
        return super().form_valid(form)

    def get_object(self, query=None):
        self.object = get_object_or_404(Solicitacao, pk = self.kwargs['pk'])
        return self.object
       

