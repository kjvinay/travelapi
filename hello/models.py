from django.db import models
from datetime import datetime
from django.db.models import DecimalField

SEMESTER_CHOICES = (
    ("0", "0"),
    ("1", "1")      
) 
PACKAGE_CHOICES =(
    ("4&40", "1"),
    ("8&80", "2"),
    ("6&60", "3"),
    ("10&100", "4"),
    ("5&50", "5"),
    ("3&30", "6"),
    ("12&120", "7")
    )
TRAVEL_CHOICES =(
    ("long distance", "1"),
    ("point to point", "2"),
    ("hourly rental", "3"),
    )
VEHICLE_CHOICES =(
    ("SEDAN", "1"),
    ("COUPE", "2"),
    ("SPORTS CAR", "3"),
    ("HATCHBACK","4"),
    ("SPORT-UTILITY VEHICLE","5")
    )

class area(models.Model):
      area_name=models.CharField(max_length=15, unique=True)
      unique_id=models.IntegerField(blank=True)
      at_longitude=models.DecimalField(max_digits=9, decimal_places=6)
      at_latitude=models.DecimalField(max_digits=9, decimal_places=6)

def __str__(self):
    return self.area_name


class city(models.Model):
      city_name=models.CharField(max_length=15, unique=True)
      unique_id=models.IntegerField(blank=True)
      at_longitude=models.DecimalField(max_digits=9, decimal_places=6)
      at_latitude=models.DecimalField(max_digits=9, decimal_places=6)
def __str__(self):
    return self.city_name

class area_travel(models.Model):
      user_no=models.CharField(max_length=10)
      from_area_id=models.IntegerField(blank=True)
      to_area_id=models.IntegerField(blank=True)
      from_longitude=models.DecimalField(max_digits=9, decimal_places=6)
      from_latitude=models.DecimalField(max_digits=9, decimal_places=6)
      to_longitude=models.DecimalField(max_digits=9, decimal_places=6)
      to_latitude=models.DecimalField(max_digits=9, decimal_places=6)
      booking_time=models.DateTimeField(default=datetime.now)
      online_booking=models.BooleanField()
      mobile_site_booking=models.BooleanField()
      car_cancellation=models.CharField(max_length = 20,choices = SEMESTER_CHOICES,blank=True)
      from_date=models.DateTimeField(default=datetime.now)
      to_date=models.DateTimeField(default=datetime.now)
      package_id=models.CharField(max_length = 20,choices = PACKAGE_CHOICES,blank=True)
      travel_type=models.CharField(max_length = 50,choices = TRAVEL_CHOICES,blank=True)
      vehicle_type=models.CharField(max_length = 50,choices = VEHICLE_CHOICES,blank=True)
      
def __str__(self):
    return self.user_no

class city_travel(models.Model):
      user_no=models.CharField(max_length=10)
      from_city_id=models.IntegerField(blank=True)
      to_city_id=models.IntegerField(blank=True)
      from_longitude=models.DecimalField(max_digits=9, decimal_places=6,blank=True)
      from_latitude=models.DecimalField(max_digits=9, decimal_places=6,blank=True)
      to_latitude=models.DecimalField(max_digits=9, decimal_places=6,blank=True)
      to_longitude=models.DecimalField(max_digits=9, decimal_places=6,blank=True)
      booking_time=models.DateTimeField(default=datetime.now)
      online_booking=models.BooleanField()
      mobile_site_booking=models.BooleanField()
      car_cancellation=models.CharField(max_length = 20,choices = SEMESTER_CHOICES,blank=True)
      from_date=models.DateTimeField(default=datetime.now)
      to_date=models.DateTimeField(default=datetime.now)
      package_id=models.CharField(max_length = 20,choices = PACKAGE_CHOICES,blank=True)
      travel_type=models.CharField(max_length = 50,choices = TRAVEL_CHOICES,blank=True)
      vehicle_type=models.CharField(max_length = 50,choices = VEHICLE_CHOICES,blank=True)

      

def __str__(self):
    return self.user_no
