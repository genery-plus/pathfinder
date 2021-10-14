from django.urls import path
from . import views
urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
]

#login - вход
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^login$', pagelogin, name='login'),
]
