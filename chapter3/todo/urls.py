from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'), #여기서 지정한 이름으로 html 태그함수에서 사용
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'),
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done, name='todo_done'),
]