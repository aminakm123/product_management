from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']


    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE, limit_choices_to={'is_deleted': False})
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/products/")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']

    def __str__(self):
        return str(self.name)