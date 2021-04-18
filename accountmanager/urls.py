"""accountmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import SigninView, SignUpView, DashboardView, signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SigninView.as_view(), name='login'),
    path('login/', SigninView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('income/', include('income.urls')),
    path('expenses/', include('expenses.urls')),
    path('logout/', signout, name='signout')
]
