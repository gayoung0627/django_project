from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Product, Category, Tag, Manufacturer, Comment
# Register your models here.

admin.site.register(Product, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Manufacturer, ManufacturerAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Tag, TagAdmin)
