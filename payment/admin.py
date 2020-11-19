from django.contrib import admin

# Register your models here.

# from .models import  order

# admin.site.register(due_list)
# admin.site.register(order)
# # admin.site.Register()

from .models import *


class transactionAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "billed_amount",
        "collected_amount",
        "trxn_no",
        "mode",
        "date_time",
    ]
    fields = [
        "student",
        "billed_amount",
        "collected_amount",
        "trxn_no",
        "date_time",
        "mode",
        "details",
    ]
    readonly_fields = [
        "student",
        "billed_amount",
        "collected_amount",
        "trxn_no",
        "date_time",
        "mode",
        "details",
    ]


class priceAdmin(admin.ModelAdmin):
    list_display = ["session", "stu_class", "motnthly_total"]

    def motnthly_total(self, obj):
        return obj.tuition_fee + obj.electric_fee + obj.tiffin_Charges


admin.site.register(price, priceAdmin)
admin.site.register(transaction, transactionAdmin)
