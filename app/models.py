from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    url = models.URLField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.name
    
