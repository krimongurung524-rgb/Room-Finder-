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
    
@register.simple_tag
def location_url(location):
    if not location:
        return "#"
    
    location = location.lower().strip()
    
    location_map = {
        'kathmandu': 'https://www.google.com/maps/search/Kathmandu,+Nepal',
        'biratnagar': 'https://www.google.com/maps/search/Biratnagar,+Nepal',
        'pokhara': 'https://www.google.com/maps/search/Pokhara,+Nepal',
        'lalitpur': 'https://www.google.com/maps/search/Lalitpur,+Nepal',
        'bhaktapur': 'https://www.google.com/maps/search/Bhaktapur,+Nepal',
    }
    
    return location_map.get(location, '#')  