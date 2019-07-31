'''
By slimtrissly@gmail.com
'''
1.Arduino sends sensort values to endpoints
	-Sensor 1 sends values to endpoint/id/1
	-Sensor 2 sends values to endpoint/id/2 	
2.Django receives data and stores value as a Time Model 
	-Sensor type using id
	-Time stamp
	-actual value sent 		
3.User uses the /home path to access the index file 
	 -This page displays all the sensor values 
		-Take each sensor model one by one 
		-Return each as a dictionary to the index file 
		-The index file displays only the latest Time of each sensor model 
		-The index file displays all the Times of each sensor model 
		-Add a chart of time(x-axis) against value(y-axis) with a chosen interval 
		-use jquery ajax to update eah chart every 10 seconds(url/ajax/)
			-fetch from each model's Time objects(fetch all together)
			-update each chart with corresponding ajax(using the key value pair of incoming response)	
	 ALTERNATIVE
	 -For start dont return anything to the index file 
	 -Let Ajax do the fetching 	 
#------------------------------
1.Create Sensors(DONE)
	-temperature-Pid1T10(degree celcius)
	-pressure-Pid2T12(atm)
	-depth-Pid3null(meters)	
	-heart rate(bpm)
2.Create 2 Time objects for each (DONE)
	- 2 normal
	- 2 on threshold 	
	
3.Do 2 using http,curl,python request,postman(Make sure a notification is created) (DONE)
4.Add BOOTSTRAP AND JQUERY TO PROJECT(DONE)
5.Configure the index page when the DB is empty
6.Configure the index page when there is data 
7.Code notification for abnormal conditions
8.Code the graphs 
	
	
NB: When a u dont enter a sensor threshold it's default value is "None" instead of ""
NB: Instead of coding the notification for the endpoint view,
	we can make it a signals handler so that creating it in the admin	
	dashboard will also affect it 
	
# requests.post("http://127.0.0.1:8000/endpoint/id/1",data={"data":12})
# always get pid  and not id 
	

	