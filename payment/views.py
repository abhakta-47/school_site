from django.shortcuts import render

from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView
from .serializers import studentSerializer

from .models import student

# Create your views here.


def pay(req):
    return render(req, "pay.html")


def user_search(req):
    return render(req, "userSearch.html")


def dues(request):
    if request.method == "POST":
        id_ = request.POST["id"]
        dob = request.POST["date"]

        if not id_.isnumeric():
            print("not int convertable")
            return render(request, "userSearch.html")

        id_ = int(id_)

        if student.objects.filter(id=id_).count() != 1:
            print(id_)
            print(type(id_))
            print(" student not found ")
            return render(request, "userSearch.html")

        this_student = student.objects.get(id=id_)

        if not str(this_student.date_of_birth) == dob:
            return render(request, "userSearch.html")

        return render(
            request, "dues.html", {"date": dob, "name": id_, "student": this_student}
        )
    else:
        return render(request, "userSearch.html")


class studentListAPIView(ListAPIView):
    search_fields = ["first_name", "last_name"]
    filter_backends = (filters.SearchFilter,)
    queryset = student.objects.all()
    serializer_class = studentSerializer
