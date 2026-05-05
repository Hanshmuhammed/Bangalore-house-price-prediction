from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Houses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=150)
    sqft = models.BigIntegerField()
    bathroom = models.IntegerField()
    bedroom = models.IntegerField()
    predicted_price = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.predicted_price}"