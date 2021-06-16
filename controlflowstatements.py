###controlflow stateements:::::##############

#1)break-once break is reached,any number of iterations are no counted.
#2)continue

for j in range(15,30):
	if j%3==0 and j%4==0 and j%8==0:
		print(j,"it satisties your condition")
		#break#stops upto satisfied condition ,otherwise it continues upto given value
		continue
		print("control flows")
	else:
		print(j,"not satisfied")

##########################
##########################
##########################3
###PRACTICE################
#controlflow
#break
#continue
for j in range(15,30):
	if j%3==0 and j%4==0 and j%8==0:
		print(j,"satisfies your condition")
		break#results 24satisfies
		

for j in range(15,30):
	if j%3==0 and j%4==0 and j%8==0:
		print(j,"satisfies your condition")
		continue#prints all statements with satisfied and not satisfied
		print("control flows")
	else:
		print(j,"not satisfied")

for j in range(15,30):
	if j%3==0 and j%4==0 and j%8==0:
		print(j,"satisfies your condition")
		break#stops at  15,not satisfied to 24satisfies condition
		print("control flows")
	else:
		print(j,"not satisfied")

			
		