from django.db import models

class Trade(models.Model):
    """One 'Bill' from the AAQS model — e.g. Earthworks, Masonry, Carpentry."""
    name = models.CharField(max_length=120, unique=True)
    bill_number = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class CatalogItem(models.Model):
    """A standard AAQS item description, with '?' placeholders for
    project-specific dimensions. Seeded once, not edited via the app."""
    trade = models.ForeignKey(Trade, on_delete=models.PROTECT, related_name="items")
    item_code = models.CharField(max_length=20, blank=True)
    description_template = models.TextField()
    unit = models.CharField(max_length=20)

    class Meta:
        ordering = ["trade__order", "id"]

    def __str__(self):
        return f"{self.item_code} — {self.description_template[:60]}"