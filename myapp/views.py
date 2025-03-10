from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from works.models import Work
# Create your views here.


# def home(request):
#     return render(request,'./main/home.html')

class HomeView(TemplateView):
   template_name ='main/home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['posts'] = Post.objects.all()[:2]
      context['works'] = Work.objects.all()[:3]
      return context

       
