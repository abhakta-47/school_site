from django.contrib import admin

# Register your models here.

from .models import student, due_list, price_list, order

admin.site.register(student)
admin.site.register(due_list)
admin.site.register(price_list)
admin.site.register(order)
# admin.site.Register()
