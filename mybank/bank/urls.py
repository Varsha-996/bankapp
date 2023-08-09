from . import views
from django.urls import path
from django.urls import path


urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.loginn,name='login'),
    path('register/',views.register,name='register'),
    path('new/',views.new,name='new'),
    path('index/',views.index,name='index'),





]
