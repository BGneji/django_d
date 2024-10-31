from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserRegisterForm


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('shop')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Старинца регистрации'
        return context
