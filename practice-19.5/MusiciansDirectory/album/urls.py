from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add/<int:id>/', views.add_album.as_view(), name='add_album'),
    path('edit/<int:id>/', views.edit_album.as_view(), name='edit_album'),

]
