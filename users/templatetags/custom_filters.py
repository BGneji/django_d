from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Добавляет класс CSS к полю формы."""
    return field.as_widget(attrs={"class": css_class})