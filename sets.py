#####################12 august#############
#set--sequence of elements that are separated by comma(,) declared inside{}
#which will automatically remove duplicates...
a={3,7,8,1,24,'python',89,34,76,12,1,3}
print(a)#prints 

a={}#it will take defaultly as empty dictionary
#b={}
print(type(a))

b=set()#empty set
print(type(b))

print(a)

#sets are Mutuable but elements which are declared should be immutable itself
c={3,'python',(1,2,3,),45,'django',65,}
print(c)

##set methods--for adding single element..
#add
c.add(76)
c.add('devops')
print(c)

#update--for adding multiple elements which are in sequence..
c.update([41,42,43])#it can be any format like tuple,list but in number format..
print(c)

#remove
c.remove(42)
print(c)

c.discard(41)
print(c)#same as remove

c.discard(55)
print(c)#it doesnt return anything..defaultly prints above statements..

#################################13 august###########################
#set operations

   #1)Union(|)
   #2)Intersection(&)
   #3)Difference(-)
   #4)symmetric_Difference(^)

# union -----taking all the elements is union
a={1,2,3,4,5}
b={3,4,5,6,7}

print(a.union(b))
print(a|b)

#Intersection---taking the only common elements is intersection

print(a.intersection(b))
print(a&b)

#Difference---subtracting b(a) elements in a(b) which are common,and uncoomon will be the result.
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)

#symmetric_difference--common elemenets are removed,uncommon elements are returned.
print(a.symmetric_difference(b))
print(a^b)
print(b^a)#same

print(a)
print(b)#not updated in result

a.intersection_update(b)
print(a)#updates values in the result

b.intersection_update(a)
print(b)#updates same as above

#difference_update
#symmetric_difference_update
#b.difference_update(a)
#print(b)

#frozenset--- same as normal sets but it is immutuable(cannot make any changes)
#we have to declare it using frozenset keyword itself..
a=frozenset({2,6,9,13,6,45,90,34})
print(a)
#set({})

#######################################################################
#####################################################################
#################################PRACTICE###########################
a={3,7,8,1,24,'python',89,34,76,12,1,3}
print(a)#prints random set
a={}#it will take defaultly as empty dictionary
b={}
print(type(a))
print(type(b))

b=set()#empty set
print(type(b))
print(a)

#sets are Mutuable but elements which are declared should be immutable itself
c={3,'python',(1,2,3,),45,'django',65,}
print(c)
c.add(76)
c.add('deveops')
print(c)
c.update([41,42,43])
print(c)

c.remove(42)
print(c)

c.discard(41)
print(c)

c.discard(55)
print(c)#it doesnt return anything..defaultly prints above statements..

######set operations
#intersection &
#union |
#difference -
#symmetric_difference ^

a={1,2,3,4,5}
b={3,4,5,6,7}
print(a.union(b))
print(a|b)#same as above

print(a.intersection(b))
print(a&b)#same as above

print(a.difference(b))
print(a-b)

print(b.difference(a))
print(b-a)

print(a.symmetric_difference(b))
print(a^b)

print(b.symmetric_difference(a))
print(b^a)

print(a)
print(b)#not updated in result

a.intersection_update(b)
print(a)#updates values in the result

b.intersection_update(a)
print(b)#updates same as above

a=frozenset({2,6,9,13,6,45,90,34})
print(a)








