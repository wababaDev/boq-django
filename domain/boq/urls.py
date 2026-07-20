from django.urls import path

from domain.boq.views.bill_items_views import (
    BillItemCreateView,
    BillItemDeleteView,
    BillItemUpdateView,
)
from domain.boq.views.pdf_export_views import ProjectExportPDFView
from domain.boq.views.project_views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
)

app_name = "boq"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("new/", ProjectCreateView.as_view(), name="project_create"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path(
        "<int:project_pk>/items/add/",
        BillItemCreateView.as_view(),
        name="bill_item_add",
    ),
    path("items/<int:pk>/edit/", BillItemUpdateView.as_view(), name="bill_item_edit"),
    path(
        "items/<int:pk>/delete/", BillItemDeleteView.as_view(), name="bill_item_delete"
    ),
    path("<int:pk>/export/", ProjectExportPDFView.as_view(), name="project_export_pdf"),
]
