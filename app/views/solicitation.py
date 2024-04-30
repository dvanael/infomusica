from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from app.utils.ajax import AjaxListView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from app.models import Solicitation, Profile
from app.forms.solicitation import SolicitacaoForm, StatusForm

#
class SolicitationList(LoginRequiredMixin, AjaxListView):
  model = Solicitation
  template_name = 'solicitation/list.html'
  partial_list = 'partials/solicitation/list.html'

class SolicitationCreate(AjaxCreateView):
  form_class = SolicitacaoForm
  template_name = 'partials/solicitation/create.html'
  success_url = reverse_lazy('solicitation-list')

  def form_valid(self, form):
      form.instance.profile = get_object_or_404(Profile, id=self.request.user.id)
      return super().form_valid(form)

class SolicitationUpdate(AjaxUpdateView):
  form_class = SolicitacaoForm
  template_name = 'partials/solicitation/update.html'
  success_url = reverse_lazy('solicitation-list')

class SolicitationDelete(AjaxDeleteView):
  model = Solicitation
  template_name = 'partials/solicitation/delete.html'
  success_url = reverse_lazy('solicitation-list')

class SolicitationStatusUpdate(AjaxUpdateView):
  form_class = StatusForm
  template_name = 'partials/solicitation/status-update.html'
  success_url = reverse_lazy('solicitation-list')