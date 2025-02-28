from django.http import HttpResponse
from shop.models import Course


def index(request):
    courses = Course.objects.all()
    return HttpResponse(courses)
