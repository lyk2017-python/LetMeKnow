from django.contrib import admin
from .models import Comment, Product, Firm


class ProductFirmInline(admin.TabularInline):  #admin sayfasında firmaları listeleyip herhangi birini seçtikten sonra,
    model = Product#seçilen firmanın ürünlerini listemeyi sağladık.
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "creation_date", "product", "rate"] #
    search_fields = ["title", "product__name", "message", "product__firm__name"] # searc attributes
    list_display_links = ['title']  # Linked attributes
    list_filter = ["title", "creation_date", "product"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "firm_name"]  #
    search_fields = ["name"]  # search attributes
    list_display_links = ['name']  # Linked attributes
    list_filter = ["name", "firm", ]

    def firm_name(self, object):
        return object.firm.name




@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ["id", "name",]  #
    search_fields = ["name"]  # searc attributes
    list_display_links = ['name']  # Linked attributes
    list_filter = ["name"]
    inlines = [ProductFirmInline]

