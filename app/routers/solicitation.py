from django.urls import path

from app.views.solicitation import (
  SolicitationList,
  SolicitationCreate,
  SolicitationUpdate,
  SolicitationStatusUpdate,
  SolicitationDelete,
)

urlpatterns = [
  path('', SolicitationList.as_view(), name='solicitation-list'),
  path('js/create/', SolicitationCreate.as_view(), name='js-create-solicitation'),
  path('js/<int:pk>/update/', SolicitationUpdate.as_view(), name='js-update-solicitation'),
  path('js/<int:pk>/status/update/', SolicitationStatusUpdate.as_view(), name='js-status-update-solicitation'),
  path('js/<int:pk>/delete/', SolicitationDelete.as_view(), name='js-delete-solicitation'),
]