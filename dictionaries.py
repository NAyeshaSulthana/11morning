# #Dictionaries:--sequence of key:values pair separated with comma(,) 
#which are declared inside{}

# a={'trophy':'IPL','teams':['csk','rcb','mi','kkr'],'captains':['dhoni','virat','rohit','karthik']}
# # print(type(a))#returns <class 'dict'>
# # print(a)
# # #####a={'trophy':'IPL',1/(1,2,3)/{1,2,3}:['csk','rcb','mi','kkr'],'captains':['dhoni','virat','rohit','karthik']}#########3
# # ###print(type(a))#returns <class 'dict'>##bcoz string,set are immutuable.[1,2,3]are lists which are mutuable,so it returns error

# # #dictionaries are mutuable#adding or removing key:values is possible in dictionaries.
# #   #but keys should be imutuable(channot be change but key is added) only.
# # #########################################################################################
# # ## Accessing key-values in the dictionary...
# # print(a['teams'])#returns values of the key,which we associated,.,,,...

# # ##get--for getting the values associated with the key if key is present.
# # #it will return none by default is key is not present
# # print(a.get('captains'))#returns value as above
# # #############
# # #print(a['captain'])#return keyerror by basic method.
# # print(a.get('captain'))#return none by get method.
# # ##########################################################################################
# # a['trophy']="BBL"
# # print(a)#updates key value.,

# # a['trophies']=['IPL','BBL','PPL']#added as another key:value pair
# # print(a)

# # #if the key already presennt in the dictionary value associated with key will be updated.
# # #if the key not present in the dictionary the key and value pair will be added as new key:value
# # a['trophies'][0]="SPL"
# # print(a)

# # #print(dir(dict))
# # ########update---for adding new key:value pairs to dictionary..
# # a.update({1:11,2:22,3:33})
# # print(a)# new key:value pairs are added at the last.


# # deletion methods

# # print(dir(dict))


# a={'trophy':'IPL','teams':['csk','rcb','mi','kkr'],'captains':['dhoni','virat','rohit','karthik']}

# # del a['trophy']

# print(a)


# # pop -- it will remove the key:value pair based on the the key given and also it can return the value removed as well.

# # print(a.pop('trophy'))

# # print(a)

# # popitem()--

# # print(a.popitem()) #-- popitem will not accept any arguments but will deleted the last key:value pair in the dictionary.. 


# # print(a)

# # clear -- which will remove all the key:value pairs and make it as an empty dictionary..


# # a.clear()


# # print(a)


# # keys -- 

# # print(a.keys())  # will return all the keys in the dictionary in list format..

# # print(a.values()) # will return all the values in the dictionary in list format..

# # print(a.items()) # will return each (key,value) pair in the dictionary as a list..


# # copy -- will take values as the reference and will create a new memory allocation with same values..
# # a={1:11,2:22,3:33}

# # b=a # memory allocation is taken into consideration..

# # b=a.copy()

# # print(id(a))
# # print(id(b))


# # b['city']="hyderabad"

# # print(a)

# # print(b)


# # fromkeys() -- will create a dictinary based on the sequence given 
#in the fromkeys methods which will take None as default if you 
# # not provide the 2nd argument..

# # b=[2,3,4,5,6]

# # print({}.fromkeys(b,55))

# a={1:'python',2:'datascience',3:'devops',4:'fullstack'}

# # a=[1,2,3,4,5]
# # print(a[3])
# # for j in a:
# # 	# print(j)
# # 	print(a[j])


# # print(4 in a.keys())

# for j in a:
# 	if j==4:
# 		print("key present")
# #		print(a[j])

# ######################################12 august#############################3
# #Dictionary comprehension---

# #syntax:-

#  #{expression for element in sequence}

# #normal way of writing
# # b={}
# # for j in range(1,6):
# # 	b[j]=j**j
# # 	#print(j)
# # print(b)

# # b={}
# # for j in range(1,10):
# # 	if j%2==0:
# # 		b[j]=j**2
# # 	else:
# # 		b[j]=j**3
# # 	#print(j)
# # print(b)

# # #dictionary comprehension of writing
# # print({j:j**j for j in range(1,6)})

# print({j:j**2 if j%2==0 else j**3 for j in range(1,10)})






# #gsanjeevreddy91@gmail.com
"""
a={}
for j in range(1,5):
	name=input("enter name:")
	dob=input("enter dob:")
	if name in a:
		a[name]=[name]+[dob]	
	else:
		pass
print(a)		
	"""	
####################################
#####################################
##################################
#####PRACTICE#################
a={
'trophy':'IPL',
'teams':['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
print(a)
print(type(a))
"""
a={
'trophy':'IPL',
1/(1,2,3)/(1,2,3):['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
print(type(a))
"""
#access
print(a["teams"])
print(a["captains"])
#get
print(a.get("teams"))
print(a.get("captains"))

#update key
a["trophy"]="BBL"
print(a)

#adds key:value pairs
a['trophies']=['IPL','BBL','PPL']
print(a)

#key already,key updates
a['trophies'][0]=["SPL"]
print(a)

print(dir(dict))

#update
a.update({1:11,2:22,3:33})
print(a)

#deletion
a={
'trophy':'IPL',
'teams':['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
del a['trophy']
print(a)

#pop
a={
'trophy':'IPL',
'teams':['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
print(a.pop('trophy'))
print(a)

#popitem-random item pops
a={
'trophy':'IPL',
'teams':['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
print(a.popitem())
print(a)#lastitem
#clear
#print(a.clear())#None
a.clear()
print(a)#empty dictionary

#keys,values,items
a={
'trophy':'IPL',
'teams':['csk','rcb','mi','kkr'],
'captains':['dhoni','virat','rohit','karthik']
}
print(a.keys())
print(a.values())
print(a.items())

#copy
a={1:11,2:22,3:33}
b=a
print(b)
#anotherway
b=a.copy()
print(b)
print(id(a))
print(id(b))
#update new pair
b['city']="hyderabad"
print(a)
print(b)

#fromkeys
b={1,2,3,4,5}
print({}.fromkeys(b,55))#b is key,and given single values allocates to all 

a={1:'python',2:'datascience',3:'devops',4:'fullstack'}
print(a[3])#3rd item

a=[1,2,3,4,5]
for j in a:
	print(j)
	
a={1:'python',2:'datascience',3:'devops',4:'fullstack'}
for j in a:
	print(a[j])
#1	
print(4 in a.keys())
#2
for j in a:
	if j==4:
		print("KEY PRESENT")
		print(a[j])

##syntax
#{expression for element in sequence}	
#normalway
b={}
for j in range(1,6):
	b[j]=j**j
	print(j)
print(b)	
##
b={}
for j in range(1,10):
	if j%2==0:
		b[j]=j**2
		#print(j)	
	else:
		b[j]=j**3
		#print(j)
print(b)		

###dictionary comprehension
print({j:j**j for j in range(1,10)})
print({j**2 if j%2==0 else j**3 for j in range(1,10)})

###########################
#########################
"""
a={}
for j in range(1,5):
	name=input("enter name:")
	dob=input("enter dob: ")
	if name in a:
		a[name]=[name]+[dob]
	else:
		a[name]=a[name]
print(a)		
"""

	




