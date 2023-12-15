from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('add/<int:id>/', views.add_musician.as_view(), name='add_musician'),
    path('edit/<int:id>/', views.edit_musician.as_view() , name='edit_musician'),
    path('delete/<int:id>/', views.delete_musician.as_view() , name='delete_musician'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login.as_view(), name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
]
