from django.shortcuts import render, redirect
from django.http import HttpResponse

# for captcha
import requests

# for pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# importing my models
from .models import notice

# Create your views here.


def home(request):
    print(request.path)
    return render(request, "index.html")

    # return HttpResponse("<h1>hei there</he>")


def notices_view(request):
    notice_list = notice.objects.all()
    # print(notice_list)
    page = request.GET.get("page", 1)
    paginator = Paginator(notice_list, 10)
    try:
        notices_ = paginator.page(page)
    except PageNotAnInteger:
        notices_ = paginator.page(1)
    except EmptyPage:
        notices_ = paginator.page(paginator.num_pages)

    return render(request, "notices.html", {"notices": notices_})


def admission(request):
    return render(request, "admission.html")


def fillup(request):
    if request.method != "POST":
        return redirect(admission)
    else:
        values = {
            "secret": "6LexS98ZAAAAAG6FI01ob329q9bzUtcsAcQNt2q_",
            "response": request.POST.get("g-recaptcha-response"),
        }
        resp = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", data=values
        )
        result = resp.json()
        """ End reCAPTCHA validation """

        if result["success"]:
            return HttpResponse("<h1>captcha successful</h1>")
        else:
            return HttpResponse("<h1>captcha unsuccessful</h1>")

