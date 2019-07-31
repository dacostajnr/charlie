from django.shortcuts import render
from django.http import HttpResponse,JsonResponse 
from .models import Sensor,Time,Alarm 
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Max, Min

# Create your views here.

def home(request):
	# get all sensor objects
	all_sensors = Sensor.objects.all()
	# bring up any notifications or alarms 
	return render(request,"capstone/morris.html",{"all_sensors":all_sensors}) 	



@csrf_exempt
def endpoint(request,id):
	"""
	The sensor just sends values to this endpoint
	1.Create a Time class with this data
	2.Create a notification if the threshhold is exceeded.

	The aim is to create a time object for this sensor and create an alarm if the value exceeds its threshold
	"""
	try:
		# get the sensor 
		sensor=Sensor.objects.get(pid=id) 
		# get the data  
		value = request.POST["data"]
		# create a Time object for that sensor 						
		time=Time.objects.create(sensor=sensor,value=value)
		#time.save() # find out if this line is needed   

		# create a notification for this sensor if the threshold is exceeded 
		if sensor.threshold==None:
			pass 
		else:
			# check if threshold is exceeded
			if int(value)>int(sensor.threshold):
				# create Alarm 
				alarm = Alarm.objects.create(sensor=sensor,value=value,seen=False)
				#alarm.save() # find out if this line is important 		
		return HttpResponse("ok")
	except Exception as e:
		return HttpResponse("Not Found") 

def ajax(request):
	# return the time object of every model 	
	sensors=Sensor.objects.all()
	data=[]
	for i in range(0,len(sensors)):		
		d = {}
		d["name"] = sensors[i].name 

		d["times"] = []
		d["id"] =sensors[i].pid
		for j in sensors[i].times.all():
			_dict = {} 
			_dict["time"] = j.timestamp
			_dict["value"] = j.value 
			d["times"].append(_dict) 
		data.append(d)	
	return JsonResponse({"data":data})


def ajax1(request,pid):	
	sensor=Sensor.objects.get(pid=pid)
	data=[]
	for j in sensor.times.all():
		_dict = {} 
		_dict["time"] = j.timestamp
		_dict["value"] = j.value 		
		data.append(_dict)		
	return JsonResponse({"data":data})	


def sensor_detail(request,id):
	# get the sensor
	sensor = Sensor.objecs.get(pid=id)
	# get all the sensor values..use ajax here
	return HttpResponse("ok")



def notification_detail(request,id):
	# get all alarms 
	seen_alarms = Alarm.objects.filter(seen=True)
	unseen_alarms = Alarm.objects.filter(seen=False)
	selected_notification = Alarm.objects.get(id=id)
	return render(request,"capstone/notification.html",
		{"seen_alarms":seen_alarms,"unseen_alarms":unseen_alarms,"id":id})

	
def clear_notification(request,id):
	return HttpResponse("ok")  


def sensor_detail(request,id):
	# get the sensor 
	sensor = Sensor.objects.get(id=id) 
	all_times = sensor.times.all() 
	# get the max  value and date
	#max_value = all_times.aggregate(Max("value"))
	max_value = all_times.order_by("value")[0].value
	# get the min value and date
	min_value = all_times.order_by("value")[len(all_times)-1].value
	#min_value = all_times.aggregate(Min("value"))

	min_date_occured = all_times.order_by("value")[0].timestamp.strftime("%D")
	min_time_occured = all_times.order_by("value")[0].timestamp.strftime("%H:%M:%S")
	max_date_occured= all_times.order_by("value")[len(all_times)-1].timestamp.strftime("%D")
	max_time_occured= all_times.order_by("value")[len(all_times)-1].timestamp.strftime("%H:%M:%S")

	return render(request,"capstone/sensor_detail.html",
		{"sensor":sensor,
		"max_value":max_value,
		"min_value":min_value,
		"max_date_occured":max_date_occured,
		"max_time_occured":max_time_occured,
		"min_time_occured":min_time_occured,
		"min_date_occured":min_date_occured}) 



