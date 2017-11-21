import silly
from django.shortcuts import render

# Create your views here.
from expenses.models import Expense


def home(request):
	return render(request, 'expenses/home.html', {"objects": Expense.objects.all(),})