from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.views
from store.api.views import ProductList, ProductCreate, ProductRetrieveUpdateDestroy, ProductStats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/<int:id>/', store.views.show, name='show-product'),
    path('cart/', store.views.cart, name='shopping-cart'),
    path('', store.views.index, name='list-products'),
    path('api/v1/products', ProductList.as_view(), name='product-list'),
    path('api/v1/products/new', ProductCreate.as_view(), name='product-create'),
    path('api/v1/products/<int:id>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('api/v1/products/<int:id>/stats', ProductStats.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
