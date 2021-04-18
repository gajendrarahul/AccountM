from django.shortcuts import render, redirect
from django.views import View
from .forms import IncomeForm, IncomeCategoryForm
from django.contrib import messages
from .models import IncomeCategory, Income
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class IncomeCategoryView(View):
    template_name = 'income_category.html'

    def get(self, request):
        context = {
            'form': IncomeCategoryForm(),
            'category': IncomeCategory.objects.filter(user_id=request.user.id)

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = IncomeCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "saved successfully!!!")
            return redirect('income_category')
        else:
            messages.add_message(request, messages.ERROR, "sorry error occurred")
            return redirect('income_category')


class IncomeAddView(View):
    template_name = 'add_income.html'

    def get(self, request):
        context = {
            'form': IncomeForm(id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = IncomeForm(request.user.id, request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully added")
            return redirect('income')
        else:
            return render(request, self.template_name, context={'form': form})


class IncomeView(View):
    template_name = 'income.html'

    def get(self, request):
        context = {
            'all': Income.objects.filter(category__in=IncomeCategory.objects.filter(user_id=request.user.id))
        }
        return render(request, self.template_name,context)


def editIncome(request, slug):
    if request.method == 'GET':
        context = {
            'form': IncomeForm(request.user.id, instance=Income.objects.get(slug=slug))
        }
        return render(request, 'edit_income.html', context)
    else:
        form = IncomeForm(request.user.id, request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Added")
            return redirect('income')
        else:
            messages.add_message(request, messages.ERROR, "Sorry")
            return redirect('income')


def editCategory(request, slug):
        form = IncomeCategoryForm(request.POST or None, instance=IncomeCategory.objects.get(slug=slug))
        if form.is_valid():
            form.save()
            return redirect('income_category')
        else:
            return render(request,'income_category.html', {'form':form})

# removes the Income
def removeIncome(request, slug):
    s = Income.objects.get(slug=slug)
    s.delete()
    return redirect('income')


# removes the Income Category
def removeIncomeCategory(request, slug):
    c = IncomeCategory.objects.get(slug=slug)
    c.delete()
    return redirect('income_category')