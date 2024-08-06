from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)
    createdat = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.task