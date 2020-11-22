from django.db import models

# Create your models here.

class ToDo(models.Model):
    title=models.CharField(max_length=30)
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
