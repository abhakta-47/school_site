from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notices/", views.notices_view, name="notices"),
    path("admission/", views.admission, name="admission"),
    path("admission/fillup/", views.fillup, name="form fillup"),
    path("courses/", views.courses, name="courses"),
    path("teacher/", views.teacher, name="teacher"),
    path("about/", views.about, name="about"),
    path("pricing/", views.pricing, name="pricing"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
]

