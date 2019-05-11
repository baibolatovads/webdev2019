from django.urls import path, re_path
from api import views

# urlpatterns = [
#     # path('task_lists/', views.task_list.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('login/', views.UserLogin),
#     # path('task_lists/<int:pk>/', views.task_list_detail.as_view()),
#     # path('task_lists/<int:pk>/tasks/', views.task_list_tasks.as_view()),
#     # path('task_lists/<int:pk>/tasks/<int:pk1>/', views.task_list_tasks_detail.as_view())
# ]

urlpatterns = [
    path('task_lists/', views.task_list1.as_view()),
    path('task_lists/<int:pk>/', views.task_list_detail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.tasks.as_view()),
    # path('task_lists/<int:pk>/tasks/<int:ik>/',views.TaskDetail.as_view())
    path('users/',views.UserList.as_view()),
    path('users/<int:pk>/',views.UserDetails.as_view()),
    path('login/',views.UserLogin),
    path('logout/',views.UserLogout)
]
