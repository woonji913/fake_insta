from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('password/', views.password_change, name='password_change'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]