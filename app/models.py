from __future__ import unicode_literals
#from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=100);
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    DAY = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    day = models.CharField(
        max_length=3,
        choices=DAY,
        default='mon',
        blank=False,
    )
    time = models.TimeField(default=datetime.strptime('00', '%H'), blank=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
		return self.name
	#def __unicode__(self):
		#return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100, default='new user', blank=False)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	classes = models.ManyToManyField(Class, blank=True)

	def __str__(self):
		return self.user.username

	def __unicode__(self):
		return self.name

class Layout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    class_id = models.OneToOneField(Class, on_delete=models.CASCADE)
    place_name = models.OneToOneField(Place, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='layout_images')
    def __str__(self):
		return self.place_name + ", " + self.class_id

	#def __unicode__(self):
		#return (self.place_name + ", " + self.class_id)


class Zone(models.Model):

    ZONE_NAMES = (
        ('A', 'Zone A'),
        ('B', 'Zone B'),
        ('C', 'Zone C'),
        ('D', 'Zone D'),
    )
    layout = models.OneToOneField(Layout, primary_key = True, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserProfile)
    zone_name = models.CharField(max_length=2, choices=ZONE_NAMES)

    def __str__(self):
		return "Zone name: " + self.zone_name + ", " + self.layout

	#def __unicode__(self):
		#return (self.class_id + ", " + self.layout)
