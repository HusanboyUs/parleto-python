from importlib.metadata import files
from pyexpat import model
from django import forms
from .models import Expense,Category


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name','date','category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date'].required = False
        self.fields['category'].required = False
        


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'