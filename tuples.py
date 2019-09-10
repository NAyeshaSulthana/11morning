#####Tuples:--sequence of elements separated with comma which are declared inside()...

a=(1,2,3,4)

print(type(a))

a=1,2,3,4,5#() is recommended but not mandatory&by declaring , between them defaults takes tuple

print(type(a))

a=(1)
print(type(a))

a=1
print(type(a))

a=(1,)#way of declaring single value tuple
print(type(a))
#tuples are immutable...(we cannot make changes)

##########accessing elements inside the tuple..(indexing##########
a=(1,11,54,'datascience','devops','cricket',[23,24,25])
print(a[4])
print(a[1:6])
print(a[0:7:2])#slicing
print(a[-3])

#a[0]=13,#assigng element give error as it is not possiblee
#del a[1],deleting is not possible in tuples...

##########Basic operations on tuples#######################
  ###1##concatenation(+):-adding 2 or more tuples..
  ###2##repetition(*):-repeating same element multiple no.of times...

print((1,2,3,4)+(3,4,5,6) )
print((1,2,3,)*4)
#as tupples are immutables there are no methods to make changes like pop,etc.,
a=(3,4.5,6,7.1,3,6,8,9,0)
#print(a.count(3))
print(a.index(7.1))# finding index
print(a[0])#finding index value
print(len(a))

#######  TASK:removing duplicates from the last ######
a=[3,4.5,6,7.1,3,6,8,9,0]
b=[]
for j in a:
	if j not in b:
		b.append(j)
	else:
		pass
print(b)	

###task:range(0,21)
b=()
c=()
print(b)#(0,2,4,6,8,10,12,14,16,18,20)
print(c)#(1,3,5,7,9,11,13,15,17,19)
########
#a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]#using list
b=[]
c=[]
for j in range(0,21):
	if j%2==0:
		b.append(j)
	else:
		c.append(j)
print(b)
print(c)		

####task:powers--formatting & R-strip
