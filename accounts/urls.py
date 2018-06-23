
from django.urls import path
from . import views

urlpatterns = [
    path('signup.html/', views.signup, name = 'signup'),
    path('login.html/', views.login, name ='login'),
    path('logout.html/', views.logout, name ='logout'),

]
