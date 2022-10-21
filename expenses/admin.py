from django.contrib import admin
from . models import *
from django.contrib import admin


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('id','category','name','amount','date')

admin.site.register(Category)    
