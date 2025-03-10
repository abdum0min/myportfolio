from django.urls import path
from .views import PostDetailView,PostListView



urlpatterns = [
    path('',PostListView.as_view(),name='blog'),
    path('blog/<int:pk>',PostDetailView.as_view(),name='blog_detail')
]
