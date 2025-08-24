# notes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('notes/create/', views.note_create, name='note_create'),
    path('notes/<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path("notes/<int:note_id>/delete/", views.note_delete, name="note_delete"),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),

    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/', views.users_list, name='users_list'),

]
