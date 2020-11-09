from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notices/", views.notices_view, name="notices"),
    path("admission/", views.admission, name="admission"),
    path("admission/fillup/", views.fillup, name="form fillup"),
]

