from django.urls import path
from  .views import WorkDetailView,WorkListView

urlpatterns = [
    path('works/',WorkListView.as_view(),name='works'),
    path('works/<int:pk>',WorkDetailView.as_view(),name='work_detail'),
]
