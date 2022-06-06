from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('updateprofile/' ,views.update_user_information, name='updateProfile')
]