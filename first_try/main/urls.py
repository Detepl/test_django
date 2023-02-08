from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = "main"),
    path('test', views.test, name = "test"),
    path('add_user', views.add_user, name = "add_user")
]
