from django.db import models

# Create your models here.
class Review(models.Model):
    uname = models.CharField(max_length=50)
    placename = models.CharField(max_length=30)
    review = models.TextField()