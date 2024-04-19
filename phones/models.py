from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    release_date = models.CharField(max_length=1000)
    lte_existst = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000)
