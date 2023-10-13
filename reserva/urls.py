from django.urls import path
from .views import IndexView, SolicitacaoCreate, SolicitacaoDelete, SolicitacaoUpdate, SolicitacaoList, StatusUpdate
from .views import resgister, UsuarioDelete, UsuarioList, UsuarioUpdate
from .views import evento_create, evento_update, evento_delete
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
    path('registrar/', resgister, name = 'registrar'),

    #CRUD USUARIO
    path('editar-usuario/<int:pk>/', UsuarioUpdate.as_view(), name = 'editar-usuario'),
    path('excluir-usuario/<int:pk>/', UsuarioDelete.as_view(), name = 'excluir-usuario'),
    path('listar-usuario/', UsuarioList.as_view(), name = 'listar-usuario'),

    #AJAX
    path('js/criar/', evento_create, name = 'js-criar'),
    path('js/editar/<int:pk>/', evento_update, name='js-editar'),
    path('js/excluir/<int:pk>/', evento_delete, name='js-excluir'),


    #ADMIN
    path('status-solicitacao/<int:pk>', StatusUpdate.as_view(), name = 'status-solicitacao'),
]