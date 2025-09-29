from django.contrib import admin
from prod.models import ProdCategory, Product

admin.site.register(Product)
admin.site.register(ProdCategory)