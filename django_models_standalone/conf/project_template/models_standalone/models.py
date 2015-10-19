from django.db import models

class SampleModel(models.Model):
	def __unicode__(self):
		return self.pk