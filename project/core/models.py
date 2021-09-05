from django.db import models
import random
import string


class UrlKey(models.Model):
	key = models.SlugField(unique=True)
	url = models.URLField()
	redirect_count = models.IntegerField()

	def save(self, *args, **kwargs):
		if not self.pk:
			self.key = ''.join(random.sample(list(string.ascii_letters + string.digits), 5))
			self.redirect_count = 0
		super().save(*args, **kwargs)
