from django.shortcuts import render,redirect
from .models import CustomUser
from django.views.generic.edit import UpdateView
from .forms import UserUpdateForm, SignUpForm, LoginForm
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login , logout
from django.contrib import messages

# Create your views here.

# registration views
class SignUpView(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')
    def get_success_url(self):
        return reverse_lazy('home')
    
# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('login')

def UserLogoutView(request):
    logout(request)
    return redirect('login')


# profile views
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    context_object_name = 'user_profile'
    template_name = 'main/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self,queryset=None):
        return self.request.user
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'main/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset = None):
        return self.request.user
    
# password change
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form) 
        messages.success(self.request, "Your password was successfully changed!")
        return response  
