from django.db import models


class OperatingSystem(models.Model):
    model = models.CharField('Название', max_length=50)
    creationyear = models.DecimalField('Год создания', decimal_places=0, max_digits=10)


class Computer(models.Model):
    model = models.CharField('Название', max_length=30)
    price = models.DecimalField('Цена', decimal_places=3, max_digits=10)
    os = models.ForeignKey(OperatingSystem, models.DO_NOTHING)

