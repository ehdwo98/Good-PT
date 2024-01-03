import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def sub(value, reg):
    return value - reg


@register.filter
def div(value, reg):
    return value // reg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))