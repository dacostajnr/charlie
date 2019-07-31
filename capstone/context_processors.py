from . models import Sensor,Time,Alarm

def all_sensors(request):
	return {"all_sensors":Sensor.objects.all()}

def all_alarms(request):
	return {"all_alarms":Alarm.objects.all()} 


def refresh_time(request):
	return {"refresh_time":70000}