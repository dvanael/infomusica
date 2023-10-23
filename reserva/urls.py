from django.urls import path
from .views import IndexView, SolicitacaoCreate, SolicitacaoDelete, SolicitacaoUpdate, SolicitacaoList, StatusUpdate
from .views import register, UsuarioDelete, UsuarioList, UsuarioUpdate
from .views import solicitacao_create, solicitacao_update, solicitacao_delete, status_update
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inicio/', IndexView.as_view(), name = 'inicio'),
    
    #CRUD SOLICITÇÔES
    path('criar-solicitacao/', SolicitacaoCreate.as_view(), name = 'criar-solicitacao'),
    path('editar-solicitacao/<int:pk>/', SolicitacaoUpdate.as_view(), name = 'editar-solicitacao'),
    path('excluir-solicitacao/<int:pk>/', SolicitacaoDelete.as_view(), name = 'excluir-solicitacao'),
    path('listar-solicitacao', SolicitacaoList.as_view(), name = 'listar-solicitacao'),

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

    #ADMIN
    path('status-solicitacao/<int:pk>', StatusUpdate.as_view(), name = 'status-solicitacao'),
]