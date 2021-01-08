
#ATM MACHINE WORKFLOW
restart = ('Y')
chances = 3
balance = 1000

while chances >=0:
	pin = int(input("Enter the 4 digit pin "))
	if pin == (1234):
		print('you enter a correct pin \n')
		while restart not in ('no','n','N','NO'):
			print("please press 1 for your balance \n")
			print("please press 2 for your withdrawl \n")
			print("please press 3 for your pay in \n")
			print("please press 4 for your Return card \n")
			option = int(input("Choose one at up "))
			if option == 1:
				print("your balance is ", balance, "\n")
				restart = input('would you to go back at main page? ')
				if restart in ('n','no','NO','N'):
					print('Thank you to banking with us')
					break
			elif option == 2:
				#option2 =('y')
				withdrawl = float(input("How much money you withdrawl? "))
				if withdrawl in range(1000):
					balance = balance - withdrawl
					print('\n balance is now', balance)
					restart = input("would you to go back at main page? ")
					if restart in ('n','no','N','NO'):
						print('Thank to banking with us')
						break
				elif withdrawl != range(1000):
					print("Invaild amount re-try again \n")
					restart = ('y')	
			elif option == 3:
				pay_in = float(input('How much would you pay? '))
				balance = balance + pay_in
				print("current balance of you account", balance)	
				restart = input("would you to go back at main page? ")
				if restart in ('n','no','N','NO'):
					print('Thank you to banking with us')
					break
			elif option==4:
				print('please wait for card come outside')
				print('Thank you to banking with us')
				break
			else:
				print('please enter right number. \n')
				restart = ('y')
				break 
	elif pin != (1234):
		print("incorrect")
		chances= chances-1
		if chances==0:
			print('try after some time')
			break								

#GENARATE PASSWORD
import string
import random

if __name__ == '__main__':
	s1 = string.ascii_lowercase
	s2 = string.ascii_uppercase
	s3 = string.digits
	s4 = string.punctuation

	plen = int(input("Enter your password digits \n"))

	s = []
	s.extend(list(s1))
	s.extend(list(s2))
	s.extend(list(s3))
	s.extend(list(s4))
	random.shuffle(s)
	print(''.join(s[0:plen]))

#DATE AND TIME USING .FORMAT METHOD
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{0:%Y-%m-%d %H:%M:%S}'.format(d))

#NOTIFICATION TIMMER 
import time
#from plyer import notification

while True:

	notification.notify(
		title = 'hey',
		message = 'good noon' ,
		timeout = 10
	)	
	time.sleep(60*60)

#CURRENCY COVENTOR
with open('new.txt') as a:
	lines = a.readlines()

currency = {}
for line in lines:
	parsed = line.split("\t")
	currency[parsed[0]] = parsed[1]

amount = int(input("enter the currency"))
print("Enter the currency")
[print(item) for item in currency.keys()]
curren= input("please")
print(f"{amount} to {amount * float(currency[curren])} {curren}")	

#FACTORIAL NUMBER
def factorial(number):
	if number == 0 or number==1:
		return 1
	else:
		return number * factorial(number-1)	

def factorialTrailingZeros(number):
	count=0
	i=5
	while(number//i != 0):
		count += int(number/i)
		i = i*5
	return count	
if __name__ == '__main__':
		number = int(input("Enter the factorial "))
		fac = factorial(number)
		print(f"The factorial is {fac}")
		print(factorialTrailingZeros(number))	


#SHOP CALCULATER
sum = 0
while(True):
	price = input("Enter the price ")
	if price != 'q':
	 	sum = sum + int(price)
	 	print(f"Total price is {sum}")

	else:
		print(f" You total price is {sum} \n")
		print("Thank you to shopping with us")
		break

#ATM MACHINE WORKFLOW
restart = ('Y')
chances = 3
balance = 1000

while chances >=0:
	pin = int(input("Enter the 4 digit pin "))
	if pin == (1234):
		print('you enter a correct pin \n')
		while restart not in ('no','n','N','NO'):
			print("please press 1 for your balance \n")
			print("please press 2 for your withdrawl \n")
			print("please press 3 for your pay in \n")
			print("please press 4 for your Return card \n")
			option = int(input("Choose one at up "))
			if option == 1:
				print("your balance is ", balance, "\n")
				restart = input('would you to go back at main page? ')
				if restart in ('n','no','NO','N'):
					print('Thank you to banking with us')
					break
			elif option == 2:
				#option2 =('y')
				withdrawl = float(input("How much money you withdrawl? "))
				if withdrawl in range(1000):
					balance = balance - withdrawl
					print('\n balance is now', balance)
					restart = input("would you to go back at main page? ")
					if restart in ('n','no','N','NO'):
						print('Thank to banking with us')
						break
				elif withdrawl != range(1000):
					print("Invaild amount re-try again \n")
					restart = ('y')	
			elif option == 3:
				pay_in = float(input('How much would you pay? '))
				balance = balance + pay_in
				print("current balance of you account", balance)	
				restart = input("would you to go back at main page? ")
				if restart in ('n','no','N','NO'):
					print('Thank you to banking with us')
					break
			elif option==4:
				print('please wait for card come outside')
				print('Thank you to banking with us')
				break
			else:
				print('please enter right number. \n')
				restart = ('y')
				break 
	elif pin != (1234):
		print("incorrect")
		chances= chances-1
		if chances==0:
			print('try after some time')
			break								

#FACTORIAL NUMBER			
num = int(input("Enter your factorial value: "))

factorial = 1
if num<0:
	print("nagetive value is not applicable")
elif num == 0:		
	print("o factorial is 1")
else:
	for i in range(1, num+1):
		factorial = factorial * i
	print(factorial)

#SIDE CALCULATION
from math import sqrt

choose_side = input("choose the side a, b, c ")

if choose_side == 'c':
	side_a = int(input("Enter the value of side a "))
	side_b = int(input("Enter the vslue of side b "))
	side_c = sqrt(side_a**2 + side_b**2)
	print(side_c)

elif choose_side == 'a':
	side_c = int(input("Enter the value of side c "))
	side_b = int(input("Enter the vslue of side b "))
	side_a = sqrt((side_c*side_c) - (side_b*side_b))
	print(side_a)

elif choose_side == 'a':
	side_c = int(input("Enter the value of side c "))
	side_a = int(input("Enter the vslue of side a "))
	side_b = sqrt((side_c*side_c) - (side_a*side_a))	
	print(side_b)

else:
	print("please choose a right side along to a, b, c")	
