from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('post/<str:pk>/', views.view_post, name='post'),
    path('deletePost/<str:pk>/', views.delete_post, name='delete'),
    path('profile/', views.profile_page, name='profile'),
    path('addpost/', views.add_post, name='addpost'),
    path('about/', views.about_page, name='about'),
    path('addpostdb/', views.add_post_db, name='addposttodb'),
]

