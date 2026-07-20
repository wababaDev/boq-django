from django import template

register = template.Library()


@register.filter
def trade_subtotal(items):
    return sum(item.amount for item in items)