class vehicle:

	Booster=20                  #class varible

	def __init__(self,name,max_speed):      #constructor
		self.name=name                      #instance varibles
		self.max_speed=max_speed

	def get_time(self,distance):      
		print "Time: %f hours" % (distance/float (self.max_speed)) 


#inheritence   

class buses(vehicle):

	def __init__(self,name,max_speed,number_of_seats):   #constructor 
		#super().__init__(name,max_speed)        
		vehicle.__init__(self,name,max_speed)
		self.number_of_seats=number_of_seats



ford=vehicle("GT-45",100)


number_of_seats=input("Enter the number of seats\n")

volvo=buses("VO-45",60,number_of_seats)      #adding new feature (reusing the code)



#print(help(buses))                 #Note # first it searchers for the methods/changes in the child class
#print (isinstance(volvo,vehicle))  
#print (issubclass(buses,vehicle))