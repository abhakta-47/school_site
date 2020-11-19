from django.contrib import admin

# Register your models here.
from .models import *


class noticeAdmin(admin.ModelAdmin):
    list_display = ["date", "description", "file"]


admin.site.register(notice, noticeAdmin)
