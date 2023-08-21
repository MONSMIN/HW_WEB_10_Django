from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<str:id_>', views.author, name='author'),
    path('tag/<str:tag_name>/', views.find_tag, name='find_tag'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote')
]
