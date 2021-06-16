# ##1##FIBONACCI NUMBER###############################################################
# ##Function for nth Fibonacci number using recursion
# num=int(input("enter a number:"))
# def Fibonacci(n):
# 	if n<0:
# 		print("incorrect input")
# 	elif n==1:
# 		return 0#first fibonacci number:0
# 	elif n==2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(num))	
# """
# enter a number:9
# 21	
# """
# *****************************************
# ##Function for fibonacci series
# def recur_fibo(n):
# 	if n<=1:
# 		return n
# 	else:
# 		return(recur_fibo(n-1)+recur_fibo(n-2))
# nterms=int(input("how many terms?:"))
# if nterms<=0:
# 	print("please enter a positive integer.")
# else:
# 	print("fibonacci series:")
# 	for i in range(nterms):
# 		print(recur_fibo(i))
# """
# how many terms?:10
# fibonacci series:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# """
# ***************************************************
# ##Function for nth fibonacci number using dynamic programming
# a=int(input("enter input:"))
# FibArray=[0,1]
# def fibonacci(n):
# 	if n<0:
# 		print("incorrect input")
# 	elif n<=len(FibArray):
# 		return FibArray[n-1]
# 	else:
# 		temp_fib=fibonacci(n-1)+(n-2)
# 		FibArray.append(temp_fib)
# 		return temp_fib
# print(fibonacci(a))		
# """
# enter input:12
# 56
# """
#********************************************************
# ##Function for nth fibonacci number using space optimization
# a=int(input("enter input:"))
# def fibonacci(n):
# 	a=0
# 	b=1
# 	if n<0:
# 		print("incorrect input")
# 	elif n==0:
# 		return a
# 	elif n==1:
# 		return b
# 	else:
# 		for i in range(2,n):
# 			c=a+b
# 			a=b
# 			b=c
# 		return b
# print(fibonacci(a))		
# """
# enter input:12
# 89
# """
##2####PRIME NUMBER###############################################################################
# num=int(input("enter a number:"))
# if num>1:
# 	for i in range(2,num//2):
# 		if(num%i)==0:
# 			print(num,"is not a prime number")
# 			break
# 	else:
# 		print(num,"is a prime number")
# else:
# 	print(num,"is not a prime number")
# """
# enter a number:8
# 8 is not a prime number
# enter a number:5
# 5 is aprime number
# """	
#******************************************************************
# # # Python program to check if the input number is prime or not
# num=int(input("enter a number:"))
# if num>1:
# 	for i in range(2,num):
# 		if(num%i)==0:
# 			print(num,"is not a prime number")
# 			print(i,"times",num//i,"is",num)
# 			break
# 	else:
# 			print(num,"is a prime number")
# else:
# 	print(num,"is not a prime number")
# """
# enter a number:131
# 131 is a prime number

# enter a number:407
# 407 is not a prime number
# 11 times 37 is 407
# """
#**********************************************************************			
#3#PALINDROME###############################################################################
# # Program to check if a string is palindrome or not
# my_str='racecar'
# my_str=my_str.casefold()
# rev_str=reversed(my_str)
# if list(my_str)==list(rev_str):
# 	print("it is palindrome")
# else:
# 	print("it is not palindrome")
# """
# it is palindrome
# """
# a='1321'
# a=a.casefold()
# r=reversed(a)
# if list(a)==list(r):
# 	print("it is palindrome")
# else:
# 	print("it is not palindrome")
# """it is not palindrome"""
#***************************************************
##Python Program to Check if a Number is a Palindrome
# 1. Take the value of the integer and store in a variable.
# 2. Transfer the value of the integer into another temporary variable.
# 3. Using a while loop, get each digit of the number and store the reversed number in another variable.
# 4. Check if the reverse of the number is equal to the one in the temporary variable.
# n=int(input("enter a number:"))
# temp=n
# rev=0
# while(n>0):
# 	dig=n%10
# 	rev=rev*10+dig
# 	n=n//10
# if(temp==rev):
# 	print("it is palindrome")
# else:
# 	print("it is not palindrome")
# """
# enter a number:121
# it is palindrome

# enter a number:1231
# it is not palindrome
# """	
# *****************************************************
# # Python Program to Check if a String is a Palindrome or Not
# string=str(input("enter string:"))
# if(string==string[::-1]):
# 	print(string,"it is palindrome")
# else:
# 	print(string,"it is not palindrome")
# """
# enter string:malayalam
# malayalam it is palindrome

# enter string:coke
# coke it is not palindrome
# """
# #**********
# x = str(input("enter string:"))
# w = "" 
# for i in x: 
#     w = i + w 
#     if (x==w): 
#         print("YES") 
# else:
# 	print("NO")
# # *****************
# # Method using inbuilt function to reverse a string:predefined function ‘ ‘.join(reversed(string)) is used reverse string. 
# s = str(input("enter string:"))
# def isPalindrome(s): 
#     r= ''.join(reversed(s)) 
#     if (s == r): 
#         return True
#     return False
# t = isPalindrome(s) 
  
# if (t): 
#     print("Yes") 
# else: 
#     print("No")
#*************** ********
# #ITERATIVE METHOD***************************
# def ispalindrome(str):
# 	for i in xrange(0,len(str)/2):
# 		if str[i]!=str(len(str)-i-1):
# 			return False
# 	return True
# s='malayalam'
# t=ispalindrome(s)
# if(t):
# 	print("YES")
# else:
# 	print("NO")
#****************************************
####FACTORIAL NUMBER#####################################################################################
# # //1method# Python 3 program to find factorial of given number 
# def factorial(n):
# 	return 1 if (n==1 or n==0) else n*factorial(n-1)
# n=5
# print("factorial of",n,"is",factorial(n))
# #o/p:factorial of 5 is 120
#*************
## //method2
# n=int(input("enter number"))
# def fact(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*fact(n-1)
# print(fact(n))		
# #o/p:enter number7-5040
#*************
##//method3
# def fact(n):
# 	if n==1:
# 		return 1
# 	else:
# 		return n*fact(n-1)
# print(fact(10))
# #o/p:3628800
#*****************************************************
##ARMSTRONG NUMBER############################################################################################
# #Check Armstrong number of n digits
# num=1634
# order=len(str(num))
# sum=0
# temp=num
# while(temp>0):
# 	digit=temp%10
# 	sum+=digit**order
# 	temp//=10
# if num==sum:
# 	print(num,"is an Armstrong number")
# else:
# 	print(num,"is not an Armstrong number")
# #o/p:1634 is an Armstrong number
##*************************************
# ##Check Armstrong number (for 3 digits)
# num=int(input("enter a number:"))
# sum=0
# temp=num
# while(temp>0):
# 	digit=temp%10
# 	sum+=digit**3
# 	temp//=10
# if num==sum:
# 	print(num,"is an Armstrong number")
# else:
# 	print(num,"is not an Armstrong number")
# #o/p:enter a number:153-153 is an Armstrong number
##*********************************************
##SUM OF DIGITS#################################################################################################
# n=int(input("enter a number:"))
# tot=0
# while(n>0):
# 	dig=n%10
# 	tot=tot+dig
# 	n=n//10
# print("the total sum of digits is:",tot)	
# #o/p:enter a number:1892-the total sum of digits is: 20
# #enter a number:8976546-the total sum of digits is: 45
##reverse of string##################################################################################################
# #1#Using reversed############################
# def reverse(string):
# 	string="".join(reversed(string))
# 	return string
# s="Geeksforgeeks"
# print ("The original string  is : ",end="") 
# print (s) 
# print ("The reversed string(using reversed) is : ",end="") 
# print (reverse(s)) 	
# """
# The original string  is : Geeksforgeeks
# The reversed string(using reversed) is : skeegrofskeeG
# """
# ##2##Using extended slice syntax###############
# def reverse(string):
# 	string=string[::-1]
# 	return string
# s="Geeksforgeeks"
# print (reverse(s)) 
# #o/p:skeegrofskeeG	
# ##3##Using recursion###########################
# def reverse(s):
# 	if len(s)==0:
# 		return s
# 	else:
# 		return reverse(s[1:])+s[0]
# s="Geeksforgeeks"	
# print(reverse(s))	
# #o/p:skeegrofskeeG	
# ##4#Using loop############################
# def reverse(s):
# 	str=""
# 	for i in s:
# 		str=i+str
# 	return str
# s="kajukaju"
# print(reverse(s))	
# #o/p:ujakujak
#************************************************************************************************************************
#8#SWAPPING OF TWO NUMBERS WITHOUT USING THIRD NUMBER###################################################################
# #1 METHOD#USING ADD&SUB#ARITHMETIC OPERATORS#####################
# x=10
# y=5
# x=x+y
# y=x-y
# x=x-y
# print("After swapping:x=",x,"y=",y)
# #o/p:After swapping:x= 5 y= 10
#***********************************************************
# ##USING MUL&DIV###########
# x=10
# y=5
# x=x*y
# y=x//y
# x=x//y
# print("After swapping:x=",x,"y=",y)
# #o/p:After swapping:x= 5 y= 10
#***********************************************************
# #2 METHOD#USING BITWISE XOR###########
# x=10
# y=5
# x=x^y
# y=x^y
# x=x^y
# print("After swapping:x=",x,"y=",y)
# #o/p:After swapping:x= 5 y= 10
#***********************************************************
# #9#print hello without using semicolon################################################################################
# print("hello")
# #o/p:hello
#********************************
#10#ASSEMBLY PROGRAM###################################################################################################
##11#MATRIX MULTIPLICATION###################################################################################################
# #Using Simple Nested Loops--Program to multiply two matrices using nested loops ************************************
# A=[[12,7,3],
#    [4,5,6],
#    [7,8,9]]
# B=[[5,8,1,2],
#    [6,7,3,0],
#    [4,5,9,1]] 
# result=[[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]
# for i in range(len(A)):
# 	for j in range(len(B[0])):
# 		for k in range(len(B)):
# 			result[i][j]+=A[i][k]*B[k][j]
# for r in result:
# 	print(r)
# #o/p:[114, 160, 60, 27]
# #    [74, 97, 73, 14]
# #    [119, 157, 112, 23]	
#********************************************
# # Method 2: Matrix Multiplication Using Nested List--using list comprehension###############
# A=[[12,7,3],
#    [4,5,6],
#    [7,8,9]]
# B=[[5,8,1,2],
#    [6,7,3,0],
#    [4,5,9,1]] 
# result=[[sum(a*b for a,b in zip(A_row,B_col))for B_col in zip(*B)]for A_row in A]
# for r in result:
# 	print(r)
# #o/p:[114, 160, 60, 27]
# #    [74, 97, 73, 14]
# #    [119, 157, 112, 23]	
########################################################################################################################
# #12#DECIMAL TO BINARY CONVERSION#
# #method 1####### Function to convert decimal number to binary using recursion ##########################
# def DecimalToBinary(num):
# 	if num>1:
# 		DecimalToBinary(num//2)
# 	print(num%2,end='')
# if __name__=='__main__':
# 	dec_val=24
# 	DecimalToBinary(dec_val)
# #o/p:11000	
# #********************************
# #Method #2: Decimal to binary using in-built function
# def DecimalToBinary(n):
# 	return bin(n).replace("0b","")
# if __name__=="__main__":
# 	print(DecimalToBinary(8))
# 	print(DecimalToBinary(18))
# 	print(DecimalToBinary(7))
# #o/p:1000
# # 10010
# # 111
# #*************************************	
##13#ALPHABET TRAINGLE##################################################################################################
# #1#
# n=5
# for i in range(1,n+1):
# 	for j in range(i,n+1):
# 		print(chr(ord('A')-1+j),end='')
# 	print()	
# #o/p:
# # ABCDE
# # BCDE
# # CDE
# # DE
# # E
#*******************************
# #2#
# n=5
# for i in range(n,0,-1):
# 	for j in range(1,i+1,1):
# 		print(chr(ord('A')-1+i),end='')
# 	print()	
# #o/p:
# # EEEEE
# # DDDD
# # CCC
# # BB
# # A
#*********************************
# #3#
# if __name__=='__main__':
# 	n=5
# 	for i in range(1,n+1):
# 		for j in range(1,i+1):
# 			print(chr(ord('A')+j-1),end='')
# 		print()	
#  #o/p:
# # A
# # AB
# # ABC
# # ABCD
# # ABCDE
#************************************
# #4#
# if __name__=='__main__':
# 	n=5
# 	for i in range(n,0,-1):
# 		for j in range(i,n+1,1):
# 			print(chr(ord('A')+j-1),end='')
# 		print()	
# # E
# # DE
# # CDE
# # BCDE
# # ABCDE
#************************************8
# #5#
# if __name__=='__main__':
# 	i,j,n=0,0,5
# 	for i in range(1,n+1):
# 		for j in range(n,i-1,-1):
# 			print(chr(ord('A')-1+i),end='')
# 		print()	
# #o/p:
# # AAAAA
# # BBBB
# # CCC
# # DD
# # E		
#**********************
# #6##
# if __name__=='__main__':
# 	i,j,n=0,0,5
# 	for i in range(1,n+1):
# 		for j in range(i,0,-1):
# 			print(chr(ord('A')+j-1),end='')
# 		print()	
# #o/p:
# # A
# # BA
# # CBA
# # DCBA
# # EDCBA
#########################################################################################################################
#14#NUMBER TRIANGLE#########################
#https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# #1#Print a number pattern using a for loop and range function.##
# for num in range(10):
# 	for i in range(num):
# 		print(num,end="")
# 	print('')	
# # # o/p:
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777
# # 88888888
# # 999999999
#************************************
# #2#riangular half pyramid number pattern
# print("second number pattern")
# lastnumber=6
# for row in range(1,lastnumber):
# 	for column in range(1,row+1):
# 		print(column,end="")
# 	print("")	
# # o/p:	
# # second number pattern
# # 1
# # 12
# # 123
# # 1234
# # 12345
#**************************************
# #3#third number pattern
# print("third number pattern")
# lastnumber=6
# for row in range(1,lastnumber):
# 	for column in range(row,0,-1):
# 		print(column,end="")
# 	print("")	
# #o/p:
# # 1
# # 21
# # 321
# # 4321
# # 54321
#****************************************
# # #4#fourth number pattern
# print("fourth number pattern")
# lastnumber=9
# for i in range(1,lastnumber):
# 	for j in range(-1+i,-1,-1):
# 		print(format(2**j,"4d"),end="")
# 	print("")	
# #o/p:
#    1
#    2   1
#    4   2   1
#    8   4   2   1
#   16   8   4   2   1
#   32  16   8   4   2   1
#   64  32  16   8   4   2   1
#  128  64  32  16   8   4   2   1
#******************************************
# # #4#fourth number pattern
# print("fifth number pattern")
# lastnumber=9
# for i in range(1,lastnumber):
# 	for i in range(0,i,1):
# 		print(format(2**i,"4d"),end="")
	
# 	for i in range(-1+i,-1,-1):
# 		print(format(2**i,"4d"),end="")
# 	print("")	
# # #o/p:
# # fifth number pattern
# #    1
# #    1   2   1
# #    1   2   4   2   1
# #    1   2   4   8   4   2   1
# #    1   2   4   8  16   8   4   2   1
# #    1   2   4   8  16  32  16   8   4   2   1
# #    1   2   4   8  16  32  64  32  16   8   4   2   1
# #    1   2   4   8  16  32  64 128  64  32  16   8   4   2   1
# #*******************************
# #6#sixth number pattern
# currentnumber=1
# stop=2
# rows=3
# for i in range(rows):
# 	for column in range(1,stop):
# 		print(currentnumber,end="")
# 		currentnumber+=1
# 	print("")
# 	stop+=2	
# #o/p:
# 1
# 234
# 56789	
#*****************************************
# #7#seventh number pattern:
# start=1
# stop=2
# currentnumber=stop
# for row in range(2,6):
# 	for column in range(start,stop):
# 		currentnumber-=1
# 		print(currentnumber,end="")
# 	print("")
# 	start=stop
# 	stop+=row
# 	currentnumber=stop
# #o/p:
# 1
# 32
# 654
# 10987
##############################################
# #8#Program to print Full Triangle Pyramid pattern using an asterisk 
# print("Print full Triangle pyramid using stars ")
# size = 7
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1 
#     for j in range(0, i + 1):
#         print("* ", end=' ')
#     print(" ")
# # # o/p:
# # Print full Triangle pyramid using stars
# #             *
# #            *  *
# #           *  *  *
# #          *  *  *  *
# #         *  *  *  *  *
# #        *  *  *  *  *  *
# #       *  *  *  *  *  *  *    
#***************************************************
# #9#half pyramid###########
# rows=input("enter number of rows:")
# rows=int(rows)
# for i in range(0,rows):
# 	for j in range(0,i+1):
# 		print("*",end="")
# 	print("\r")	
# #o/p:
# # enter number of rows:5
# # *
# # **
# # ***
# # ****
# # *****	
#************************************
# #10#Print Alphabets and Letters pattern in python
# lastnumber=6
# asciinumber=65
# for i in range(0,lastnumber):
# 	for j in range(0,i+1):
# 		character=chr(asciinumber)
# 		print(character,end="")
# 		asciinumber+=1
# 	print("")	
# # #o/p:
# # A
# # BC
# # DEF
# # GHIJ
# # KLMNO
# # PQRSTU	
########################################################################################################################
# #15#FIBONACCI TRIANGLE###############
# def fib(f,N):
# 	f[1]=1
# 	f[2]=1
# 	for i in range(3,N+1):
# 		f[i]=f[i-1]+f[i-2]
# def fiboTriangle(n):
# 	N=n*(n+1)//2
# 	f=[0]*(N+1)
# 	fib(f,N)
# 	fiboNum=1
# 	for i in range(1,n+1):
# 		for j in range(1,i+1):
# 			fiboNum = fiboNum + 1
# 			print(f[fiboNum], " ", end = "") 
# 		print()
# n=5
# fiboTriangle(n)			
# #o/p:
# 1
# 2  3
# 5  8  13
# 21  34  55  89
# 144  233  377  610
#######################################################################################################################
# #16#PASCAL TRIANGLE######################
# def printpascal(n):
# 	for line in range(0,n):
# 		for i in range(0,line+1):
# 			print(binomialcoef(line,i),"",end="")
# 		print("")
# def binomialcoef(n,k):
# 	res=1
# 	if(k>n-k):
# 		k=n-k
# 	for i in range(0,k):
# 		res=res*(n-i)
# 		res=res//(i+1)
# 	return res
# n=7
# printpascal(n)
# #o/p:
# # 1
# # 1 1
# # 1 2 1
# # 1 3 3 1
# # 1 4 6 4 1
# # 1 5 10 10 5 1
# # 1 6 15 20 15 6 1
#######################################################################################################################
#17#CONVERT NUMBER IN TRIANGLE#########
#number traingle

		
