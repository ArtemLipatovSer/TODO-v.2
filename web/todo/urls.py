from django.urls import path
from .views import (home, 
                    TaskList, 
                    TaskDetail, 
                    TaskCreate, 
                    TaskUpdate,
                    TaskDelete)

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(3600)(home), name='home'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete')
]