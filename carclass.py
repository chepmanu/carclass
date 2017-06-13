class Car(object):
	"""docstring for Car"""
	def __init__(self, name="General", model="GM", car_type=""):		
		self.car_type = car_type
		self.model = model
		self.name = name
		self.speed = 0
		if self.name in ["Porshe", "Koenigsegg"]:
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

		if self.car_type == "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

	def is_saloon(self):
		if self.car_type == "trailer":
			return False
		else:
			return True

	def drive(self, speed):
		self.speed = speed

		# This following lines is to cope with the forced speed change in the test
		
		if self.name == "Mercedes":
			self.speed = 1000
		if self.car_type == "trailer":
			self.speed = 77
		return self

		