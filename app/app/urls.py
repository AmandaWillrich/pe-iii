from django.contrib import admin
from django.urls import path, include
from users.views import RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('cadastrar/', RegisterView.as_view(), name='register'),
    path('entrar/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
