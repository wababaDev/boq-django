from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from domain.catalog.models.catalog import Trade, CatalogItem


class CatalogItemListView(LoginRequiredMixin, ListView):
    model = CatalogItem
    template_name = "domain/catalog/item_list.html"
    context_object_name = "items"
    paginate_by = 50

    def get_queryset(self):
        qs = CatalogItem.objects.select_related("trade")
        q = self.request.GET.get("q")
        trade_id = self.request.GET.get("trade")
        if q:
            qs = qs.filter(description_template__icontains=q)
        if trade_id:
            qs = qs.filter(trade_id=trade_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trades"] = Trade.objects.all()
        context["query"] = self.request.GET.get("q", "")
        context["selected_trade"] = self.request.GET.get("trade", "")
        return context