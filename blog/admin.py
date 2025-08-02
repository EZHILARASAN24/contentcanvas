from django.contrib import admin
from blog.models import Category,Blog

class CategoryAdmin(admin.ModelAdmin):
    list_display=['cname','created_at','updated_at']

class BlogAdmin(admin.ModelAdmin):
    search_fields=['id','category__cname','author__username','created_at','updated_at','trending','status']
    prepopulated_fields={'slug':('title',)}
    list_display=['title','category','author','status','trending','created_at','updated_at']
    list_editable=['trending']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin) 