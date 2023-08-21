from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryname", 'cat_image')
    prepopulated_fields = {"slug":('categoryname',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)