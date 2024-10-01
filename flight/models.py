from django.db import models


class Flight(models.Model):
    flight_no = models.CharField(max_length=10, unique=True)
    airline = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.flight_no} - {self.airline}"
