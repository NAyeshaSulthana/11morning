 # __init__ --- constructor

 # self -- default argument for every method inside the class.


class Employee:
	def __init__(self,name,company):#(,)-->local
		print(name,company)
obj = Employee("Ramesh","Wipro")#returns helps in passing the values for particular class,it is called constructor


class Employee:
	def __init__(self,name,company): #
		self.name=name#made it global to use in designation(#to use  it  as a local from global)
		self.company=company
		print(name,company)
		#no execution#return name #-- __init__  will not return any value..,return none
	def details(self,designation):
		return "{} works as a {}".format(self.name,designation) 
        #(.,) to use from global and make it local we use (self.)
obj = Employee("Ramesh","Wipro")#returns helps in passing the values for particular class,it is called constructor
print(obj.details("Developer"))    
#no exes#print(Employee.details("Developer"))##it throws error bcoz we cannot access methods of class
#__init__ methods will be called automatially when we create a object.
"""
Ramesh Wipro
Ramesh Wipro
Ramesh works as a Developer
""" 


# Instance Methods--Those methods which takes self as default argument
# and can be accessed only with object..
#ex:--
class Employee:
	def __init__(self,name,company):
		self.name=name
		self.company=company
		print(name,company)

	def details(self,designation):# instance methods
		self.designation=designation#making designation global for below method
		return "{} works as a {}".format(self.name,designation)
	#to use it as new methods follows below	
	def details1(self):# instance methods
		return "{} has 100 {} people".format(self.company,self.designation)
	def data(cls,name,company):
		return "{} works for {}".format(name,company)

obj=Employee("Ramesh","Wipro")
print(obj.details("Developer"))		
print(obj.details1())
print(obj.data("Venkat","Infosys"))
"""
Ramesh Wipro
Ramesh works as a Developer
Wipro has 100 Developer people
Venkat works for Infosys
"""
	
# class Methods-- Those methods which takes cls as default argument and can be 
# accessed with both object and class and which takes @classmethod(decorator)
#ex:--
class Employee:
	def __init__(self,name,company):
		self.name=name
		self.company=company
		print(name,company)

	def details(self,designation):# instance methods
		self.designation=designation#making designation global for below method
		return "{} works as a {}".format(self.name,designation)
	#to use it as new methods follows below	
	def details1(self):# instance methods
		return "{} has 100 {} people".format(self.company,self.designation)
	
	@classmethod
	def data(cls,name,company):
		cls.name=name
		cls.company=company#to use it as global
		return "{} works for {}".format(name,company)
#whatevr values we used back are instance methods as company,self,so we use cls

	@classmethod
	def data1(cls,designation):
		return "{} works as {}".format(cls.name,designation)#cls.name to take local as global 
		#and there also changes in data class name
	
obj=Employee("Ramesh","Wipro")
print(obj.details("Developer"))		
print(obj.details1())
print(obj.data("Venkat","Infosys"))
print(obj.data1("Tester"))
"""
Ramesh Wipro
Ramesh works as a Developer
Wipro has 100 Developer people
Venkat works for Infosys
Venkat works as Tester
"""

# Static Methods--Those methods which will not take any default argument
# and can be accessed with both object and class.
##ex:--
class Employee:
	def __init__(self,name,company):
		self.name=name
		self.company=company
		print(name,company)

	def details(self,designation):# instance methods
		self.designation=designation#making designation global for below method
		return "{} works as a {}".format(self.name,designation)
	#to use it as new methods follows below	
	def details1(self):# instance methods
		return "{} has 100 {} people".format(self.company,self.designation)
	
	@classmethod
	def data(cls,name,company):
		cls.name=name
		cls.company=company#to use it as global
		return "{} works for {}".format(name,company)
#whatevr values we used back are instance methods as company,self,so we use cls

	@classmethod
	def data1(cls,designation):
		return "{} works as {}".format(cls.name,designation)#cls.name to take local as global 
		#and there also changes in data class name
	@staticmethod
	def add_data(name,company):
		return "{} works for {}".format(name,company)
obj=Employee("Ramesh","Wipro")
print(obj.details("Developer"))		
print(obj.details1())
print(obj.data("Venkat","Infosys"))
print(obj.data1("Tester"))
print(obj.add_data("Suresh","IBM"))
print(Employee.add_data("Rajesh","Wellsfargo"))
"""
Ramesh Wipro
Ramesh works as a Developer
Wipro has 100 Developer people
Venkat works for Infosys
Venkat works as Tester
Suresh works for IBM
Rajesh works for Wellsfargo
"""