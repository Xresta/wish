from os import stat
from django.contrib import admin
from django.urls import path, include
from store import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.productView, 'product')
router.register(r'categories', views.categoryView, 'category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('products/', views.all_products.as_view(), name='all_products'),
    path('item/<slug:slug>/', views.product_detail.as_view(), name='product_detail'), 
    path('create/', views.createProductAPIView.as_view(), name='product_create'),
]
