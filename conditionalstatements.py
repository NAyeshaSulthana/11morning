#conditional statements-statements will be executed based on conditions..
#3 statements:
#1-if statement
#2-if else statement
#3-if elif else statement

#If statement:

#block of statement in python is represented using indentation
"""
Syntax:-
#it automatically takes space in next line with 4 spaces after if condition

if condition:
	statements
"""

#a=int(input("enter the value"))
#print(type(a))
#print(a)
#if a>50:
#print("value entered is graterthan 50")

#print("Else Block")
#IF-ELSE STATEMENT
"""

#if-elif-else
""
if condition:
	statement
elif condition:
	statement
elif condition:
	statement
else
	statement
"""
marks=int(input("enter your marks:-"))

if marks>70:#if condition can be used once
	print("you dot distinction!")
elif marks>60 and marks<=70:
	print("you got first class!")
elif marks>50 and marks<=60:#elif condition can be used any no. of times
	print("you got second class!")
else:
	print("you are just passed!")
#if-else
a=int(input("enter thevalue:-"))
print(type(a))
if a>50:
	print("value entered is greater than 50")
else:
	print("value is lesser than 50")

###############################################
##################################################
############PRACTICE
#conditional statements
#3 statements
#if
#if else
#if elif else

#if
a=int(input("enter the value"))
print(type(a))
print(a)
if a>50:
	print("value entered is greater than 50")
#print("ELSE BLOCK")

#IF ELIF ELSE
"""
if condition:
	statement	
elif:
	statement
elif:
	statement
else:
	statement
	"""
marks=int(input("enter your marks:"))
if marks>70:
	print("you got distinction")
elif marks>60 and marks<=70:
	print("you got 1st class")
elif marks<50 and marks<=60:
	print("you got 2nd class")
else:
	print("you are just passs")

a=int(input("enter value:"))
print(type(a))
if a>50:
	print("value entered is greater than 50")
else:
	print("value entered is less than 50")

