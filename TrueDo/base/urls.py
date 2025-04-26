from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
    path('<int:pk>/',TaskDetail.as_view(),name='task'),  # pk = primary key
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-edit/<int:pk>/',TaskUpdate.as_view(),name='task-edit'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]