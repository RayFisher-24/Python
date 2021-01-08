a={4,5,6,8,9,5}
print(a)

b=[1,5,8,96,4,6,1,3,3,23,1]
print(b[1:8])

dict = {'dave':1, 2:'mia'}
print(dict[2])


people = {'employee':{1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}}


#print(people['employee'])
print(people)
print(people.keys())
print(hash(object))

new_dist = {'employee':{1:{'name':'arijit','phone':'9123325003','salary':'2000'},
2:{'name':'mia','phone':'9123355003','salary':'2500'},
3:{'name':'dave','phone':'9144325003','salary':'1000'},
4:{'name':'roishe','phone':'9123325004','salary':'1200'}}}

print(new_dist.values())

print(hash(object))



people1 = {1:{'name':'arijit', 'phone':9123325,'salary':2000},
			2:{'name':'roishe', 'phone':8594325,'salary':1200}}

print(people1[1]['name'])
print(people1[2]['phone'])
print(people1.keys())
print(people1.get(3))
people1[3] = {'name':'modon', 'phone':9123325,'salary':2000}
print(people1[3])
print(people1)
del people1[3]
print(people1)

#for key in people1.get(): print(key)
lis1 = [1,5,6,9,3,2.1]

for i in lis1:
	if i%2 == 0:
		print("happy")
	elif i%2 == 1:
		print("yo")	
	else:
		print("not happy")	

list1 = [1,5,6,3,1,8]
list2 = [5,8,9,5,6,9]

print(list1 is not list2)


x = 2
print(x**4)

s={5,4,5,5,9}
print(type(s))

from collections import namedtuple, Counter
po = namedtuple('po',['x','y'])
p= po(11, y=22)
print(p[0] + p[1])

c= [4,5,6,1,3,1,1,2,2,0,5,9,6,4,8,5,6,4]
print(Counter(c))


x=9

if x%2==0:
	print("morning")
else:
	print("evening")

x=6

if x>5:
	if x%2==0:
		print("even & positive number")
	else:
		print("odd & positive number")	
else:
	print("error number")


x=0
while(x<9):
	print(x)
	x=x+1
print("style")

for i in range(-1,10):
	if i%2==0:
		print("even")
	else:
		print("odd")	

from array import *

a=array('i', [4,8,9,6,7])

print(type(a))
print(a.typecode)

for j in a:
	if j%2!=0:
		print("right")
	else:
		print("wrong")	


b = array('d', [5.1,6.2,8.6,8.7])

print(b)
b.append(5.8)
print(b)
b.pop()
print(b)
print(b.typecode)
print(b.itemsize)
print(b.buffer_info())

print(b[0:2])

for x in b[0:-1]:
	print(x)


def fn1(a):
	total = a+2
	return total

b = fn1(5)
print(b)	

def function1(function):
	def wrapper(*arg, **kwargs):
		print('hello')
		function(*arg, **kwargs)
		print("welcome")
	return wrapper	
@function1
def function2(name):
	print(f"{name}")
function2("arijit")		


def function2(function):
	def rapper(*arg, **kwargs):
		print("hello")
		function(*arg, **kwargs)
		print("welcome")
	return rapper

@function2
def function3(name):
	print(f"{name}")
function3("arijit")	

x= lambda a:a*a
print(x(3))

def new(a):
	return a*a
L = new(3)	
print(L)

lists=[4,8,9,6,4,6,1]
newlist = list(filter(lambda a:(a/3==2),lists))
print(newlist)