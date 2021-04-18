from .models import Income, IncomeCategory
from django import forms


class IncomeCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = IncomeCategory
        fields = ['title']


class IncomeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=None)

    def __init__(self, id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = IncomeCategory.objects.filter(user_id=id)

    class Meta:
        model = Income
        fields = '__all__'