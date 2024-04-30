from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#index

@login_required
def index(request):
  template_name = 'index.html'
  return render(request, template_name,)