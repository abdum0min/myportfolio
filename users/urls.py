from django.urls import path
from .views import ProfileEditView, ProfileView, SignUpView, UserLoginView,UserPasswordChangeView, UserLogoutView

urlpatterns = [
    path('signup/',SignUpView.as_view(), name='sign_up'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',UserLogoutView, name='logout'),
    path('profile/edit/',ProfileEditView.as_view(), name='profile_edit'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('profile/changepassword/',UserPasswordChangeView.as_view(),name='change_password'),
]

