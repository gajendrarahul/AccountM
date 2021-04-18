from django.db import models
from abstract.models import Category, Abs
from django.contrib.auth.models import User
# Create your models here.


class ExpensesCategoryManager(models.Manager):
    pass


class ExpensesCategory(Category):
    objects = ExpensesCategoryManager()
    class Meta:
        unique_together = ('title','user')
        db_table = 'expensescategory'
    def __str__(self):
        return self.title


class ExpensesManager(models.Manager):
    pass


class Expenses(Abs):
    image = models.ImageField(upload_to='expenses/', null=True, blank=True)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)
    objects = ExpensesManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'expenses'
