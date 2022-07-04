from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from ..utils import *

register = template.Library()

@register.filter
def insert_emoji(arg):
    arg = conditional_escape(arg)
    for key,value in emojis.items():
        arg = arg.replace(key, f'<img src="/media/{value}" width="30" height="30">')
    return mark_safe(arg)
