###########################functions-1#########333
#Functions---set of statements inside a block which will be executed repeatedly.
#Main feature of functions is code reusability..


a=45
b=65

print(a+b)
print(a-b)
print(a*b)

a=34
b=75

print(a+b)
print(a-b)
print(a*b)


#def---it is the keyword for defining a function..
"""
def function-name():
	statements
"""

def data(a,b):#a,b are called arguments..
	print(a+b)
	print(a-b)
	print(a*b)
data(45,65)#function calling
data(2,3)#function calling

#function call is mandatory to execute a statement inside the function....
#different ways of passing arguments to the function--

##1)postional Arguments
##2)Default
##3)Keyword
##4)Arbitary positional
##5)Arbitary keyword

######1)Positional Arguments-the value assignment to the arguments will be based on the position########
def details(name,city):
	print("{} has come from {} city".format(name,city))
print("Hi Hello")
details("Rama","Punjab")
details("punjab","Rama")#it takes postions,no the correct format,declarations should be given right..	


#######2)Default Arguments-passing a default value  to the function at the functions declaration
def details(name,city="HYD"):
	print("{} has come from {} city".format(name,city))
print("Hi Hello")
details("Rama","vizag")
details("venkat")

######3)Keyword Arguments-declaring the values at the function call using key-name..
def details(name,city,state):
	print("{} has come from {} city in {} state".format(name,city,state))
details("rama","hyd","A.P")
details(city="hyd",state="A.P",name="siri")
details("Raki",state="A.P",city="hyd")#atleast two values are to be declared for taking empty declared value 
                                     # which is not assigned....
#details(name="Venkat","vizag",state="Andhra")#once a keyword argument is declared after that whatever you 
 #it throws error....                                               #declare should be keyword                                

##################Functions-2#################

 ####4)Arbitary Positional Arguments-

 # *arg--for declaring multiple arguments
def add(*a):
	print(type(a))
	count=0            
	for j in a:
		print(count)   #0 #3 #7
		count=count+j
		print(count)   #3 #7 #12
 	#print(a)
 	#print(sum(a))

#add(2,3)
add(3,4,5)
#add(4,5,6,7)	

def add(*a):
	print(type(a))
	count=0            
	for j in a:   
		count=count+j
		print(count)   
 	#print(a)
 	#print(sum(a))

add(2,3)
add(3,4,5)
add(4,5,6,7)

#####5)Arbitary Arguuments--for declaring multiple keyword arguments..

def add(**a):
	print(a)
	count=0
	for j in a:
		#print(j,"value is:-",a[j])
		count=count+a[j]
	print(count)	
		#print(a[j])

print(add(a=4,b=5,c=6))	
add(d=7,e=8,f=9,g=1)
#add(h=8,i=9,j=10,k=12,l=11)

#a={'city':'hyderabad','state':'A.P'}
#print(a['state'])
 

#return--it will store the value instead of printing and send it to where functions is called..
#once a return is reached inside the function after that no statement will be executed...

def data(a,b):
	print(a+b)#9
	return (a+b)*b#45
	#print("Hyderabad")#it will not print as return is last statement in the function
print(data(4,5))	#9
#data(4,5)	

def sub(c):
	return data(4,5)-c#45-3
print(sub(3))	#42

###########Functions-3##########

###Local  and Global variables-
#Global-variables declared outside of all the functions and can be accesed anywhere throughout the function
#Local-those which we declare inside the functions and can accessed only inside the functions itself.. 

a=32
b=56
def add(c):#inside it is possible to declare
	print(a)
	print(b)
	print(c)
	return a+b+c
print(add(7))	
#print(c)#it throws error,its not possible to print the variable
print(a)
print(b)

##Recursion:-A functions which calls same functions again and again...

#n!==n*(n-1)!
#6!==6*5!
     #6*(5*4!)
     #6*5*(4*3!)
     #6*5*4*(3*2!)
     #6*5*4*3*(2*1!)
     #6*5*4*3*2*1

def cal_fact(a):
	if a==1:
		return 1#if false else iteration used
	else:
	    return a*cal_fact(a-1)
print(cal_fact(7))
#6*5*4*3*2*1	    

##################################################
###################################################
######################################################
##############PRACTISE##############################
############FUNCTIONS##################
a=45
b=65
print(a+b)
print(a-b)
print(a*b)

a=34
b=75
print(a+b)
print(a-b)
print(a*b)

#def---it is the keyword for defining a function..
"""
def function-name():
	statements
"""
def data(a,b):#a,b arguments
	print(a+b)
	print(a-b)
	print(a*b)
data(45,65)#function calling
data(34,75)	

#DIFFERENT WAY OF PASSING ARGUMENTS
##1)postional Arguments
##2)Default
##3)Keyword
##4)Arbitary positional
##5)Arbitary keyword

####1.POSTIONAL ARGUMENTS
def details(name,city):
	print("{} has come from {} city".format(name,city))
print("HI Hello")
details("Rama","Punjab")
details("Punjab","Rama")#declaration given it takes,we should give a/c to format

#########2.DEFAULT ARGUMENTS
def details(name,city="HYD"):
	print("{} has come from {} city".format(name,city))
print("HI Hello")
details("Rama","Vizag")
details("Venkat")#2nd arguments missing takes from deafult argumnt

############3.KEYWORD ARGUMENTS
def details(name,city,state):
	print("{} has come from {} city in {} state".format(name,city,state))
print("HI Hello")
details("Rama","hyd","A.P")
details(city="hyd",state="A.P",name="Siri")#indictaing format values in unordered 
details("Raju",city="hyd",state="A.P")#atleat 2 arguments should given
#details(name="Venkat","vizag",state="Andhra")#error#1st key word declared,so next should

###4.ARBITARY POSITIONAL
def add(*a):
	print(type(a))
	count=0
	for j in a:
		print(count)
		count=count+j
		print(count)
	print(a)	
	print(sum(a))
add(3,4,5)		
add(2,3)
add(4,5,6,7)

##another
def add(*a):
	print(type(a))
	count=0
	for j in a:
		count=count+j
		print(count)
add(3,4,5)
add(2,3)
add(4,5,6,7)

##5.ARBITARY ARGUMENTS
def add(**a):
	print(a)#prints sequence given in function
	count=0
	for j in a:
		count=count+a[j]
	print(count)#prints count
print(add(a=4,b=5,c=6))#none for print
add(d=7,e=8,f=9,h=1)		
add(h=8,i=9,j=10,k=12,l=11)

a={'city':'hyderabad','state':'A.P'}
print(a['state'])
 
##return-after return is in the block,next one is ignored
def add(a,b):
	print(a+b)
	return(a+b)*b
	print("HYderabad")
print(add(4,5))
#add(4,5)

def sub(c):
	return data(4,5)#-c(-1 as sub)
print(sub(3))	#None 

#######LOCAL AND GLOBAL VARIABLES
a=32
b=56
def add(c):
	print(a)
	print(b)
	print(c)
	return a+b+c
print(add(7))#irs must for return value resulting and missing intitaions takes here
#print(c)#erroe as no c value
print(a)
print(b)	

###RECURSION
def cal_fact(a):
	if a==1:
		return 1
	else:
		return a*cal_fact(a-1)
#print(cal_fact(7))#5040
print(cal_fact(6))	#720	
###########################################################################################################################

#Lambda Functions or Anonymous Functions:-A Function which does not have any name.....like add,sub,cal etc.,
#lambda is the keyword for defining lambda function...

#lambda argument:expression

def sample(a):
	return a*2
print(sample(6))#12
print(sample(8))#16	
#print((lambda a,b:a*b)(6,8))#48

#print(sample(6))#12	
#(lambda a:a*2)(6)#returns empty

#single line of using lambda....
#print((lambda a,b:a*b)(6,8))#48

#map--which perform iteration or loopings on the sequence..
#filter--which perform iteration and conditionals on a sequence...
a=[54,75,92,53,65,21,74,98]

b=[]
def sample(a):
	print(a)
sample(a)	
#implement above code by multiplying each with 2
a=[54,75,92,53,65,21,74,98]

b=[]
def sample(a):
	for j in a:
		b.append(j*2)
	
sample(a)
print(b)#[108, 150, 184, 106, 130, 42, 148, 196]

print((lambda j:j*2,a))#(<function <lambda> at 0x0000012F8AEB08B8>, [54, 75, 92, 53, 65, 21, 74, 98])#shwng function
print(map(lambda j:j*2,a))#<map object at 0x000002ACEBE81348>#showing map
print(list(map(lambda j:j*2,a)))#[108, 150, 184, 106, 130, 42, 148, 196]#showing list[]
print(tuple(map(lambda j:j*2,a)))#[108, 150, 184, 106, 130, 42, 148, 196]#showing tuple()
print(tuple(filter(lambda j:j%2==0,a)))#54,92,74,98
print(tuple(map(lambda i:i*2,(tuple(filter(lambda j:j%2==0,a))))))#(108, 184, 148, 196)

##############################################
##############################################
###############################################
##############PRACTICE###########################
def sample(a):
	return a*2
print(sample(6))	
print(sample(8))

((lambda a:a*2)(6))#empty
print((lambda a:a*2)(6))
print((lambda a,b:a*b)(6,8))#single line of using lambda

#map
#filter
a=[54,75,92,53,65,21,74,98]
b=[]
def sample(a):
	print(a)
sample(a)#passing  to print

#multiply with 2
a=[54,75,92,53,65,21,74,98]
b=[]
def sample(a):
	for j in a:
		b.append(j*2)
sample(a)
print(b)

print((lambda j:j*2,a))
print(map(lambda j:j*2,a))
print(tuple(map(lambda j:j*2,a)))
print(list(map(lambda j:j*2,a)))
print(tuple(filter(lambda j:j%2==0,a)))
print(tuple(map(lambda i:i*2,tuple(filter(lambda j:j%2==0,a)))))


