from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('register/', views.register, name='register'),
]