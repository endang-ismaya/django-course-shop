from django.urls import path
from shop import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:course_id>", views.single_course, name="course"),
]
