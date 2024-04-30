from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

from app.utils.ajax import AjaxListView, AjaxDeleteView
from app.models import Item
from app.forms.item import ItemForm 


class ItemList(AjaxListView):
  model = Item
  template_name = 'item/list.html'
  partial_list = 'partials/item/list.html'

class ItemCreate(CreateView):
  model = Item
  form_class = ItemForm
  template_name = "item/create.html"
  success_url = reverse_lazy('item-list')

class ItemUpdate(UpdateView):
  model = Item
  form_class = ItemForm
  template_name = "item/create.html"
  success_url = reverse_lazy('item-list')

class ItemDelete(AjaxDeleteView):
  model = Item
  template_name = "partials/item/delete.html"
  success_url = reverse_lazy('item-list')