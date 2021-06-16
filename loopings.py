#looping--executing the statement multiple number of times.

#while loop
#for loop

#while loop
"""
while condition:
	statements
	"""

#a=int(input("enter a value:-"))

#while a<30:
	#if a%3==0:
		#print(a,"value is lessthan 30!")
	#a=a+1

#################################################6 data types in python##############################################33
# #############1)numbers(int,flaot,complex)--(a+jb)######################################
#there is default value of j i.e.,j2=-1
#a=3+4j
#print(a)
#print(type(a))

#b=complex(3,4)

#print(b)

#c=complex(3)

#print(c)
#d=13.456789023412345678901234567890
#print(d)#print upto 15locations after decimal value

###################2)strings--sequence of anything declared inside ' ' or " " or """ """(most important data type)###############
#a="qwrtyuisoapfgdhjsk2324567890!@#$%^&*("#anything u declare in quotation can be displyed samez
#print(a)

#b='qwer234!@#$'
#print(b)

#c="""hyd 
#bang 
#knl 
#4321
# ***$$$##"""#""" """-writes multiple lines
#print(c)

#d="twink' twinkle"#opsta-p prints in only(" ")
#print(d)

###############3)lists-sequence of values or elements which are separated with comma(,)which are declared inside[ ] ##################
#d=[23,45,67,"hyd","bang"]#declared with " "
#print(d)
################4)tuples-sequence of value or elements which are separated with comma(,)which are separated inside{ }##############
#d={23,45,67,"hyd","bang"}#declared with " "
#print(d)

################5)dictionary-sequence of key:values pair which are separated with comma(,)which are declared inside{ }################
#d={'city':'hyd','state':['Andhra','Telangana']}#' 'are used to declare
#print(d)
####################6)sets-sequences of values or elements which are separated with comma(,)which are declared inside{ }##############
#the duplicates of strings are removed
#d={2,3,4,5,2}
#print(d)

##################################FOR LOOP###########################

#for loop will work only on the sequences data type only..
"""
for element in sequence:
	statements
"""

#a="python programming"
#for j in a:
	#print(j)
	#print(j,end=" ")#the initiated 'a' will prints single letter in each line bcoz of looping repeatedly

#a=[23,56,78,'python','hyderabad']	
#for j in a:
	#print(j,end=" ")

#################range:::##############

a=range(15)

#for j in a:
	#print(j,end="-")#it prints upto 15-1=14

#for j in range(10,30):#prints from 10 t0 30-1
		#print(j,end=" ")

#for j in range(10,30,3):#increment with 3 from 10 to 30
	#print(j)

#without specifyng 3rd argument,then it will not work
for j in range(34,10,-1):
	print(j)


########################################################
#####################################################
#################################################
##############3PRACTICE####################
#while
#for
"""
while condition:
	statement
	"""
"""
a=int(input("enter a value:"))
while a<30:
	if a%3==0:
		print(a,"value is less than 30")
	a+=1	
"""
#6datatypes in python
#1#################numbers(int,float,complex)	
#default value j i.e.,j2=-1
a=3+4j
print(a)
print(type(a))

b=complex(3,4)
print(b)

c=complex(3)
print(c)

d=13.8765313579800765432234
print(d)#print 15positions
print(type(d))

#2######strings
a="asdfghjklwertyuiopzxcvbnm,1234567890-!@#$%^&*()"
print(a)
print(type(a))

b='asd1234!@#$'
print(b)
print(type(b))

c="""hyd
bang
knl
asd
123
!@#$%^&*"""
print(c)
print(type(c))

d="twink' twinkle"#opsta-p prints in only(" ")
print(d)

##3##LISTS###############
d=[23,45,67,"hyd","bang"]#declared with " "
print(d)
print(type(d))

##4##tuples
d=(23,45,67,"hyd","bang")#declared with " "
print(d)
print(type(d))

##5##dictionary
d={'city':'hyd','state':['Andhra','Telangana']}#' 'are used to declare
print(d)
print(type(d))

##6##set
d={2,3,4,5,2}
print(d)
print(type(d))

##############FOR loop#################
"""
for element in sequence:
	statement
	"""
"""
a="python programming"
for j in a:
	print(j)
	print(j,end=" ")	
"""
a=range(15)
for j in a:
	print(j,end="-")

for j in range(10,30):
	print(j,end="")

for j in range(10,30,3):
	print(j)

for j in range(34,10,-1):#reverse order
	print(j)




