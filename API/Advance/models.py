from datetime import datetime

from django.db import models
class BookModel(models.Model):
    name = models.CharField(max_length=50)
    auth = models.CharField(max_length=50)
    store = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=datetime.now())

# Create your models here.
