from django.urls import path
from . import views

urlpatterns = [
    path('',views.musician_list,name='musician_list'),
    path('musician/<int:pk>/', views.musician_detail, name='musician_detail'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('musician/new/', views.add_musician, name='add_musician'),
    path('album/new/', views.add_album, name='add_album'),
    path('musician/<int:pk>/delete/', views.delete_musician, name='delete_musician'),
    path('album/<int:pk>/delete/', views.delete_album, name='delete_album'),
]