"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('pages/', views.pages, name='pages'),
    path('pages/<int:page_id>/', views.page, name='page'),
    path('new_page/', views.new_page, name='new_page'),
    path('new_post/<int:page_id>/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]