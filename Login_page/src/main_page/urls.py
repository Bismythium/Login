from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #/main_page/login/
    path('login/', views.LoginView.as_view(), name='login'),
    #/main_page/signup/
    path('signup/', views.SignupView.as_view(), name='signup'),
]