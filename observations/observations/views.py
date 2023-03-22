from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registration/login.html"
    success_url = reverse_lazy("/")  # Replace "home" with the name of your homepage URL
