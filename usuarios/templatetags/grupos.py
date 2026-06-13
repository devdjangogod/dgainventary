from django import template

register = template.Library()

@register.filter
def tiene_grupo(user, nombre_grupo):
    return user.groups.filter(name=nombre_grupo).exists()