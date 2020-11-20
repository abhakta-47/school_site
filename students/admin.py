from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path
import json, datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

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
            '<a href="'
            + str(obj.id)
            + '/collect" class="btn btn-primary">Collect Fee</a>'
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


def get_due_info(student_id):
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
    # print(due_info)
    return due_info


def collect_view(request, student_id):

    due_info = get_due_info(student_id)

    if request.method == "POST":
        data = request.POST
        trx_no = str(datetime.datetime.now())
        new_deposit = (
            due_info["new_deposit"] + int(data["amount"]) - due_info["amount_payable"]
        )
        transaction_instance = payment_models.transaction.objects.create(
            student_id=student_id,
            billed_amount=due_info["amount_payable"],
            collected_amount=int(data["amount"]),
            trxn_no=trx_no,
            details={
                "due": due_info["due"],
                "month_items": due_info["month_items"],
                "session_items": due_info["session_items"],
                "grand_total": due_info["grand_total"],
                "deposit": due_info["deposit"],
                "amount_payable": due_info["amount_payable"],
                "collected_amount": int(data["amount"]),
                "new_deposit": new_deposit,
            },
        )
        student_instance = student.objects.get(id=student_id)
        due_instance = student_instance.due_set.all()[0]
        for month in due_info["due"]:
            setattr(due_instance, month, trx_no)

        setattr(due_instance, "deposit", new_deposit)
        due_instance.save()

        return redirect(
            "/admin/payment/transaction/" + str(transaction_instance.id) + "/change/"
        )

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
