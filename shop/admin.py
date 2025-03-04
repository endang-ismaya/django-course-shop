from django.contrib import admin
from shop.models import Category, Course

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Manage Courses"


class CourseInline(admin.TabularInline):
    model = Course
    exclude = ["created_at"]
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    inlines = [CourseInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
