from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='products')

    def __str__(self):
        return f'{self.name} | {self.category.title}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
