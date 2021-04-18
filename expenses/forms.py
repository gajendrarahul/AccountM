from .models import Expenses, ExpensesCategory
from django import forms


class ExpensesCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ExpensesCategory
        fields = ['title']


class ExpenseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=None)

    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = ExpensesCategory.objects.filter(user_id=id)

    class Meta:
        model = Expenses
        fields = '__all__'