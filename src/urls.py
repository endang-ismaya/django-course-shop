from django.contrib import admin
from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name="v1")
api.register(CourseResource())
api.register(CategoryResource())

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
    path("api/", include(api.urls)),
]
