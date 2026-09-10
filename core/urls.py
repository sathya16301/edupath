from django.contrib import admin
from django.urls import path, re_path
from learning import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('subject/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('quiz/<int:subject_id>/', views.quiz_view, name='quiz'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Serve media files (thumbnails) in both development and production.
urlpatterns += [
    re_path(
        r'^media/(?P<path>.*)$',
        static_serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]