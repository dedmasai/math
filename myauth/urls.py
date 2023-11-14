from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import path

from .views import (
    AboutMeView,
    RegisterView,
)

app_name = "myauth"

urlpatterns = [

    path("register/", RegisterView.as_view(), name="register"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("login/", LoginView.as_view(template_name='myauth/login.html',
                                     redirect_authenticated_user=True), name="login"),

]