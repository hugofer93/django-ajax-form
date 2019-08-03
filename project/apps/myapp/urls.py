from django.urls import path

from project.apps.myapp.views import Create, Detail, Index, List

app_name = 'myapp'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create/', Create.as_view(), name='create'),
    path('list/', List.as_view(), name='list'),
    path('detail/<int:id>/', Detail.as_view(), name='detail'),
]