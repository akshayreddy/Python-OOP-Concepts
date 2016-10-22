class vehicle:

	Booster=20                  #class varible

	def __init__(self,name,max_speed):      #constructor
		self.name=name                      #instance varibles
		self.max_speed=max_speed

	def boost(self):                        #instance method (changs within the class,takes instance as argument)
		vehicle.Booster=self.max_speed+vehicle.Booster

	@classmethod
	def add_values(cls):        #constructor methdod(used to perform some logic when an instance is created, takes class as argument)
		pass

	@staticmethod
	def get_time(distance):       #static methode(takes neither instance or class as arguments, no interaction with class parameters)
		print "Time: %f hours" % (distance/float (60)) # equivalent to a normal fuction, but within a class

#value="GT-3,100"
#instance=vehicle.add_vale(value)

ford=vehicle("GT-8",100)
nisan=vehicle("HH-147",80)

distance=input("Enter the distance in Km\n")
vehicle.get_time(distance)
