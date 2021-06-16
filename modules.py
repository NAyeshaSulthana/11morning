#ModulesEvery python file is called as modules..
#it is concept that helps loading some other files...
#loading the file programmily is called importing.
#import-- is the keyword...
#import modulename
#modulename--filename you want to import without extension..


#Modules will be divided into 2 types:-
#1)Userdefined
#2)Inbuilt Modules
"""
######1st method of loading modules....
import module1

print(module1.a)#54
print(module1.b)#65

print(module1.add(4,5))#9
print(module1.sub(4,5))#-1

#####2nd method of loading modules.....
#from modulename import functionalities

from module1 import *
#from module1 import add,sub,mul#name 'a' is not defined-so using * is necessary
print(a)#54
print(b)#65

print(add(4,5))#9
print(sub(4,5))#-1
print(mul(4,5))#20
#whenever we import python files,it is necessary to be located in python itself,because it will return error.

#when we import  python check into 3 locations:
 #1)The current working folder...
 #2)where python is installed..
 #3)environmental variables path..

import sys

print(sys.path)

sys.path.append('C:/Users/Vali Basha/Desktop/11morning')#/ change

print(sys.path)#the path which we given is added to sys.path and printed...

#from module1 import *
from module1 import (add,sub)#mul#name 'a' is not defined-so using * is necessary
#print(a)#54
#print(b)#65

print(add(4,5))#9
print(sub(4,5))#-1

from module2 import*
from module3 import*
from module2 import*#latest imported..
print(name)#python
print(city)#Hyderabad
print(add(3,4))#goes to module2 and performs action and prints result
print(div(12,3))#from module3-4.0 & from module2 that is latest imported returns 144.0

import module3
import module2
print(module3.name)#python

print(module2.add(3,4))#7

print(module2.div(12,3))#144.0

print(module3.div(12,3))#4.0


print(name)#python
"""
###1st method loading files
import module1
print(module1.a)
print(module1.b)
print(module1.add(4,5))
print(module1.sub(4,5))
print(module1.mul(4,5))
###2nd method
from module1 import *
print(a)
print(b)
print(add(4,5))
print(sub(4,5))
print(mul(4,5))

import sys
print(sys.path)
sys.path.append('C:/Users/Vali Basha/Desktop/11morning')
print(sys.path)

from module1 import (add,sub)
print(add(4,5))
print(sub(4,5))

from module2 import *
from module3 import *
from module2 import *
print(name)
print(city)
print(add(3,4))
print(div(12,3))

import module3
import module2
print(module3.name)
print(module2.add(3,4))
print(module2.div(12,3))
print(module3.div(12,3))
print(name)