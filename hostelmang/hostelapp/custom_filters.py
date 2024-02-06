# yourapp/templatetags/custom_filters.py

from django import template

register = template.Library()

displayed_hostels = set()

@register.filter(name='hostel_displayed')

def hostel_displayed(hostel_id):
    if hostel_id in displayed_hostels:
        return True
    displayed_hostels.add(hostel_id)
    return False
