from django.shortcuts import render,redirect
from django.views import View
from .forms import ExpenseForm, ExpensesCategoryForm
from django.contrib import messages
from .models import ExpensesCategory, Expenses
# Create your views here.


class ExpenseCategoryView(View):
    template_name = 'expenses_category.html'

    def get(self, request):
        context = {
            'form': ExpensesCategoryForm(),
            'category': ExpensesCategory.objects.filter(user_id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ExpensesCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS,"Saved Successfully")
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR,"Sorry Error occurred")
            return redirect('dashboard')


class ExpenseAddView(View):
    template_name = 'add_expenses.html'

    def get(self, request):
        context = {
            'form': ExpenseForm(id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ExpenseForm(request.user.id,request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"successfully added")
            return redirect('expenses')
        else:
            return render(request,self.template_name,context={'form': form})


class ExpenseView(View):
    template_name = 'expenses.html'

    def get(self, request):
        context = {
            'all': Expenses.objects.all()
        }
        return render(request, self.template_name,context)


def editExpense(request, slug):
    if request.method == 'GET':
        context = {
            'form': ExpenseForm(request.user.id, instance=Expenses.objects.get(slug=slug))
        }
        return render(request, 'edit_expenses.html', context)
    else:
        form = ExpenseForm(request.user.id, request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Added")
            return redirect('expenses')
        else:
            messages.add_message(request, messages.ERROR, "Sorry")
            return redirect('expenses')


def editECategory(request, slug):
    form = ExpensesCategoryForm(request.POST or None, instance=ExpensesCategory.objects.get(slug=slug))
    if form.is_valid():
        form.save()
        return redirect('expense_category')
    else:
        return render(request, 'expenses_category.html', {'form': form})


def removeExpenses(request, slug):
    s = Expenses.objects.get(slug=slug)
    s.delete()
    return redirect('expenses')


def removeexpenseCategory(request, slug):
    c = ExpensesCategory.objects.get(slug=slug)
    c.delete()
    return redirect('expense_category')



