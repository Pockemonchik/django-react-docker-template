from auth import views
from django.urls import re_path


urlpatterns = [
    re_path('', views.AuthView.as_view()),
]