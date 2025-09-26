#Code by <\Endless>
#A simple python password generator that utilizes functions, loops(while loop) and inbuilt python modules(random, time & system)

#Modules
import random
import time
import os

#Alphabets list
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rand1 = random.choice(abc)

#Alphabets and numbers variable list
abcnum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rand2 = random.choice(abcnum)

#Alphabets, numbers & special characters list
special = "!@#$%&*-_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rand3 = random.choice(special)

#Generated password
password = []


#Function for clearing a previous output
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


#Password generator starts here
def intro():
	print("----- Password Generator -----\n\n1. Abc only\n2. Abc & num\n3. Abc, num and symbols\n")
	passtype = input("Choose a password type (1-3) : ")
	try:
		#Password type contains ABC only
		if int(passtype) == 1:
			clear()
			def intro1():
				gen = 0
				password = []
				x = input("----- Password Generator -----\n\nEnter your desired password length : ")
				try:
					user = int(x)
					while gen < int(x):
						rand1 = random.choice(abc)
						password.append(rand1)
						gen += 1
					print("\n" + "".join(password) + "\n")
					#Generate another password(rerun)
					rerun = input("Enter 'p' to generate another password : ")
					if rerun.lower() == "p":
						clear()
						intro()
					else:
						exit()
				#Invalid input for password length
				except ValueError:
					print("\n❌ Invalid input")
					time.sleep(1)
					clear()
					intro1()
			intro1()
		#Password type contains ABC and num 
		elif int(passtype) == 2:
			clear()
			def intro2():
				gen = 0
				pasdword = []
				x = input("----- Password Generator -----\n\nEnter your desired password length : ")
				try:
					user = int(x)
					while gen < int(x):
						rand2 = random.choice(abcnum)
						password.append(rand2)
						gen += 1
					print("\n" + "".join(password) + "\n")
					#Generate another password(rerun)
					rerun = input("Enter 'p' to generate another password : ")
					if rerun.lower() == "p":
						clear()
						intro()
					else:
						exit()
				#Invalid input for password length
				except ValueError:
					print("\n❌ Invalid input")
					time.sleep(1)
					clear()
					intro2()
			intro2()
		#Password type contains ABC, num & special characters
		elif int(passtype) == 3:
			clear()
			def intro3():
				gen = 0
				password = []
				x = input("----- Password Generator -----\n\nEnter your desired password length : ")
				try:
					user = int(x)
					while gen < int(x):
						rand3 = random.choice(special)
						password.append(rand3)
						gen += 1
					print("\n" + "".join(password) + "\n\n")
					#Generate another password(rerun)
					rerun = input("Enter 'p' to generate another password : ")
					if rerun.lower() == "p":
						clear()
						intro()
					else:
						exit()
				#Invalid input for password length
				except ValueError:
					print("\n❌ Invalid input")
					time.sleep(1)
					clear()
					intro3()
			intro3()
		#Invalid password type selection
		elif int(passtype) != 1 or 2 or 3:
			print("\n❌ Invalid input")
			time.sleep(1)
			clear()
			intro()
	except ValueError:
		print("\n❌ Invalid input")
		time.sleep(1)
		clear()
		intro()
intro()