from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic import TemplateView

from .forms import ProductForm, ProductDeleteForm
from .models import Category, Product
from .utils import CategoritsMixin


class HomeView(TemplateView, CategoritsMixin):
    template_name = 'shop/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class ShowViewCategories(ListView, CategoritsMixin):
    template_name = 'shop/product_category.html'
    model = Product
    context_object_name = 'categories_product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товары {self.kwargs['category_slug']}'
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'products_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Старинца о продукте'
        return context


class CreateProduct(CreateView, CategoritsMixin):
    form_class = ProductForm
    template_name = 'shop/create_product.html'
    success_url = reverse_lazy('shop')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Старинца добавить продукт'
        return context


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/update_product.html'
    success_url = reverse_lazy('shop')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Старинца изменить продукт'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'
    success_url = reverse_lazy('shop')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductDeleteForm()
        context['title'] = "Страница удаления продукта"
        return context

    def post(self, request, *args, **kwargs):
        form = ProductDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.success_url)
        return self.get(request, *args, **kwargs)
