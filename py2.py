def name_length(name):
	count= 0
	for i in name:
		count += 1 
	return count

print(name_length("arijit"))	

p = 'arijit'
print(len(p))

from collections import Counter, deque, ChainMap

cou = "google.com"
num_char = Counter(cou)
print(num_char)

def length(str):
	if len(str) <2:
		return ''
	return str[0:2] + str[-2:]

print(length("arijit"))   

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

ch = Counter(p=4,q=2,r=0,s=-2)
print(list(ch.elements()))

ch2 = Counter("www.facebook.com")
print(ch2)
print(list(ch2.most_common(3)))

deq=['a','b','c']
new_deq = deque(deq)
new_deq.append('python')
print(list(new_deq))

deq=['a','b','c']

for elements in deq:
	print(elements)


text = Counter("arijitmondalijklikilsiwiiii")
print("original text: ", text)
print(list(text.most_common(10)))

import re
text="python is the cool program, cool python is the heart of all pythno lover but python had very good syntax"
words = re.findall('\w+', text)
print(Counter(words).most_common(10))

subject = input("enter the subject name ")
marks = input("enter the marks ")

number = ({subject:marks})

print(number)

de = ['arijit','mondal','bobo','gogo']
cc = deque(de)
cc.append('python')
print(cc)
cc.appendleft('java')
print(cc)
cc.pop()
print(cc)
cc.popleft()
print(cc)

cc.reverse()
print(cc)



