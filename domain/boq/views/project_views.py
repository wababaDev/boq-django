from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from domain.boq.models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "domain/boq/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "client_name", "location", "reference_number",
              "management_fee_percent", "vat_percent"]
    template_name = "domain/boq/project_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("boq:project_detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "domain/boq/project_detail.html"
    context_object_name = "project"

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)