
from django.test import TestCase,Client
from django.urls import reverse
from expenses.models import Category,Expense
import datetime

class TestView(TestCase):

    def setUp(self):
        self.client=Client()
        self.expense_list_url=reverse('expense/list/')
        self.category_list_url=reverse('category/list/')

        Category.objects.create(
            name='Travelling'
        )
    

    def category_list_GET(self):
        response=self.client.get(self.category_list_url)
        self.assertEqual(response.status_code, 200)

    def expense_list_GET(self):
        response=self.client.get(self.expense_list_url)
        self.assertEqual(response.status_code, 200) 

    def expense_create(self):
        response=self.client.get(self.expense_list_url)
        self.assertEquals(response.status_code, 302)
        self.assertGreater(Category.objects.all().count(),4)