from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('post/<str:pk>/', views.view_post, name='post'),
    path('profile/', views.profile_page, name='profile'),
]
