from django.db import models
from django.contrib import admin
# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=20, help_text="Enter product Name")
    price = models.IntegerField(help_text="Enter product price")
    mfg_date = models.DateField()
    product_code = models.IntegerField(help_text="Enter product code")

class productAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'mfg_date ', 'product_code ']