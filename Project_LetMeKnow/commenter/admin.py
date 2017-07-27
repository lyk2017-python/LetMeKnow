from django.contrib import admin
from .models import Comment, Product, Firm
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "title","creation_date","product"] #
    search_fields = ["title","product__name","message","product__firm__name"] # searc attributes
    list_display_links = ['title'] # Linked attributes
    list_filter = ["title","creation_date","product",]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    pass

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):

    pass