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
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView

from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import UsuarioForm, PerfilForm, ProfileEditForm, SolicitacaoForm, StatusForm, PostForm
from .models import *

from django.core.mail import send_mail
from django.conf import settings

# -- INDEX --
class IndexView(TemplateView):
    template_name = 'index.html'

class DashboardView(GroupRequiredMixin, ListView):
    group_required = [u'Aluno',u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitacaos'] = Solicitacao.objects.all()
        context['posts'] = Post.objects.all().order_by('-post')
        context['items'] = Item.objects.last()
        return context

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
                data['html_list'] = render_to_string("solicitacao/adm-list.html", {'object_list': solicitacoes})
            else:
                data['html_list'] = render_to_string("solicitacao/list.html", {'object_list': solicitacoes})
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
    
    return save_form(request, form, "solicitacao/create.html")

# SOLICITACAO UPDATE
def solicitacao_update(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, instance=solicitacao)
        
    else:
        form = SolicitacaoForm(instance=solicitacao)

    return save_form(request, form, "solicitacao/update.html")


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
            data['html_list'] = render_to_string("solicitacao/adm-list.html", {'object_list': solicitacoes})
        else:
            data['html_list'] = render_to_string("solicitacao/list.html", {'object_list': solicitacoes})  
    else:
        context = {'solicitacao': solicitacao}
        data['html_form'] = render_to_string('solicitacao/delete.html', context, request=request)
    
    return JsonResponse(data)

# SOLICITACAO STATUS UPDATE
def status_update(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=solicitacao)
        
    else:
        form = StatusForm(instance=solicitacao)

    return save_form(request, form, "solicitacao/status-update.html")

# -- CLASS BASED VIEWS -- 

# LIST
class SolicitacaoList(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'solicitacao/solicitacao.html'
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
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['solicitacaos'] = Solicitacao.objects.all()
        return context
    
class SolicitacaoDetail(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Solicitacao
    template_name = 'solicitacao/detail.html'

    def get_queryset(self): 
        queryset = Solicitacao.objects.all(pk = self.kwargs['pk'])
        return queryset

# -- CRUD ITEMS -- 
# CREATE
class ItemCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Item
    fields = ['name', 'description', 'image', 'sound']
    template_name = 'form.html'
    success_url = reverse_lazy('inventario')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Adicionar Novo Item ao Inventário".format(self.object)
        return context

# UPDATE 
class ItemUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Item
    fields = ['name', 'description', 'image', 'sound']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-item')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Editar Item".format(self.object)
        return context

    def get_object(self, query=None): 
        self.object = get_object_or_404(Item, pk = self.kwargs['pk'])
        return self.object
    

# DELETE
class ItemDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Item
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-item')
    
    def get_object(self, query=None): 
        self.object = get_object_or_404(Item, pk = self.kwargs['pk'])
        return self.object

# LIST
class ItemList(GroupRequiredMixin, ListView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Item
    template_name = 'lista/item.html'
    content_object_name = 'object_list'
    paginate_by = 7

# VIEW
class InventoryView(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Item
    template_name = 'lista/inventory.html'
    content_object_name = 'object_list'
    paginate_by = 3

# -- CRUD POST --
class PostCreate(GroupRequiredMixin, CreateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    form_class = PostForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-post')
    
    def form_valid(self, form):
        form.instance.author = get_object_or_404(Perfil, user = self.request.user)
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Nova Postagem".format(self.object)
        return context

# UPDATE 
class PostUpdate(GroupRequiredMixin, UpdateView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    form_class = PostForm
    template_name = 'form.html'
    success_url = reverse_lazy('listar-post')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Editar Postagem".format(self.object)
        return context

    def get_object(self, query=None): 
        self.object = get_object_or_404(Post, pk = self.kwargs['pk'])
        return self.object

# DELETE
class PostDelete(GroupRequiredMixin, DeleteView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-post')
    
    def get_object(self, query=None): 
        self.object = get_object_or_404(Post, pk = self.kwargs['pk'])
        return self.object

# LIST
class PostList(GroupRequiredMixin, ListView):
    group_required = [u'Admin']
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'lista/post.html'
    content_object_name = 'object_list'
    paginate_by = 7

# VIEW
class PostDetail(GroupRequiredMixin, DetailView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'lista/post-detail.html'

# LIST USER
class PostListClient(GroupRequiredMixin, ListView):
    group_required = [u'Aluno', u'Admin']
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'lista/post-list.html'
    content_object_name = 'object_list'
    paginate_by = 12

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-post')
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

            # send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER, [user.email], fail_silently= False)            

            my_recipient =  form.cleaned_data['email']

            send_mail(
                subject= 'MIM DE',
                message= 'POGGERS',
                recipient_list= [my_recipient],
                from_email= None,
                fail_silently= False

            )

            return redirect('inicio')
        
    else:
        form = UsuarioForm()
        profile_form = PerfilForm()

    context = {'form': form, 'profile_form': profile_form} 
    return render(request, 'registration/sing-up.html',  context)

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
    
    def get_object(self, query=None): 
        self.object = get_object_or_404(User, pk = self.kwargs['pk'])
        return self.object

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
