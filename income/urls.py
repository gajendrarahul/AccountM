from django.urls import path
from .views import IncomeCategoryView, IncomeAddView, IncomeView, editIncome, removeIncome, removeIncomeCategory, editCategory
from . import views


urlpatterns = [
    path('category/', IncomeCategoryView.as_view(), name='income_category'),
    path('create/', IncomeAddView.as_view(), name='income_add'),
    path('incomeList', IncomeView.as_view(), name='income'),
    path('editIncome/<slug:slug>', views.editIncome, name='editIncome'),

    path('editCategory/<slug:slug>', views.editCategory, name='editCategory'),
    path('removeincome/<slug:slug>', views.removeIncome, name='removeincome'),
    path('removeincomecategory/<slug:slug>', views.removeIncomeCategory, name='removeincomecategory')
]