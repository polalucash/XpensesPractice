import silly
from django.core.management import BaseCommand
import silly
from expenses.models import Expense

class Command(BaseCommand):
	help = "Create new random expenses."
	
	def add_arguments(self, parser):
		parser.add_argument('n', type=int)
	
	def handle(self, n, **options):
		for i in range(n):
			o = Expense(
				title=silly.title(),
				date=silly.datetime(),
				amount=silly.number(),
				discrption=silly.paragraph()
			)
			o.save()