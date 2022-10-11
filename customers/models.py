from django.db import models

# Create your models here.
class Customers (models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    socialMedia = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.socialMedia}'