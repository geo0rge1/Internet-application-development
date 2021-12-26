from django.db import models


class Stock(models.Model):
    namestock = models.CharField(max_length=50, verbose_name="Название компании")
    description = models.CharField(max_length=50, verbose_name="описание компании")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена акции")