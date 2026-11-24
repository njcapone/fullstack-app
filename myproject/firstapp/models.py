from django.db import models

# Create your models here.

# sample model from the course
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length = 255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length = 1000)
"""
make a model, do the following

python manage.py makemigrations
python manage.py migrate
"""

