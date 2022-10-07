from django.db import models

# Create your models here.
class Customers (models.Model):
    Image = models.ImageField(upload_to='images/')
    text = models.TextField()
    socialMedia = models.URLField()
    