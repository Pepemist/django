from django.db import models

class ProdCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_img', null=True, blank=True)
    category = models.ForeignKey(to=ProdCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
