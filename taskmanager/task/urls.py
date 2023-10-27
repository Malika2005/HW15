from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/create/', create_task, name='create_task'),
    path('task/<int:pk>/edit/', edit_task, name='edit_task'),
    path('task/<int:pk>/delete', delete_task, name='delete_task'),
    path('task/<int:pk>/complete', complete_task, name='complete_task'),
]