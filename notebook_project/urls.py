from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

app_name = "users"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notes.urls")),
    path("", include("users.urls")),  # наши /auth/login, /auth/logout, ...
    path("accounts/profile/", lambda r: redirect("index")),  # чтобы не падать на /accounts/profile/
]