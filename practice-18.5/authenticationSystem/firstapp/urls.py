
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('passChange/', views.passChange, name='passChange'),
    path('passChange2/', views.passChange2, name='passChange2'),

]
