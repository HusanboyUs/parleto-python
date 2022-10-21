from functools import total_ordering
from unicodedata import category
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.urls import path, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .forms import ExpenseSearchForm,UpdateCategoryForm
from .models import Expense, Category
from .reports import summary_per_category,summary_per_month_year,all_sumed


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        


        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            date=form.cleaned_data.get('date')
            category=form.cleaned_data.get('category')
            amount=form.cleaned_data.get('amount', )
            date_ascend = form.cleaned_data.get('date_ascended')
            date_descend= form.cleaned_data.get('date_descended') 

            if name:
                queryset = queryset.filter(name__icontains=name)
            if date:
                try: #try less than, to
                    queryset=queryset.filter(date__lt=date)
                except: #try greater than, from
                    queryset=queryset.filter(date__gte=date)
            if category is not None :
                queryset=queryset.filter(category=category)

            if amount:
                queryset = queryset.filter(amount__gte=amount)  

            if date_ascend:
                queryset = queryset.filter().order_by('date')
            if date_descend:
                queryset = queryset.filter().order_by('-date')                 
          
        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),summary_per_month_year=summary_per_month_year(queryset),all_sumed=all_sumed(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)



class update_category_view(UpdateView):
    model=Category
    fields='__all__'
    template_name='update_category.html'
    success_url=reverse_lazy('expenses:category-list')
update_category=update_category_view.as_view()


#alternative view(function based) for category update.
def UpdateCategoryView(request, pk):
    model=Category.objects.get(id=pk)
    form=UpdateCategoryForm(instance=model)
    if request.method=='POST':
        form=UpdateCategoryForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('expenses:category-list')

    context={'form':form,'model':model}
    return render(request, 'update.html',context)        




