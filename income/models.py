from django.db import models
from abstract.models import Category,Abs
# Create your models here.


class IncomeCategoryManager(models.Manager):
    pass


class IncomeCategory(Category):
    objects = IncomeCategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'user')
        db_table = 'incomecategory'


class IncomeManager(models.Manager):
    pass


class Income(Abs):
    image = models.ImageField(upload_to='income/', null=True, blank=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    objects = IncomeManager()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'category')
        db_table = 'income'