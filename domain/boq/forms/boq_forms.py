from django import forms
from domain.boq.models import BillItem


class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ["trade", "catalog_item", "description", "unit", "quantity", "rate"]
        widgets = {
            "catalog_item": forms.HiddenInput(),
            "description": forms.Textarea(attrs={"rows": 3}),
        }