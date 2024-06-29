from django.contrib.auth.views import LoginView
from django.urls import path


urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(template_name="users/login.html"), 
        name="login"
    )
]