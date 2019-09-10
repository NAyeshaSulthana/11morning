#######string--sequence of anything declared in " "/' '/""" """

#strings are immutable i.e.,at the paricular place we cannot make changes after declaration

#a="python programming"
#accessing inside the string..

#print(a[16])

#print(a[5:13])

#print(a[2:17:2])#slicing

#print(a[-1])

#print(a[-2:-10:-1])

#####basic operations
#Concatenation(+)---adding multiple strings
#Repetition(*)--repeating same strings multiple times

#print("python"+"programming"+"h")

#print("python"*4)

######string methods

#print(dir(str))


#a="python programming"

#startswith----------
#print(a.startswith("pyth"))

#endswith--------
#print(a.endswith("age"))
#print(a.endswith("ing"))

#isalpha-------
#print(a.isalpha())#it checks all are alphabets only,spaces are also should be filled.

#isalnum--------
#a="qwerty12"
#print(a.isalnum())

#isdigit----
#a="123456asdcv"
#print(a.isdigit())#all the values in the should contain numbers only

#islower-------all the alphabets should be in lowercase
#a="qwertyuiasdfghj 125678"
#print(a.islower())

#isupper---all the alphabets should be in upper case
#a="ASDFG ASDF"
#print(a.isupper())

#lower-----
#a="PYTHON PROGRAMMING 10 STARS"
#print(a.lower())#converts upper to lower

#upper-coverts lower to upper
#a="asdfghjkl"
#print(a.upper())

#capitalize-converts startng character will be converted into upparcase
#a="ayesha"
#print(a.capitalize())

#title------converts each statng word into lower to upper case
#a="Opera world is a web broweser using by 1000 people"
#print(a.title())

#swapcase---converts
#print(a.swapcase())

#count-how many times a particular substrng is repeated
#a="programming language"
#print(a.count('ng'))

#index--finds index value,it will return the index of substring in the main string
#print(a.index('i'))
#we cannot find multiple index value of same alphabets,it takes deafult which is first occurance value of string
#print(a.index('g'))
#print(a.find('g'))#index and find is same
#print(a.find('z'))
####print(a.index('z'))##it will return error bcoz it doesnot show minus value as find###

#replace----

a="if you trouble the trouble,trouble troubles you,i am not the trouble,i am the truth"
#print(a.replace('trouble','problem'))
#print(a.replace('trouble','problem',4))
#print(a.rsplit('trouble',3))
print(" problem".join(a.rsplit('trouble',3)))
#replaces the word with which we intiate in the next comma and how many times is given in third place by numbers.

#strip()---------will defaultly remove the escape sequences at startng and ending of the strings.
#a="\n\tpython is\n programming language\n"#\n gives new line and \t gives tabspace
#print(a)
#print(a.strip())#it will remove the \n,\t in the startng and the ending of the strings,in the middle that are not removed
#print(a.lstrip())#strip is applied only on the left(startng)to remove sequences.
#print(a.rstrip())#strip is applied only on the right side(ending)to remove sequences.

#split()-------

#a="msd the captain of csk"
#print(a.split())#[]split makes the words as different strings considered by spaces into commas......
#print(a.split('t'))
#split('t')makes the given alphabet removed and spaces are considered as in the split &differnt strings and considered by commas.

##zfill-zerofills at the left side,if the length given is less,it fills empty strings,if the length is greater it prints complet asusual
#a="76543210"
#print(a.zfill(10))
#print(a.zfill(5))

#join-for adding everythng to all the element in the sequence.
a="python"
#print('$'.join(a))
#whatever type of value declaring should be a string only in join
a=['1','2','3','4','5','6','7']
print('@'.join(a))
####startswith,endswith,isalpha,isalnum,isdigit,islower,isupper,lowe,upper,capitalize,title,swapcase,count,index,find,replace,
##########strip,lstrip,rstrip,split,zfill,join,
