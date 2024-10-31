from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='shop'),
    path('category/<slug:category_slug>/', ShowViewCategories.as_view(), name='category'),
    path('add/', CreateProduct.as_view(), name='created_product'),
    path('product/update/<slug:slug>/', UpdateProduct.as_view(), name='update_product'),
    path('product/detail/<slug:slug>', ProductDetail.as_view(), name='detail_product'),
    path('product/delete/<slug:slug>', ProductDeleteView.as_view(), name='delete_product'),
]