from django import template

register = template.Library()

@register.filter
def truncatechars(value, arg):
    """
    Truncates a string after a certain number of characters.
    Argument: Number of characters to truncate after.
    """
    try:
        length = int(arg)
    except ValueError:  # Invalid literal for int().
        return value  # Fail silently.

    if len(value) > length:
        return value[:length] + '...'
    return value
