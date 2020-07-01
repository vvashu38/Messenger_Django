from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name="register"),
    path('loggedin/<str:friendusername>', views.loggedin, name='loggedin'),
    path('loggedin', views.loggedin, name='intitalloggedin'),
    path('logout', views.logout, name='logout'),
    path('message', views.message , name= 'message'),
]