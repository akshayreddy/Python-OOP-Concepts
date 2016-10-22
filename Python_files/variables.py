class vehicle:

	Booster=20                  #class varible

	def __init__(self,name,max_speed):
		self.name=name                      #instance varibles
		self.max_speed=max_speed

	def get_time(self,distance):
		print "Time: %f hours" % (distance/float (self.max_speed))

	def boost(self):
		vehicle.Booster=self.max_speed+vehicle.Booster

ford=vehicle("GT-8",100)      # An instance is created
nisan=vehicle("HH-147",80)


name=input("Enter the car brand- ford/nisan\n")
distance=input("Enter the distance in Km\n")
name.get_time(distance)
name.boost()

#print (name.__dict__)
#vehicle.Booster=30                  
#print (vehicle.__dict__)            #Remove the comments and understand