from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Work

# Create your views here.

class WorkListView(ListView):
    template_name = 'main/works.html'
    context_object_name = 'works'
    model = Work
    paginate_by = 5

class WorkDetailView(DetailView):
    template_name = 'main/works_detail.html'
    context_object_name ='work'
    model = Work