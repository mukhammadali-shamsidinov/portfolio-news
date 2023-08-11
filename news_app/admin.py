from django.contrib import admin
from .models import News,Category,Contact
# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published_time','status']
    prepopulated_fields = {"slug":("title",)}
    list_filter = ['published_time','status']
    search_fields = ['title','body']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Contact)