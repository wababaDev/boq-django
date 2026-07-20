from django.contrib import admin

from domain.catalog.models import Trade, CatalogItem


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("name", "bill_number", "order", "item_count")
    ordering = ("order",)

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = "Items"


@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ("item_code", "trade", "short_description", "unit")
    list_filter = ("trade",)
    search_fields = ("description_template", "item_code")
    ordering = ("trade__order", "item_code")

    def short_description(self, obj):
        return obj.description_template[:80]
    short_description.short_description = "Description"