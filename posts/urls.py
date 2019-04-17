from django.urls import path
from . import views

app_name = 'posts' 

urlpatterns = [
    path('explore/', views.explore, name='explore'),
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    # path('<int:post_pk>/read/', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),
]