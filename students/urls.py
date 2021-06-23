from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"student_details", studentViewSet)
# router.register(r"student_details", student_detailsViewSet)
router.register(r"student_class", student_classViewSet)
# router.register(r"student_address", student_addressViewSet)
# router.register(r"student_contact", student_contactViewSet)

urlpatterns = [
    path("", student_list_view),
    path("<int:student_id>/", student_detailed_view, name="id_stu"),
    path("api/", include(router.urls)),
    path("<int:student_id>/due/", due_view),
]
