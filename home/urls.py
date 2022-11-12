"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),

    path("tours/", views.tours, name='tours'),
    path('tours/<int:pk>/', views.tourDetail, name='tour-detail'),
    path("agents/", views.agents, name='agents'),
    path('agents/<int:pk>/', views.agentDetail, name='agent-detail'),

    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerUser, name='register'),
    # path("register/customuser", views.customuser, name='customuser'),

    path("create-tour/", views.addTour, name='create-tour'),
    # path("create-tour/<int:pk>/", views.updateTour, name='update-tour'),

]
