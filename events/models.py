from django.db import models
from users.models import CustomUser

class Place(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Transport(models.Model):
    title = models.CharField(max_length=100)
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return self.title

    def free_seats(self):
        return self.max_people - self.seats

class Event(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    transport = models.ManyToManyField(Transport)
    promoter = models.ManyToManyField(CustomUser)
    date = models.DateTimeField()

    def __str__(self):
        return self.place.title

