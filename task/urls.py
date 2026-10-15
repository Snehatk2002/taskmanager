from django.urls import path
from .views import task_list
from .views import add_task
from .views import update_task
from .views import delete_task

urlpatterns=[
    path('',task_list,name='task_list'),
    path('add/',add_task,name='add_task'),
    path('update/<int:id>/',update_task,name='update_task'),
    path('delete/<int:id>',delete_task,name='delete_task'),
]