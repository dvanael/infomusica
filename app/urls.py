from django.urls import path, include

from .views.index import index
from .views.user import register, login_view, logout_view

from .routers import solicitation, user, post

# Crie suas urls aqui
urlpatterns = [
  path('', index, name='index'),

  path('cadastro/', register, name='register'),
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),

  path('solicitacoes/', include(solicitation)),
  path('usuarios/', include(user)),
  path('postagens/', include(post)),
]