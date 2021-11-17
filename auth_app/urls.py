from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path("home/", TemplateView.as_view(template_name='auth_app/home.html'), name="home"),
    path("view/", TemplateView.as_view(template_name='auth_app/view.html'), name="view"),
    path("edit/", EditView.as_view(), name="edit"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/signup/", signup_page, name="signup")
]