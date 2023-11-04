from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('login/',views.loginpage, name="login"),
    path('register/',views.register, name="register"),
    path('adminpage/',views.adminpage, name="adminpage"),
    path('center/<int:cno>',views.center, name="center"),
    path('worker/<int:wno>',views.worker, name="worker"),
    path('workerreg',views.worker_reg, name="worker_reg"),
    path('user/<int:uno>',views.user, name="user"),
    ]
