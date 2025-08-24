# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"  # <<< ВАЖНО

urlpatterns = [
    # регистрация
    path("auth/register/", views.register, name="register"),

    # логин/логаут
    path(
        "auth/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    # Вариант 1: логаут-редирект (можно кликать обычной ссылкой)
    path(
        "auth/logout/",
        auth_views.LogoutView.as_view(next_page="users:login"),
        name="logout",
    ),

    # восстановление пароля
    path(
        "auth/password_reset/",
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "auth/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "auth/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "auth/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
        name="password_reset_complete",
    ),
]
