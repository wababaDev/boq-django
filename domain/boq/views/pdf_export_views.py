from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import  DetailView

from domain.boq.models import Project

class ProjectExportPDFView(LoginRequiredMixin, DetailView):
    model = Project

    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        html_string = render_to_string(
            "domain/boq/project_pdf.html", {"project": project}
        )
        pdf = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf, content_type="application/pdf")
        filename = f"BoQ - {project.name}.pdf"
        response["Content-Disposition"] = f'inline; filename="{filename}"'
        return response