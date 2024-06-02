from django.urls import path, re_path
from product import views

urlpatterns = [
    
    path('category/create/', views.create_category, name='create_category'),
    path("", views.categories, name="categories"),
    re_path(r'^category/edit/(?P<pk>.*)/$', views.edit_category, name='edit_category'),
    re_path(r'^delete-category/(?P<pk>.*)/$', views.delete_category, name='delete_category'),    
    re_path(r'^category/(?P<pk>.*)/$', views.category, name='category')    
    
]

