from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# import models and serializers
from .serializers import *

from .models import *
from .forms import *
from payment import models as payment_models

# Create your views here.


def dashboard(req):
    return render(req, "dash-base.html")


def student_list_view(request):
    if request.method == "POST":
        form = student_detailsForm()
        form = student_detailsForm(request.POST)
        print(form)
        if form.is_valid():
            print(".....post on students ...")
            # print(form)
            form.save()
            return redirect("/", student_id=3)
    return render(
        request,
        "dash-student-list.html",
        {"api": "/students/api/student_class/?format=datatables"},
    )


def student_detailed_view(request, student_id):
    student_inst = student.objects.get(pk=student_id)
    form = student_detailsForm(instance=student_inst)
    context = {"student": student_inst, "form": form}

    if request.method == "POST":
        form = student_detailsForm()
        form = student_detailsForm(request.POST, instance=student_inst)

        if form.is_valid():
            form.save()
            context["student"] = student_inst
            return redirect("id_stu", student_id)

        return HttpResponse("<h1>wrong datas</h1>")

    return render(request, "dash-student-detailed-view.html", context)

    # form = student_detailsForm()
    # context = {"details": form}
    # return render(request, "student-detailes-form.html", context)


def due_view(request, student_id):

    student_instance = student.objects.get(id=student_id)
    due_instance = student_instance.due_set.all()[0]
    payment_info = due_instance.payment_info()

    prices = payment_models.price.objects.filter(stu_class=student_instance.stu_class)
    prices = prices[0].formed_data()

    grand_total = (
        prices["month_total"] * len(payment_info["due"])
        if not payment_info["due_session"]
        else (
            prices["month_total"] * (len(payment_info["due"]) - 1)
            + prices["session_total"]
        )
    )

    if grand_total >= payment_info["deposit"]:
        amount_payable = grand_total - payment_info["deposit"]
        new_deposit = 0
    else:
        new_deposit = payment_info["deposit"] - grand_total
        amount_payable = 0

    # amount_payable = (
    #     grand_total - payment_info["deposit"]
    #     if grand_total >= payment_info["deposit"]
    #     else 0
    # )

    due_info = {
        "due": payment_info["due"],
        "paid": payment_info["paid"],
        "due_session": payment_info["due_session"],
        "deposit": payment_info["deposit"],
        "month_total": prices["month_total"],
        "number_due_months": len(payment_info["due"])
        if payment_info["due_session"]
        else (len(payment_info["due"]) - 1),
        "month_items": prices["month_items"],
        "session_total": prices["session_total"],
        "session_items": prices["session_items"],
        "grand_total": grand_total,
        "amount_payable": amount_payable,
        "new_deposit": new_deposit,
    }

    return render(request, "dash-student-due.html", context=due_info)


class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all().order_by("name")
    serializer_class = student_detailsSerializer


class student_classViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    queryset = student.objects.all().order_by("name")
    serializer_class = student_classSerializer

