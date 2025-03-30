from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from blog.models import Post
from works.models import Work
from .models import Contact
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from django.urls import reverse_lazy
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

class ContactView(SuccessMessageMixin, CreateView):
   model = Contact
   template_name = 'main/contact.html'
   form_class = ContactForm
   success_url = reverse_lazy('contact')
   success_message = "Your message has been sent succesfully!"

   def get_initial(self):
      initial =  super().get_initial()
      if self.request.user.is_authenticated:
         initial['name'] = self.request.user.first_name
      return initial