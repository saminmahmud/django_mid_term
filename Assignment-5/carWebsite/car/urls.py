from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login.as_view(), name='user_login'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
    path('edit_profile/<int:id>/', views.edit_profile.as_view(), name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
    path('buy/<int:id>/', views.buy, name='buy'),
]

