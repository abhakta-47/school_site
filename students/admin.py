from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path
import json
from django.http import HttpResponse
from django.shortcuts import render

# register your models here.

from .models import *
from payment import models as payment_models


def make_active(modelAdmin, request, queryset):
    queryset.update(status=True)
    make_active.short_description = "Make selected students status active"


def make_inactive(modelAdmin, request, queryset):
    queryset.update(status=False)
    make_active.short_description = "Make selected students in-active"


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "stu_class",
        "stu_sec",
        "stu_roll",
        "teaching_allowance",
        "status",
        "account_actions",
    ]
    fieldsets = (
        (
            "General Details",
            {
                "fields": (
                    "name",
                    "father_name",
                    "mother_name",
                    "guardian_name",
                    "dob",
                    "gender",
                    "reg_no",
                )
            },
        ),
        (
            "Academic Detils",
            {
                "fields": (
                    "stu_class",
                    "stu_sec",
                    "stu_roll",
                    "status",
                    "teaching_allowance",
                )
            },
        ),
        (
            "Address",
            {"fields": ("address1", "address2", "post", "pin", "dist", "state")},
        ),
        ("Contact", {"fields": ("primary_number", "whatsapp_number", "mail")}),
    )
    list_filter = ["stu_class", "stu_sec"]
    actions = [make_active, make_inactive]
    search_fields = ["name"]

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="">Collect Fee</a>'
            # reverse("admin:account-deposit", args=[obj.pk]),
            # reverse("admin:account-withdraw", args=[obj.pk]),
        )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "<int:student_id>/collect/",
                self.admin_site.admin_view(collect_view),
                name="due_view_admin",
            )
        ]
        return my_urls + urls


def collect_view(request, student_id):

    # # return render(request, "admin-due.html")
    # context = {}
    # student_inst = student.objects.get(pk=student_id)
    # due_inst = student_inst.due_set.all()[0]

    # payment_info = due_inst.payment_info()

    # prices = payment_models.price.objects.filter(stu_class=student_inst.stu_class)
    # prices = prices[0].formed_data()

    # context = {
    #     "paid": payment_info["paid"],
    #     "due": payment_info["due"],
    #     "prices": prices["month_items"],
    #     "total": prices["month_total"],
    #     "grand_total": prices["month_total"] * len(payment_info["due"]),
    # }
    # if request.method == "POST":
    #     post_data = request.POST
    #     print(post_data)
    #     new_deposit = (
    #         due_inst.deposit
    #         + int(post_data["amount"])
    #         - total * len(payment_info["due"])
    #     )
    #     return HttpResponse(new_deposit)

    # return render(request, "admin-due.html", context)

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

    amount_payable = grand_total - payment_info["deposit"]

    due_info = {
        "due": payment_info["due"],
        "paid": payment_info["paid"].items(),
        "due_session": payment_info["due_session"],
        "deposit": payment_info["deposit"],
        "month_total": prices["month_total"],
        "number_due_months": len(payment_info["due"]),
        "month_items": prices["month_items"],
        "session_total": prices["session_total"],
        "session_items": prices["session_items"],
        "grand_total": grand_total,
        "amount_payable": amount_payable,
    }
    print(due_info)

    if request.method == "POST":
        data = request.POST
        print(data["amount"])
        transaction_instance = payment_models.transaction.objects.create(
            student_id=student_id,
            billed_amount=grand_total,
            collected_amount=int(data["amount"]),
            trxn_no="xxxxxxxx",
            details=due_info.__str__(),
        )
        print(transaction_instance)
        return HttpResponse("hhh")

    return render(request, "admin-due.html", context=due_info)


@admin.register(due)
class student_dueAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "session_yr",
        "session",
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]


# admin.site.register(student_details, student_detailsAdmin)
# admin.site.register(student_class, student_classAdmin)
# admin.site.register(student_address)
# admin.site.register(student_contact, student_contactAdmin)

# admin.site.register(student, studentAdmin)
# admin.site.register(student, student_contactAdmin)
