from django.urls import path

from app.views.post import (
  PostList, 
  PostCreate,
  PostUpdate,
  PostDelete,
)

urlpatterns = [
  path('', PostList.as_view(), name='post-list'),
  path('cadastrar/', PostCreate.as_view(), name='create-post'),
  path('<int:pk>/atualizar/', PostUpdate.as_view(), name='update-post'),
  path('js/<int:pk>/deletar/', PostDelete.as_view(), name='js-delete-post'),
]