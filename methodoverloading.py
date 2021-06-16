# methodoverloading--Python doesnot support the type of Overloading...


# class sample:

# 	def addition(self,a,b):
# 		return a+b

# 	def addition(self,a,b,c):
# 		return a+b+c

# obj=sample()
# print(obj.addition(3,4,5))	#the latest assigned call is considered...

# print(obj.addition(3,4))#addition() missing 1 required positional argument: 'c'
#the assiging former than the later is not considered



#Datahiding or Encapsulation(binding or restrictions)-----Restricting the access to the variables
    #or methodsoutside the class....

# class sample:
# 	name="Ramesh"#those attributes/variables we can access anywhere/outside---public attributes

# 	def details(self,city):#public methods
# 		return "{} came from {} city".format(self.name,city)

# obj=sample()
# print(obj.name)
# print(obj.details("Hyderabad"))		
################
# class sample:
# 	__name="Ramesh"#those attributes/variables with __---private attributes

# 	def details(self,city):#public methods
# 		return "{} came from {} city".format(self.__name,city)

# obj=sample()

# print(obj.details("Hyderabad"))	
#######

# class sample:
# 	__name="Ramesh"#those we can access with __---private attributes

# 	def __details(self,city):#private methods
# 		return "{} came from {} city".format(self.__name,city)

# obj=sample()
# print(obj._sample__name)
# print(obj._sample__details("Hyderabad"))
#syntax::print(objectname._classname__attributename)	
#for certain variables ,we are hiding the data--called datahiding....

#Eventhough MO it cannot achieve,we can achieve through functions with multiple positional arguments....

class sample:

	def addition(self,*a):
		#print(a)
		count=0
		for i in a:
			count=count+i
		print(count)

obj=sample()
print(obj.addition(3,4,5))#to n number of values we can add...
print(obj.addition(2,3))
#By default python doesnot support method overloading...but by using smaller functions we can do it...

