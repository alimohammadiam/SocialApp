from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'social'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
