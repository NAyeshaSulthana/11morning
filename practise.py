#1#ADDING TWO NUMBERS#########
# In the below program to add two numbers, the user is first asked to enter two numbers 
# and the input is scanned using the input() function and stored in the variables number1 and number2.
#  Then, the variables number1 and number2 are added
#  using the arithmetic operator + and the result is stored in the variable sum.
# #to add two numbers::
# num1=1997
# num2=1998
# #adding two nos
# sum=num1+num2
# #printing values
# print("sum of {0} and {1} is {2}".format(num1, num2, sum))

######
Adding two number provided by user input
num1=input("enter num1:")
num2=input("enter num2:")
sum=float(num1)+float(num2)
print("sum of {0} and {1} is {2}".format(num1,num2,sum))

# ########3####SIMPLE INTEREST
# P=2
# T=3
# R=5
# SI = (P*T*R) / 100
# print("simple interest is" , SI)	

# P = 10000
# T = 5
# R = 5	
# SI=(P*T*R)/100
# print("simple interest is",SI)

#4##COMPOUND INTEREST
# def CI(principle,rate,time):
# 	CI = principle*(pow((1+rate)/100,time))
# 	print("compound interest is",CI)
# CI(5000,56,9.8)

def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
print("Area is %.6f" % findArea(5)); 

def findarea(r):
	PI=6
	return PI*(r*r);
print("area is %.6f" % findarea(2))


