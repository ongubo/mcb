from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # User Views
    path('', views.home, name="home"),
    path('apply/', views.register_user, name="register"),
    path('stats/', views.stats, name="stats"),

    # Authentivcation views
    path('login/', auth_views.login,
         {'template_name': 'loan/auth/login.html'}, name="login"),
    path('logout/', auth_views.logout, {'next_page': '/'}, name="logout"),

    # Dashboard Views
    path('dashboard/', views.dashboard, name="dashboard-home"),
    path('users/', views.users, name="dashboard-users"),
    path('loans/', views.loans, name="dashboard-loans"),
    path('loan/apply/', views.apply_loan, name="dashboard-loan-apply"),
    path('loan/delete/', views.delete_loan, name="dashboard-loan-delete"),
]
