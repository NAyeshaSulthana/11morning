#REGULAR EXPRESSIONS---

import re

#match
#search
#findall

#pattern-

#This is my mobile number 765 890-2345
#This is my mobile number 912 345-6789

#\d--is the symbol only for digits..
#\w--is the symbol for alphanumeric..

#{}-- specifying the length..

# pattern=r'\d{3} \d{3}-\d{4}')

# print(pattern)

#match-----will perform the operations  at the starting of the string only..
#all the regular expressions are performed only on strings..

# a="765 890-2345 This is my mobile number 765 890-2345"

# re.match(pattern,string)--syntax;;;

# match1=re.match(pattern,a)
# print(match1.group())

##search---will perform the operation to find the string anyehere present in the location unlike match..

# a="This is my mobile 665 890-2345 number 765 890-2345"
# print(re.search(pattern,a))#<re.Match object; span=(25, 37), search='765 890-2345'>
# search1=re.search(pattern,a)
# print(search1.group())

###findall--find all the strings in the file with correct 10digits

# a="This is my mobile 665 890-2345 number 765 890-2345"
# findall1=re.findall(pattern,a)
# print(findall1)#['665 890-2345', '765 890-2345']

# with open("sample2.txt",'r')as file:
# 	for line in file.readlines():
# 		search1=re.search(pattern,line)
# 		if search1==None:
# 			pass
# 		else:
# 			print(line)

# a=['monalisa@yahoo.co.in','manish@gmail.com','ayesha6@amazon.co.us','vani@facebook.com']

# pattern=r'\.in'#monalisa@yahoo.co.in
# pattern=r'\.us'#ayesha6@amazon.co.us
# pattern=r'\.in+\.us'
# pattern=r'\w'
"""monalisa@yahoo.co.in
manish@gmail.com
ayesha6@amazon.co.us
vani@facebook.com
"""
# for j in a:
# 	search1=re.search(pattern,j)
# 	if search1:
# 		print(j)
# 	else:
# 		pass
		
# p1=input("Enter the pattern:")
# pattern=r'{}'.format(p1)
# print(pattern)
# b=['sachin_Ind','pointing_Aus','cook_Eng']
# for j in b:
# 	search1=re.search(pattern,j)
# 	if search1:
# 		print(j)
# 	else:
# 		print("unable to find details")
"""Enter the pattern:_Ind
_Ind
sachin_Ind
unable to find details
unable to find details
"""		
p1=input("Enter the pattern:")
pattern=r'{}'.format(p1)
# print(pattern)
with open("sample2.csv",'r')as file:
	for j in file.readlines():
		search1=re.search(pattern,j)
		if search1:
			print(j)
		else:
			print("unable to find details")

