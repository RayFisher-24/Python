class Employee(object): #main Class
	increment = 2 #class variable
	def __init__(self,name,salary): #initializetion
		self.name = name
		self.salary = salary
		self.increment = 1.4 #intence variable
	
	def increse(self):
		#self.salary = int(self.salary*self.increment)
		self.salary = int(self.salary*Employee.increment)

	@classmethod #class method for playing with class variable
	def change_increse(cls,amount):
		cls.increment = amount

	@staticmethod # static method for neither for class or intence playing
	def isopen(day):
		txt='sunday'
		if day == txt:
			return False
		else:
			return True

	def __add__(self,other):
		return self.salary + other.salary	

	def __repr__(self):
		return 'Employee({} {})'.format(self.name, self.salary)	

	def __str__(self):
		return 'The Emplyee name is {}'.format(self.name)	

class Programmer(Employee): #subClass
	def __init__(self, name, salary, lang):
		super().__init__(name,salary)
		self.lang = lang

		

Emp1 = Employee('ram', 74000) #main Class objects
Emp11 = Programmer('ram', 74000,'python') #sub Class objects
Emp2 = Employee('sam', 73000)

#FOR CLASS AND INTENCE VARIABLE
print(Emp1.__dict__)	
print(Emp1.name)
print(Emp1.salary)
Emp1.increse()
print(Emp1.salary)

#FOR CLASSMETHOD
Employee.change_increse(4)
Emp1.increse()
print(Emp1.salary)

#FOR STATICMETHOD
print(Employee.isopen('sunday'))

#FOR INHERITANCE
print(Emp11.lang)

#HOW TO CHECK SUBCLASS OR SUPERCLASS
print(issubclass(Employee, Programmer))
print(issubclass(Programmer, Employee))

#MAGIC/DUNDER METHOD
print(Emp1 + Emp2) #__add__
print(repr(Emp2)) #__repr__
print(str(Emp1)) #__str__
