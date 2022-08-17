from django.db import models

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Restaurant(models.Model):
    name=models.CharField(max_length=255,default="Restaurant")
    lng=models.DecimalField(max_digits=50, decimal_places=3)
    lat=models.DecimalField(max_digits=50, decimal_places=3)
    point = models.PointField()

    def __str__(self):
            return self.name

#Restaurant.objects.create(point=Point(lng, lat))