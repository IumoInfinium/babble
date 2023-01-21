from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('feed/', views.public_feed, name="feed"),
    path('register/', views.register, name="register"),
    path('join/',views.join,name="join"),
    path('add/', views.add_post)
]