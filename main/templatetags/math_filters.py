from django import template

register = template.Library()

@register.filter
def divide_by(value, arg):
    try:
        return int(value) // int(arg)
    except (TypeError, ValueError, ZeroDivisionError):
        return 0
