from django import template

register = template.Library()

@register.filter
def add_tax(price, tax_rate):
    try:
        tax_amount = float(price) * (float(tax_rate) / 100)
        total = float(price) + tax_amount
        return f"Rs. {total:.2f}"
    except (ValueError, TypeError):
        return price