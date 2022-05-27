from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view, name='main'),
    path('delete/', views.delete_message, name='delete'),
    path('history/', views.history, name='history'),
    path('search-results/', views.search_message, name='search-results'),

]
