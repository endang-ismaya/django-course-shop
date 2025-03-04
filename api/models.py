from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from api.authentication import CustomApiKeyAuthentication
from tastypie.exceptions import BadRequest


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = "categories"
        allowed_methods = ["get"]


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = "courses"
        allowed_methods = ["get", "delete", "post"]
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()
        always_return_data = True

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return super().hydrate(bundle)

    def dehydrate(self, bundle):
        bundle.data["category_id"] = bundle.obj.category.id
        bundle.data["category"] = bundle.obj.category
        return super().dehydrate(bundle)

    def dehydrate_title(self, bundle):
        return bundle.data["title"].upper()

    def delete_list(self, request=None, **kwargs):
        """
        Prevent deletion of all courses.
        """
        raise BadRequest("Deleting all courses is not allowed.")
