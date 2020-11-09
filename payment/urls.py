from django.urls import path
from . import views


urlpatterns = [
    # Leave as empty string for base url
    path("", views.user_search, name="user_search"),
    path("pay/", views.pay, name="Payment"),
    path("dues/", views.dues, name="due_list"),
    path(r"studentapi/", views.studentListAPIView.as_view(), name="student_list"),
]
