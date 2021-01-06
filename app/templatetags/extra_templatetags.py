from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    """Removes all values of arg from the given string with whitespace"""
    return value.replace(arg, ' ')