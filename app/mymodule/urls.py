from mymodule import views
from django.urls import re_path
from django.urls import path



urlpatterns = [
    path('records/<int:pk>/', views.RecordDetailView.as_view()),
    path('records/', views.RecordListView.as_view()),
]

