from django.shortcuts import render
from django.http import HttpResponse
import json

# rest imports
from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView

# my models and forms import
from students import forms as student_form, models as student_model

# Create your views here.


def pay(req):
    return render(req, "pay.html")


def user_search(req):
    return render(req, "userSearch.html")


def collect_fee(request, student_id):
    # context = {}
    # if request.method == "POST":
    #     print(request.POST)
    #     return HttpResponse(request.POST)
    # student = student_model.student_details.objects.get(pk=student_id)
    # student_due = (student.due_set.all())[0]
    # # print(type(student_due.due))
    # # print(student_due.due)
    # # context = {"student_due": json.dumps(student_due.due)}
    # context = {"student_due": (student_due.due)}
    # return render(request, "collect-fee.html", context)
    return HttpResponse("<h1>integration with payment gateway in progress</h1>")


# def dues(request):
# if request.method == "POST":
#     id_ = request.POST["id"]
#     dob = request.POST["date"]

#     if not id_.isnumeric():
#         print("not int convertable")
#         return render(request, "userSearch.html")

#     id_ = int(id_)

#     if student.objects.filter(id=id_).count() != 1:
#         print(id_)
#         print(type(id_))
#         print(" student not found ")
#         return render(request, "userSearch.html")

#     this_student = student.objects.get(id=id_)

#     if not str(this_student.date_of_birth) == dob:
#         return render(request, "userSearch.html")

#     return render(
#         request, "dues.html", {"date": dob, "name": id_, "student": this_student}
#     )
# else:
# return render(request, "userSearch.html")
