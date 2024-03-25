from django.contrib import admin
from django.urls import path

from apps.user.api import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("admin/", admin.site.urls),
]
