from django.db import models


class Expense(models.Model):
	date = models.DateField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	title = models.CharField(max_length=300)
	discrption = models.TextField(blank=True)
	def __str__(self):
		return self.title

