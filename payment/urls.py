from django.urls import path
from . import views
from students import views as student_views

urlpatterns = [
    # Leave as empty string for base url
    # path("", views.user_search, name="user_search"),
    path("", student_views.student_list_view, name="user_search"),
    path("collectfee/<int:student_id>", views.collect_fee, name="collect_fee"),
]
