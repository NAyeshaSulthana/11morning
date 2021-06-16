#a=25777
#b=25777
#print(id(a))
#print(id(b))
#a="qwerty"
#print(a[0])
#print(a[1])
#a="qwertyuiopasdfghjklzxcvbnm"
#print(a[len(a)//2])
#updates address and prints
a="qwertyuiop"
a=a.upper()
print(a)
#prints but does not updates
a="qwertyuiop"
print(a.upper())
print(a)
#given command value changes output into requested specification,though letters are not ordered(lower,upper)
a=input("enter your name:-")
print("your name is",a.capitalize())
#makes center of the value
print("Hello Mr."+a.center(16,"*"))
#capitalize first alphabet and then makes center of the stars
print("Hello Mr."+a.capitalize().center(16,"*"))
#same as above
a=input("enter your name:").capitalize()
print("Hello Mr."+a.center(16,"*"))
#it gives zeroes infront of names filling within 10places
a=input("enter your name:")
print(a.zfill(10))
#zfill()exactly takes one arguments
a="1"
print(a.zfill(0))
