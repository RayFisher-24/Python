class Car(object):

	new_modefication = 'v12'

	def __init__(self, name, color, price, engine):
		self.name = name
		self.color = color
		self.price = price
		self.engine = engine

	def new_upgrade(self):	
		self.engine = Car.new_modefication

	@classmethod
	def Classes(cls, engine):
		cls.new_modefication = engine	
	
	@staticmethod
	def Statices(car):
		engine = 'v14'
		if car == engine:
			return True
		else:
			return False	

c1 = Car('lamborghini', 'green', '140k', 'v10')
print(c1.engine)
c1.new_upgrade()
print(c1.engine)

Car.Classes('v14')
c1.new_upgrade()
print(c1.engine)	

print(Car.Statices(upper('v14'))	