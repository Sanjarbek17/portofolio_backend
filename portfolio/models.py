from django.db import models

# Create your models here.
class First(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name