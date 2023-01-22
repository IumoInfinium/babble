from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('feed/', views.public_feed, name="feed"),
    path('register/', views.register, name="register"),
    path('join/',views.join,name="join"),
    path('create_room/', views.create_room),
    path('add/', views.add_post),
    path('check/', views.check_code)
]