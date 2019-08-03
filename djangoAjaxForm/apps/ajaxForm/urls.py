from django.urls import path

from . import views

app_name = 'ajaxform'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.Create.as_view(), name='create'),
    path('list/', views.List.as_view(), name='list'),
    path('detail/<int:id>', views.Detail.as_view(), name='detail'),
]