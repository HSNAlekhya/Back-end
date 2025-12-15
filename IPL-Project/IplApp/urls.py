from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('register-franchise/', views.register_franchise, name='register_franchise'),
    path('franchise-list/', views.franchise_list, name='franchise_list'),
    path('franchise-details/<int:id>/', views.franchise_details, name='franchise_details'),
    path('update-franchise/<int:id>/', views.update_franchise, name='update_franchise'),
    path('delete-franchise/<int:id>/', views.delete_franchise, name='delete_franchise'),
    path('register-player/', views.register_player, name='register_player'),
    path('player-list/', views.player_list, name='player_list'),
    path('register-stadium/', views.register_stadium, name='register_stadium'),
    path('stadium-list/', views.stadium_list, name='stadium_list'),
    path('register-user/', views.register_user, name='register_user'),
    path('login-user/', views.login_user, name='login_user'),
]