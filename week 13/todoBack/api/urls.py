from django.urls import path, re_path
from api import views

urlpatterns = [
    path('task_lists/', views.task_list.as_view()),
    path('task_lists/<int:pk>/', views.task_list_detail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.task_list_tasks.as_view()),
    path('task_lists/<int:pk>/tasks/<int:pk1>/', views.task_list_tasks_detail.as_view())
]