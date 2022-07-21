from django.contrib import admin
from applications.product.models import Category, Product, Image, Like, Rating

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Rating)



class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]


admin.site.register(Product, ProductAdmin)


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
