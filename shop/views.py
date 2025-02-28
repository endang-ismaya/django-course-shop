from django.shortcuts import render
from shop.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, "shop/courses.html", context={"courses": courses})
