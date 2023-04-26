from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.homeView),
    path('/op/', views.outputView, name='output'),
    path('/<str:short_url>/', views.redirect_url, name='redirect_url')
]
