from importlib.metadata import files
from pyexpat import model
from django import forms
from .models import Expense,Category


class ExpenseSearchForm(forms.ModelForm):
    date_ascended = forms.BooleanField()
    date_descended = forms.BooleanField()
    

    class Meta:
        model = Expense
        fields = ('name','date','category','amount','date_ascended', 'date_descended')
        widgets={
            'date':forms.TextInput(attrs={'placeholder':'yyyy/mm/dd'}),
            'name':forms.TextInput(attrs={'placeholder':'Title'}),
            'amount':forms.TextInput(attrs={'placeholder':'Amount'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date'].required = False
        self.fields['category'].required = False
        self.fields['amount'].required = False
        


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'