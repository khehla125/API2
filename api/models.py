from django.db import models

class DataLogger(models.Model):
    device = models.CharField(max_length=50)
    temperature = models.FloatField()
    turbidity = models.FloatField()
    conductivity = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.timestamp}"
