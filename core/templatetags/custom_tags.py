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
    location = location.lower().strip()
    
    if location == 'kathmandu':
        return "https://www.google.com/maps/place/Kathmandu+44600/@27.7089543,85.284933,13z/data=!3m1!4b1!4m6!3m5!1s0x39eb198a307baabf:0xb5137c1bf18db1ea!8m2!3d27.7103145!4d85.3221634!16zL20vMDRjeDU?entry=ttu&g_ep=EgoyMDI2MDgxOS4wIKXMDSoASAFQAw%3D%3D"
    elif location == 'biratnagar':
        return "https://www.google.com/maps/place/Biratnagar+56613/@26.4481888,87.1894055,12z/data=!3m1!4b1!4m6!3m5!1s0x39ef744704331cc5:0x6d9a85e45c54b3fc!8m2!3d26.4559006!4d87.2802344!16zL20vMDRncjRf?entry=ttu&g_ep=EgoyMDI2MDgxOS4wIKXMDSoASAFQAw%3D%3D"
    elif location == 'pokhara':
        return "https://www.google.com/maps/place/Pokhara/@28.2296977,83.8742167,12z/data=!3m1!4b1!4m6!3m5!1s0x3995937bbf0376ff:0xf6cf823b25802164!8m2!3d28.2095831!4d83.9855674!16zL20vMDQwZHgz?entry=ttu&g_ep=EgoyMDI2MDgxOS4wIKXMDSoASAFQAw%3D%3D"
    else:
        return "#"   