from django.contrib import admin
from django.urls import path, include
from .views import (ArticleListApiView, ArticleDetailApiView, ContactListApiView, ContactDetailApiView)

urlpatterns = [
    path('articles', ArticleListApiView.as_view()),
    path('articles/<int:pk>', ArticleDetailApiView.as_view()),
    path('contacts', ContactListApiView.as_view()),
    path('contacts/<int:pk>', ContactDetailApiView.as_view()),
]
