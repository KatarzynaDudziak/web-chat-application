from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view, name='main'),
    path('delete/', views.delete_message, name='delete'),
    path('admin_view/', views.admin_view, name='admin_view'),
]