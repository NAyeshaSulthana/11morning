#inheritance:----a class getting properties from other classes..

#single inheritance:-At a time getting the properties fron single class 
#Multiple inheritance:-at a time getting the properties from multiple classes
#Multilevel inheritance--a class getting the properties from its parent class and again that parent
# has a grand parent class.so,child can get properties fron grandparent as well

################Single inheritance############
class Parent:
	name="Ramesh"
	city="Hyd"

	def address(self):
		return "{} is from {}".format(self.name,self.city)

obj=Parent()
print(obj.address())


class child(Parent):
	name="Suresh"
	city="Hyd"

	def address(self):
		return "{} came from {}".format(self.name,self.city)

obj=child()

print(obj.address())


#############Multiple inheritance###############
class First:
	course="Python" #Python future of IT industry

	def course_details(self):
		return "{} is trending".format(self.course)

class Second:
	course="Django" #Django future of IT industry

	def course_details(self):
		return "{} is a framework".format(self.course)		

class Third(First,Second):
	course="Datascience" #Datascience future of IT industry

	def course_details(self):
		return "{} future of IT industry".format(self.course)

obj=First()
print(obj.course)
print(obj.course_details())	

obj=Second()
print(obj.course)#print all cas
print(obj.course_details())	

obj=Third()
print(obj.course)#print all cases...
print(obj.course_details())	

#################Multilevel inheritance################
class First:
	course="Python" #Python future of IT industry

	def course_details(self):
		return "{} is trending".format(self.course)

class Second(First):
	course="Django" #Django future of IT industry

	def course_details(self):
		return "{} is a framework".format(self.course)		

class Third(Second):
	pass

	course="Datastuctures" #Datastructures future of IT industry

	def course_details(self):
		return "{} future of IT industry".format(self.course)
obj=Third()
print(obj.course)#print all cases...
print(obj.course_details())	

"""
Ramesh is from Hyd
Suresh came from Hyd
Python
Python is trending
Django
Django is a framework
Datascience
Datascience future of IT industry
Datastuctures
Datastuctures future of IT industry
"""