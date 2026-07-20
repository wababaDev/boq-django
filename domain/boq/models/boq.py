from decimal import Decimal
from django.conf import settings
from django.db import models

from domain.catalog.models import Trade, CatalogItem




class Project(models.Model):
    name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    reference_number = models.CharField(max_length=50, blank=True)
    management_fee_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00"),
        help_text="e.g. 10.00 for 10%",
    )
    vat_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00"),
        help_text="Applied to the management fee only, per her sample BoQ",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="boq_projects"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def items_total(self):
        return self.bill_items.aggregate(total=models.Sum("amount"))["total"] or Decimal("0")

    @property
    def management_fee_amount(self):
        return self.items_total * (self.management_fee_percent / Decimal("100"))

    @property
    def vat_amount(self):
        """VAT applies to the management fee only, matching her sample."""
        return self.management_fee_amount * (self.vat_percent / Decimal("100"))

    @property
    def grand_total(self):
        return self.items_total + self.management_fee_amount + self.vat_amount


class BillItem(models.Model):
    """One line in a project's bill. May come from the catalog (particularized)
    or be fully custom — both are first-class, per how she actually works."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bill_items")
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, related_name="bill_items")
    catalog_item = models.ForeignKey(
        CatalogItem, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="bill_items",
    )
    description = models.TextField()
    unit = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=12, decimal_places=2)
    rate = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=Decimal("0"), editable=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["trade__order", "order", "id"]

    def save(self, *args, **kwargs):
        self.amount = (self.quantity or 0) * (self.rate or 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description[:50]} ({self.project.name})"