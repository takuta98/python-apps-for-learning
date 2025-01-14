from django.db import models

# Create your models here.


class MarkerModel(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='', null=True)
    tag = models.CharField(max_length=20, null=True)
    memo = models.TextField(null=True)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)

    def __str__(self):
        return self.title
