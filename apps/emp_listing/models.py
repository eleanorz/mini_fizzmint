from django.db import models

class Manager(models.Model):
	name = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	created_at = models.DateTimeField()

	class Meta:
		db_table = 'managers'

class Employee(models.Model):
	manager = models.ForeignKey(Manager)
	name = models.CharField(max_length = 100)
	created_at = models.DateTimeField()

	class Meta:
		db_table = 'employees'