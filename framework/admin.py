from django.contrib import admin
from framework.models import Category

# Register your models here.
# Admin classes are necessary when trying to display a admin site with foreign keys or custom design


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    # fields = '__all__'


admin.site.register(Category, CategoryAdmin)
