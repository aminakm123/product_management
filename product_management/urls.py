from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(('product.urls','product'),namespace='product'))
]
