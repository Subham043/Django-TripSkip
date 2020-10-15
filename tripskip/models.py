from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.
class IndexSearch(models.Model):
	name = models.CharField(max_length = 100)
	image = models.ImageField(upload_to = '')
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class Offer(models.Model):
	name = models.CharField(max_length = 100)
	promo = models.CharField(max_length = 100)
	mode = models.CharField(max_length = 100)
	desc = models.TextField()
	image = models.ImageField(upload_to = '')
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class Routes(models.Model):
	name = models.CharField(max_length = 100)
	departure = models.CharField(max_length = 100)
	arrival = models.CharField(max_length = 100)
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

class FAQ(models.Model):
	num = models.CharField(max_length = 100,default = "")
	question = models.TextField(default = "")
	answer = models.TextField(default = "")
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.num

class Flights(models.Model):
	fligthname =  models.CharField(max_length = 100,default = "")
	flightnum =  models.CharField(max_length = 100,default = "")
	depttime =  models.CharField(max_length = 100,default = "")
	arrtime =  models.CharField(max_length = 100,default = "")
	duration =  models.CharField(max_length = 100,default = "")
	price =  models.CharField(max_length = 100,default = "")
	image = models.ImageField(upload_to = '')
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.flightnum

class AirportOption(models.Model):
	airport = models.CharField(max_length = 100,default = "")
	airportcode = models.CharField(max_length = 100,default = "")
	place = models.CharField(max_length = 100,default = "")
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.airportcode

class HotelCarousel(models.Model):
	cityname = models.CharField(max_length = 100,default = "")
	price =  models.CharField(max_length = 100,default = "")
	image = models.ImageField(upload_to = '')
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.cityname

class HotelFAQ(models.Model):
	num = models.CharField(max_length = 100,default = "")
	question = models.TextField(default = "")
	answer = models.TextField(default = "")
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.num

class HotelDestination(models.Model):
	cityname = models.CharField(max_length = 100,default = "")
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.cityname


class HotelList(models.Model):
	name = models.CharField(max_length = 50, default = "")
	star = models.IntegerField(default = 0)
	location = models.CharField(max_length = 50, default = "")
	amen1 = models.CharField(max_length = 50, default = "")
	amen2 = models.CharField(max_length = 50, default = "")
	amen3 = models.CharField(max_length = 50, default = "")
	amen4 = models.CharField(max_length = 50, default = "")
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = '')
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    username =  models.CharField(max_length = 50, default = "", blank=True)
    phone = models.CharField(max_length=20, blank=True) #  change the field to watever works for you

    def __str__(self):
    	return self.user.username


class ComplaintMessage(models.Model):
	name = models.CharField(max_length = 50, default = "")
	email = models.CharField(max_length = 50, default = "")
	phone = models.CharField(max_length = 50, default = "")
	message = models.TextField(default = "")
	username = models.CharField(max_length = 50, default = "")

	def __str__(self):
		return self.username

class FlightOrderBooked(models.Model):
	username = models.CharField(max_length = 50, default = "")
	amount = models.CharField(max_length = 50, default = "")
	payment_id = models.CharField(max_length = 100, default = "")
	AdultName = models.CharField(max_length = 1000, default = "")
	ChildName = models.CharField(max_length = 1000, default = "")
	InfantName = models.CharField(max_length = 1000, default = "")
	DeparturePlace = models.CharField(max_length = 100, default = "")
	ArrivalPlace = models.CharField(max_length = 100, default = "")
	DepartureTime = models.CharField(max_length = 100, default = "")
	ArrivalTime = models.CharField(max_length = 100, default = "")
	FlightDate = models.CharField(max_length = 100, default = "")
	FlightNum = models.CharField(max_length = 100, default = "")
	email = models.CharField(max_length = 100, default = "")
	phone = models.CharField(max_length = 100, default = "")
	paid = models.BooleanField(default=False)

	def __str__(self):
		return self.username

class HotelOrderBooked(models.Model):
	username = models.CharField(max_length = 50, default = "")
	amount = models.CharField(max_length = 50, default = "")
	payment_id = models.CharField(max_length = 100, default = "")
	tRoom = models.CharField(max_length = 50, default = "")
	tAdults = models.CharField(max_length = 50, default = "")
	tChild = models.CharField(max_length = 50, default = "")
	HotelName = models.CharField(max_length = 50, default = "")
	checkIn =  models.CharField(max_length = 50, default = "")
	checkOut =  models.CharField(max_length = 50, default = "")
	FirstName =  models.CharField(max_length = 50, default = "")
	LastName =  models.CharField(max_length = 50, default = "")
	email =  models.CharField(max_length = 50, default = "")
	phone =  models.CharField(max_length = 50, default = "")
	paid = models.BooleanField(default=False)

	def __str__(self):
		return self.username


