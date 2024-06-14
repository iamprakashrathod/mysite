from django.db import models
from datetime import datetime

# Create your models here.
class Tutorial(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	published = models.DateTimeField('published', default=datetime.now())

	def __str__(self):
		return self.name
