from django.urls import path
from .views import ExpenseCategoryView,ExpenseAddView,ExpenseView
from . import views
urlpatterns = [
    path('category/', ExpenseCategoryView.as_view(), name='expense_category'),
    path('create/', ExpenseAddView.as_view(), name='expenses_add'),
    path('expenseList', ExpenseView.as_view(), name='expenses'),
    path('editExpense/<slug:slug>', views.editExpense, name='editExpense'),
    path('removeExpenses/<slug:slug>', views.removeExpenses, name='removeExpenses'),
    path('editCategory/<slug:slug>', views.editECategory, name='editECategory'),
    path('removeexpenseCategory/<slug:slug>',views.removeexpenseCategory, name='removeexpenseCategory')
]
