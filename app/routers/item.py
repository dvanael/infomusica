from django.urls import path

from app.views.item import (
  ItemList, 
  ItemCreate,
  ItemUpdate,
  ItemDelete,
)

urlpatterns = [
  path('', ItemList.as_view(), name='item-list'),
  path('cadastrar/', ItemCreate.as_view(), name='create-item'),
  path('<int:pk>/atualizar/', ItemUpdate.as_view(), name='update-item'),
  path('js/<int:pk>/deletar/', ItemDelete.as_view(), name='js-delete-item'),
]