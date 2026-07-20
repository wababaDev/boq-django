from django.urls import path

from domain.catalog.views.catalog_views import CatalogItemListView



app_name = "catalog"

urlpatterns = [
path("", CatalogItemListView.as_view(), name="item_list"),
]
