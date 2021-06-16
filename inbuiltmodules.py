#Those modules that comes directly with python...

#print(help('modules'))

#math,random,os,calendar,urllib

#import math
#print(dir(math))
#print(math.pow(2,3))#8

#print(math.pi)

#print(math.e)

#print(math.exp(3))

#print(math.log(10))

#print(math.log10(10))

import random
print(dir(random))

print(random.random())#0.8061479670642078-it prints range of zero value only

print(random.randint(12,30))#it print the values of the range in b/n 

#[12,15,18,21,24,27]
print(random.randrange(12,30,3))#the value are b/n 28line values only

a=[2,"a","python","django",4.5]

print(random.choice(a))#it prints  any one value randomnly each&everytime we print 

print(a)
random.shuffle(a)
print(a)#after shuffle keyword,it prints shuffling of values whenever we print the values

#0s-finding the path of the file from various subfolder files..
#Os Module--
import os

#print(dir(os))#list all the functions inside the particular  module..

print(os.getcwd())#current working directory..

#os.chdir('C:/Users/Vali Basha/Desktop')#changing the directory..

#print(os.getcwd())

#print(os.listdir(''))

#os.mkdr('Folder1')#make a directory
#os.rmdr('Folder1')#removing a directory
#os.makedirs('folder1/folder2/folder3')

#calendar module--

#import calendar
#print(calendar.firstweekday())
#print(calendar.day_name[0])

#print(calendar.isleap(1990))

#print(calendar.month(2019,8))

#print(calendar.calendar(2020))

#b=calendar.weekday(2019,1,6)
#print(calendar.day_name[b])

##Urllib--

#import urllib.request

#sample=urllib.request.urlopen("https://www.w3schools.com/python/python_modules.asp")

#print(sample)
#print(sample.read())

#############################################
###########################################
###################PRACTICE
####math##############################
#print(help('modules'))
import math
#print(dir(math))
print(math.pow(2,3))
print(math.pi)
print(math.e)
print(math.exp(3))
print(math.log(10))
print(math.log10(10))
###random############################
import random
#print(dir(random))
print(random.random())
print(random.randint(12,30))
print(random.randrange(12,30,3))

a=[2,"a","python","django",4.5]
print(random.choice(a))
print(a)
random.shuffle(a)
print(a)
#os##################################
import os
#print(dir(os))
print(os.getcwd())
#os.chdir('C:/Users/Vali Basha/Desktop')
#print(os.getcwd())
#print(os.listdir(''))
#os.mkdir('Folder1')
#os.rmdir('Folder1')
#os.makedirs('folder1/folder2/folder3')
#########calender module
import calendar
print(calendar.firstweekday())
print(calendar.day_name[0])
print(calendar.isleap(1990))
print(calendar.month(2019,8))
print(calendar.calendar(2020))

b=calendar.weekday(2019,1,6)
print(calendar.day_name[b])
"""
###Urllib
import urllib.request
sample=urllib.request.urlopen("https://www.w3schools.com/python/python_modules.asp")
print(sample)
print(sample.read())
"""