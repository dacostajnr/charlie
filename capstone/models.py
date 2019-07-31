from django.db import models

# Create your models here.

class Sensor(models.Model):
	name = models.CharField(max_length=100)
	pid = models.PositiveIntegerField(unique=True)
	unit = models.CharField(max_length=100)
	threshold = models.IntegerField(default="",null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name 


class Time(models.Model):
	sensor = models.ForeignKey(Sensor,related_name='times')
	value  = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.sensor.name+" value of "+self.value+" "+self.sensor.unit+" at " + str(self.timestamp)

class Alarm(models.Model):
	sensor = models.ForeignKey(Sensor,related_name='alarms',on_delete=models.CASCADE)
	value  = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)
	seen=models.BooleanField(default=False)

	def __str__(self) :
		return self.sensor.name +" alarm"+self.value+" more than "+str(self.sensor.threshold)






"""

When ajax checks a notification that exists,
it can set a checked=True
So we only need to check for alarms with checked=False
""" 



