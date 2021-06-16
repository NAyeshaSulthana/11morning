#OOps--Object Oriented Programmings....

#class-Detailed explanation of an object.
#object-A variables which have permissions to access anything inside the class.


#class---is the keyword for class declaration..

"""
class Classname:
	statements
"""	

#def Employee():
	#name=input("Enter the Employee name:-")
	#company=input("Enter the company name:-")

#Employee()#function call is mandatory for calling function	

class Employee:
	name=input("Enter the Employee name:-")
	company=input("Enter the company name:-")

	def details(self):#self argument defines same class for every method..
		print("{} works for {} company".format(self.name,self.company))
		#to access any varaible outside of that method "self"is used..
		return self.name+self.company

	
	
#using classes method is not called

print(Employee.name)
print(Employee.company)

#print(Employee.details())#Methods inside the class cannot be accessed using classname...

obj=Employee()#it has permission to access anything inside the class..

print(obj.name)
print(obj.company)

print(obj.details())



###############################
"""
COMMAND PROMPT::::::::::::

C:/Users/Vali Basha/Desktop/11morning>python oops.py
Enter the Employee name:-ram
Enter the company name:-wipro
ram
wipro
ram
wipro
ram works for wipro company
ramwipro

"""












