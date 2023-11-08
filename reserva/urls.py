from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('inicio/', DashboardView.as_view(), name = 'inicio'),
    
    #CRUD SOLICITÇÔES
    path('listar-solicitacao', SolicitacaoList.as_view(), name = 'listar-solicitacao'),
    path('detalhar-solicitacao/<int:pk>/', SolicitacaoDetail.as_view(), name = 'detalhar-solicitacao'),

    #AUTENTICAÇÂO
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('registrar/', register, name = 'registrar'),

    #CRUD USUARIO
    path('editar-usuario/<int:pk>/', UsuarioUpdate.as_view(), name = 'editar-usuario'),
    path('excluir-usuario/<int:pk>/', UsuarioDelete.as_view(), name = 'excluir-usuario'),
    path('listar-usuario/', UsuarioList.as_view(), name = 'listar-usuario'),

    #AJAX
    path('js/criar/', solicitacao_create, name = 'js-criar'),
    path('js/editar/<int:pk>/', solicitacao_update, name='js-editar'),
    path('js/excluir/<int:pk>/', solicitacao_delete, name='js-excluir'),
    path('js/editar-status/<int:pk>/', status_update, name='js-editar-status'),

    path('perfil/', ProfileEdit.as_view() , name = 'perfil'),
    path('password/', PasswordEdit.as_view(template_name = 'change-password.html'), name = 'mudar-senha'),
    
]