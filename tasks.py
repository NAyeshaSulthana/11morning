###Dictionaries:::::::
####Task:1)Write a Python script to check if a given key already exists in a dictionary. 

# a={'company':'wipro','teams':'testing','candidate':'ayesha'}
# def key_present(i):
# 	if i in a:
# 		print("given key already exists")

# 	else:
# 		print("given key not exists")


# print(key_present("candidate"))

"""
given key already exists
"""		
# for j in a:
# 	if j=='candidate':
# 		print("key already present")
#########################################################################		
###Task:2) Write a Python script to generate and print a dictionary that contains a number 
# (between 1 and n) in the form (x, x*x). 
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# b={}
# for j in range(1,11):
# 	b[j]=j*j
	
# print(b)
#2 type:# print({j:j*j for j in range(1,11)})
"""{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}"""
##########################################################################
####Task:3)Write a program which will find all such numbers which are divisible by 7 but 
# are not a multiple of 5,between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# b=[]
# for j in range(2000,3201):
# 	if (j%7==0) and (j%5==0):
# 		b.append(str(j))
# print(",".join(b))	
"""2030,2065,2100,2135,2170,2205,2240,2275,2310,2345,2380,2415,2450,2485,2520,2555,2590,2625,2660,
2695,2730,2765,2800,2835,2870,2905,2940,2975,3010,3045,3080,3115,3150,3185"""
		
print([ if j%7==0 and j%5==0 for j in range(2000,3200)])


