from django.urls import path

from app.views.user import (
  UserList,
  UserUpdate,
  UserDelete,
  UserUpdatePermission,
)

urlpatterns = [
  path('', UserList.as_view(), name='user-list'),
  path('js/<int:pk>/update/', UserUpdate.as_view(), name='js-update-user'),
  path('<int:pk>/atualizar/permissao/', UserUpdatePermission.as_view(), name='update-user-permission'),
  path('js/<int:pk>/delete/', UserDelete.as_view(), name='js-delete-user'),
]