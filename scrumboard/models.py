from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # relation with foreign key below
    # each Card must belong to a List
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)