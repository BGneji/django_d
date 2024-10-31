from django.views.generic.base import ContextMixin

from .models import Category


class CategoritsMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('id')
        return context
