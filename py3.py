from collections import *
import re


a=[1,2,4,3,1,2,3,2,4,5,5]
b=deque(a)
print(b.count(3))

c=Counter(a)
print(list(c.elements()))

for i in c.elements():
	print(i)

d = "text"
e=Counter(d)
print(list(e.most_common(10)))

f = [2,3,4]
g=deque(f)
print(g)
g.append(3)
print(g)

word ="the rhe fhty fkk"
text = re.findall('\w+', word)
print(Counter(text).most_common(10))

str ="+++pythonworld+++"
str.strip()
print(str)

dlo= [1,2,3,2,1,2,3,1,2,3,1]
f=Counter(dlo)
print(f.most_common(1))


d = 'Arijit Mondal'

ro = deque(d)
ro.rotate()
print(ro)

d= {'a':'arijit'}
b= {'r':'rose'}

chain = ChainMap(d,b)
print(chain)