from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from domain.boq.forms.boq_forms import BillItemForm
from domain.boq.models import BillItem, Project
from domain.catalog.models import CatalogItem


class BillItemCreateView(LoginRequiredMixin, CreateView):
    model = BillItem
    form_class = BillItemForm
    template_name = "domain/boq/bill_item_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(
            Project, pk=kwargs["project_pk"], created_by=request.user
        )
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        catalog_item_id = self.request.GET.get("catalog_item")
        if catalog_item_id:
            catalog_item = get_object_or_404(CatalogItem, pk=catalog_item_id)
            initial.update({
                "catalog_item": catalog_item.pk,
                "trade": catalog_item.trade_id,
                "description": catalog_item.description_template,
                "unit": catalog_item.unit,
            })
        return initial

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context

    def get_success_url(self):
        return reverse("boq:project_detail", kwargs={"pk": self.project.pk})


class BillItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BillItem
    form_class = BillItemForm
    template_name = "domain/boq/bill_item_form.html"

    def get_queryset(self):
        return BillItem.objects.filter(project__created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.object.project
        return context

    def get_success_url(self):
        return reverse("boq:project_detail", kwargs={"pk": self.object.project_id})     

class BillItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BillItem
    template_name = "domain/boq/bill_item_confirm_delete.html"

    def get_queryset(self):
        return BillItem.objects.filter(project__created_by=self.request.user)

    def get_success_url(self):
        return reverse("boq:project_detail", kwargs={"pk": self.object.project_id})