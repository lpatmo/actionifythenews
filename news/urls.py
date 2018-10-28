from django.urls import path
from news import views


urlpatterns = [
    path('', views.index, name='home'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]
