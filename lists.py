##################################2/8######################################################
#Lists--sequence of elements or values which are separated with comma(,)which

#a=[6,7.9,'python']

#a=[6,7.9,'python',[11,12,13]]#nested list

#list are mutuable data types...(changes are possible in the list)

#accessing elements inside the string..(indexing)

a=[2,5.6,'python',11,'django']#indexing will start from zero

print(a[2])
#print(a[4])
#print(a[1])

print(a[1:4])#accessing range/sequence of elements.
#depending on which data type we perform,it returns that data type.

print(a[0:5:2])#slicing***0-5 means performing i.e.,5elements---first to last&2 is slicing

a=[1,2,'python',[11,12,13,14]]#declaring a list inside a list is nested list

print(a[3])#whatever list given list in the input we will get that o/p as single element.

print(a[3][2])#we can access a element inside a list of nested list by initialising indexing..---nested indexing

print(a[2][4])#we can also apply to string as nested indexing to get element.

print(a[-1][-3])#printing in opposite direction.

###2 basic operations---####
###updating----
print(a)#before updating
a[1]=5.6#any data type can be replaced in the list by accessing 
#and at a time its not possible,though we can access it by step by step
#a[1:3]=[12.3,13.3,14.3,15.3]#we can give any no. of elements bcoz it is mutuable
print(a)
#a[3][2]=17
#print(a)#after updating

####deleting-----
#del a[3]
#print(a)#after deleting

###2 basic operations in string--##
#1)concatenation(+)--adding of 2 or more lists..
#2)repetition(*)--repetition elements inside the lists multiple times

#a=[1,2,3,4,5]
#b=[6,7,8,9,0]

#print(a+b)
#print(a*3)

############################################################################5/8####################
#list methods ----(append,extend,insert),remove,pop,clear,count,index,sort,reverse,copy etc.,,
#                 ###adding elements###removing elements##
##############Append---it is a method that adds elements in the list at the ending./it adds one element at a time towards last.
#a=[1,8.7,'python',67,42]

#a.append(100)
#a.append('django')
#a.append([1,2,3])
#print(a)

############Extend-----it is for sequence of elements into the list at the lasr,where extend method will take only sequence data types.
##prints the given extend sequence as single letters.

#a.extend('django')
#print(a)
#a.extend([11,22,33])
#print(a)

##########insert--inserting the element at specific index location.
#a.insert(3,'datascience')
#print(a)

#######remove--removing the specfied element from the list(it removes first prefernce from the left)
#a.remove(8.7)
#print(a)

########pop----for removing the element by index number.
#a.pop(3)
#print(a)

#####clear----remove all the elements and making it as a empty list.
#a.clear()
#print(a)

#a=[1,8.7,'python',67,42,13,8.7,42,13,11,12,13]

##count--returns how many times a particula=r element

#print(a.count(13))

###index--will return the index value of the specified element in the list..from the left..

#print(a.index(12))

###sort--returns the value in the sorted order(defaultly in ascending order)
#a=[45,76,12,89,56,43,87,49]
#a.sort()--for ascending
#a.sort(reverse=True)--for descending

###reverse--
#a.reverse()
#print(a)

###copy--copies the element when we assign & doesnt copy by initiating 'copy'
#a=[3,4,5,6,7,8]

#b=a#--copies the element
#b=a.copy()#doesnot copy the element

#print(a)
#print(b)

#b.append(9)

#print(b)
#print(a)
#print(len(a))


##loopings on list#################################################################6\8####
####
#a=[24,76,79,95,64,12,98,76,123]
#b=[]
#c=[]
#for j in a:
	#if j%2==0:
		#print(j,"is an Even number")
		#b.append(j)
	#else:
		#print(j,"is an Odd number")
		#c.append(j)
#print(b)
#print(c)		
###


###############Task::::a=[45,89,46,87,45,90,32,87,46]#########################
##################removing duplicate values from the list################
a=[45,89,46,87,45,90,32,87,46]
b=[]
for j in a:
	if j not in b:
		b.append(j)
	else:
		pass
print(b)		

##############divide by both 3&4 ##############
#a=[]
#for j in range(0,50):
	#if j%3==0 and j%4==0:
		#a.append(j)
#print(a)

############divide and then multiply condition###########
#a=[]
#for j in range(1,11):
	#if j%3==0:
		#a.append(j*3)
	#else:
		#a.append(j)
#print(a)		

#######list comprehension--this is elevant or faster way of creating a list

#syntax:-
"""
[expression for j in sequence(number,list,range,etc.,)]
"""
##########prints the range from 0 to 10  ##########
a=[j for j in range(0,11)]###to ignore append command from (giving a to append)####
print(a)

#########2 methods of finding even numbers#####
######  1  ####
a=[]
for j in range(0,11):
	if j%2==0:
		a.append(j)
print(a)
######  2  ######
a=[j for j in range(0,11) if j%2==0]
print(a)

a=[j ]
#############2 ways of findng  which is %2 is multiplied by 2#################
################## 1 method ###########
a=[j*2 if j%2==0 else j for j in range(0,11)]
print(a)
################# 2 method ##############
a=[]
for j in range(0,11):
	if j%2==0:
		a.append(j*2)
	else:
		a.append(j)
print(a)
	
##########################################################################################
#######################################################################################
##############PRACTICE#########################	
a=[6,7.9,'python']
a=[6,7.9,'python',[11,12,13]]#nested list
a=[2,5.6,'python',7,'django']
print(a[2])
print(a[4])
#print(a[10])#prints error as out of index range 
print(a[1:4])
print(a[0:5:2])
a=[1,2,'python',[11,12,13,14]]
print(a[3])
print(a[3][2])
print(a[2][4])
print(a[-1][-3])
print(a)
##updating
a[1]=5.6
print(a)
a[1:3]=[12.3,13.3,14.3,15.3]#it replaces 3positions with any number of given values
print(a)
a=[1,2,'python',[11,12,13,14]]
a[3][2]=17
print(a)
#deleting
del a[3]
print(a)
#basic operations
#concatenation
#repitition
a=[1,2,3,4,5]
b=[6,7,8,9,0]
print(a+b)
print(a*5)
print(b*3)
#######list methods
#append
a=[1,8.7,'python',67,42]
a.append(100)
a.append('django')
a.append([1,2,3])
print(a)
#extend
a=[1,8.7,'python',67,42]
a.extend("django")
print(a)
a.extend([11,22,33])
print(a)
#insert
a=[1,8.7,'python',67,42]
a.insert(3,'datascience')
print(a)
#remove
a.remove(8.7)
print(a)
#pop
a.pop(3)
print(a)
#clear
a.clear()
print(a)
#count
a=[1,8.7,'python',67,42,13,8.7,42,13,11,12,13]
print(a.count(13))
#index
print(a.index(13))
####SORTING
a=[45,76,12,89,56,43,87,49]
a.sort()#for ascending
print(a)
a.sort(reverse=True)#for descending
print(a)
#reverse
a=[45,76,12,89,56,43,87,49]
a.reverse()
print(a)
#copy
a=[3,4,5,6,7,8]
b=a
print(a)
b=a.copy()
print(b)
b.append(9)
print(b)
print(a)
print(len(a))
#######looping on list
#printing 2sets of list even and odd
a=[24,76,79,95,64,12,98,76,123]
b=[]
c=[]
for i in a:
	if i%2==0:
		print("i,is an even number")
		b.append(i)
	else:
		print("i,is an odd number")
		c.append(i)
print(b)
print(c)		
###TASK:removing duplicate elements from the list
a=[45,89,46,87,45,90,32,87,46]
b=[]
for i in a:
	if i not in b:
		print("i,is not in a")
		b.append(i)
	else:
		pass
print(b)		
#divide by both 3&4
a=[]
for i in range(0,50):
	if i%3==0 and i%4==0:
		a.append(i)
print(a)		
##divide and then multiply condition
a=[]
for i in range(1,11):
	if i%3==0:
		a.append(i*3)
	else:
		a.append(i)
print(a)		
###list comprehension
"""
[expression for j in sequence(number,list,range,etc.,)]
"""
a=[j for j in range(0,11)]
print(a)
#2 methods of finding even numbers
####1######
a=[]
for i in range(0,11):
	if i%2==0:
		a.append(i)
print(a)
####2####		
a=[i for i in range(0,11) if i%2==0]
print(a)
#2 ways of findng  which is %2 is multiplied by 2
#######1##########
a=[]
for i in range(0,11):
	if i%2==0:
		a.append(i*2)
	else:
		a.append(i)
print(a)
#####2#####
a=[i*2 if i%2==0 else i for i in range(0,11)]
print(a)		




