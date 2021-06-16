# exception_handlings---

#Exception---An error

a=[1,4.5,'a',6.5,12,0]


# for i in a:
# 	print(1/i)#at particular error,execution stops,,discontinues other values operation...

"""
1.0
0.2222222222222222
Traceback (most recent call last):
  File "exception_handlings.py", line 7, in <module>
    print(1/i)#at particular error,execution stops,,discontinues other values operation...
TypeError: unsupported operand type(s) for /: 'int' and 'str'--'a'
ZeroDivisionError: division by zero-'0'
"""

#Exception_handlings--handling the errors

#try--those line which errors are expected are written in this syntax
#except-

"""
try:
	statement
except:
	statement
"""

# for i in a:
# 	try:
# 		print(1/i)
# 	except:
# 		print("Error occured")

"""
1.0
0.2222222222222222
Error occured
0.15384615384615385
0.08333333333333333
Error occured
"""		

#Inbuilt Exceptions---

# import sys
# for i in a:
# 	try:
# 		print(1/i)
# 	except:
# 		print("Error Occured")
# 		print(sys.exc_info()[0])
"""
11.0
0.2222222222222222
Error Occured
<class 'TypeError'>
0.15384615384615385
0.08333333333333333
Error Occured
<class 'ZeroDivisionError'>
"""
		
# for i in a:
# 	try:
# 		print(1/i)
# 	except TypeError:
# 		print("Type Error Occured!")
# 		# print(sys.exe_info()[0])
# 	except ZeroDivisionError:
# 		print("ZeroDivisionError!")
"""
1.0
0.2222222222222222
Type Error Occured!
0.15384615384615385
0.08333333333333333
ZeroDivisionError!
"""		

#UserDefined Exceptions---

#Exception--

# class ValueLargeError(Exception):
# 	pass

# class ValueSmallError(Exception):
# 	pass	

# num1=int(input("Enter num1 values:-"))

# while True:
# 	try:
# 		num2=int(input("Enter num2 values:-"))

# 		if num2>num1:
# 			raise ValueLargeError

# 		elif num2<num1:
# 			raise ValueSmallError
# 		else:
# 			print("Number guessed correctly!")
# 			break
# 	except ValueLargeError:
# 			print("Value Entered is Larger!Try Again!")
# 	except ValueSmallError:
# 			print("Value Entered is Smaller!Try Again!")
			
"""
Enter num1 values:-34
Enter num2 values:-45
Value Entered is Larger!Try Again!
Enter num2 values:-20
Value Entered is Smaller!Try Again!
Enter num2 values:-34
Number guessed correctly!
"""
			

