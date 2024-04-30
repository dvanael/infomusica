from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

from app.utils.ajax import AjaxListView, AjaxCreateView, AjaxUpdateView, AjaxDeleteView
from app.models import Post, Profile
from app.forms.post import PostForm 


class PostList(AjaxListView):
  model = Post
  template_name = 'post/list.html'
  partial_list = 'partials/post/list.html'

class PostCreate(CreateView):
  model = Post
  form_class = PostForm
  template_name = "post/create.html"
  success_url = reverse_lazy('post-list')

  def form_valid(self, form):
    form.instance.author = get_object_or_404(Profile, id=self.request.user.id)
    return super().form_valid(form)

class PostUpdate(UpdateView):
  model = Post
  form_class = PostForm
  template_name = "post/create.html"
  success_url = reverse_lazy('post-list')

class PostDelete(AjaxDeleteView):
  model = Post
  template_name = "partials/post/delete.html"
  success_url = reverse_lazy('post-list')