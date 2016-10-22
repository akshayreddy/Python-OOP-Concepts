

class vehicle:
	number_of_wheels=0
	name=""
	max_speed=0

	def get_time(self,distance):                                   # takes the instance as the first aurgument
		print "Time: %f hours" % (distance/float (self.max_speed))

ford=vehicle()       # An instance is created
ford.name="GP-83"
ford.number_of_wheels=4
ford.max_speed=100

print "Enter the distance in Km"
ford.get_time(input())
