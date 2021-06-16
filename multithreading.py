#multithreading---Running multiple process at single time is Multithreading...

#declaring normal python syntax:::
# a=[2,3,4,5]
# def square(a):
# 	print(a)
# def cube(a):
# 	print(a)
# square(a)
# cube(a)	
################
# import time
# a=[2,3,4,5]

# def square(a):
# 	for j in a:
# 		time.sleep(0.1)
# 		print(j**2)
	
# def cube(a):
# 	for j in a:
# 		time.sleep(0.05)
# 		# print(time.sleep(0.05))
# 		print(j**3)
# t=time.time()#before execution
# square(a)
# cube(a)	

# #after execution with difference of before execution:time.time()-t

# print("Time taken:",time.time()-t)
#############

######using Multithreading---
# import time
# import threading
# a=[2,3,4,5]

# def square(a):
# 	# print(a)
# 	for j in a:
# 		time.sleep(0.1)
# 		print(j**2)
	

# def cube(a):
# 	# print(a)
# 	for j in a:
# 		time.sleep(0.05)
# 		# print(time.sleep(0.05))
# 		print(j**3)
# t=time.time()#before execution

# #after execution with difference of before execution:time.time()-t
# t1 = threading.Thread(target=square,args=(a,))
# t2 = threading.Thread(target=square,args=(a,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print("Time taken:",time.time()-t)

