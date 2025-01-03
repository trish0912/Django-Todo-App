from django.urls import path
from . import views
from .views import ItemCreate, TodoListView, tododeleteview, todoupdateview
'''
urlpatterns = [
    path('', TodoListView.as_view(), name='task-list'),
    path('new/', ItemCreate.as_view(), name='task-create'),
    path('<int:pk>/delete/', tododeleteview.as_view(), name='task-delete'),  
    path('<int:pk>/update/', todoupdateview.as_view(), name='task-update'),
    path('about/', views.about, name='task-home'),
 
]'''

urlpatterns = [
    path('', views.about, name='task-home'),
    path('about/', TodoListView.as_view(), name='task-list'),
    path('new/', ItemCreate.as_view(), name='task-create'),
    path('<int:pk>/delete/', tododeleteview.as_view(), name='task-delete'),  
    path('<int:pk>/update/', todoupdateview.as_view(), name='task-update'),
 
]