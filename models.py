from django.db import models


# Create your models here.

class Tour(models.Model):
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    days = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class booking(models.Model):
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    persons = models.IntegerField()

    def __str__(self):
        return self.name
