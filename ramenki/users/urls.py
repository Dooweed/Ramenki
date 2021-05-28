from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView

app_name = "auth"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Profile
    path("profile/", views.profile_view, name="profile"),
    path("profile-edit/", views.profile_edit_view, name="profile-edit"),

    # Password reset
    path("password-reset/", PasswordResetView.as_view(template_name="auth/password_reset/password_reset.html", success_url="/password-reset-done/",
                                                      email_template_name="auth/password_reset/password_reset_email.html", ), name="password-reset"),
    path("password-reset-done/", PasswordResetDoneView.as_view(template_name="auth/password_reset/password_reset_done.html"), name="password-reset-done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="auth/password_reset/password_reset_confirm.html",
                                                                     post_reset_login_backend='django.contrib.auth.backends.ModelBackend', post_reset_login=True,
                                                                     success_url="/profile/"), name="password-reset-confirm"),

    # Password change
    path("password-change/", PasswordChangeView.as_view(template_name="auth/password_change/password_change.html",
                                                        success_url="/password-change-done/"), name="password-change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(template_name="auth/password_change/password_change_done.html"), name="password-change-done"),

    # Password set
    path("password-set/", views.set_password_view, name="password-set"),
]
