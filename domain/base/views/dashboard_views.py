from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from domain.boq.models import Project
from domain.catalog.models import CatalogItem


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "domain/dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.filter(created_by=self.request.user)
        context["project_count"] = projects.count()
        context["recent_projects"] = projects.order_by("-created_at")[:5]
        context["catalog_item_count"] = CatalogItem.objects.count()
        context["total_value"] = sum(p.grand_total for p in projects)
        return context