import tkinter
from tkinter import *
root=tkinter.Tk()

root.geometry("400x300+500+300")

# root.geometry("400x300")#defining dimensions

root.resizable(0,0)#cannot extend iafter running


root.title('calculator')
# buttons are created but we dont have any label for displaying 
# we create it by adding following before the title at the root...
data=StringVar()
lbl=Label(
	root,
	text="Label",
	anchor=SE,
	font=("Verdana",20),
	textvariable=data,
	background="#ffffff",
)
lbl.pack(expand=True,fill="both",)	

val=""
A=0
operator=""
def btn1_isclicked():
	global val
	val=val+"1"
	data.set(val)

def btn2_isclicked():
	global val
	val=val+"2"
	data.set(val)
def btn3_isclicked():
	global val
	val=val+"3"
	data.set(val)
def btn4_isclicked():
	global val
	val=val+"4"
	data.set(val)
def btn5_isclicked():
	global val
	val=val+"5"
	data.set(val)
def btn6_isclicked():
	global val
	val=val+"6"
	data.set(val)
def btn7_isclicked():
	global val
	val=val+"7"
	data.set(val)
def btn8_isclicked():
	global val
	val=val+"8"
	data.set(val)
def btn9_isclicked():
	global val
	val=val+"9"
	data.set(val)
def btn0_isclicked():
	global val
	val=val+"0"
	data.set(val)
def btnC_isclicked():
	global val
	val=""
	data.set(val)
def btnplus_isclicked():
	global val
	global A
	global operator
	A=int(val)
	operator="+"
	val=val+"+"
	data.set(val)

def btnminus_isclicked():
	global val
	global A
	global operator
	A=int(val)
	operator="-"
	val=val+"-"
	data.set(val)
def btnmul_isclicked():
	global val
	global A
	global operator
	val2=val
	# if operator=="*":
	# 	x=int(val2.split('*')[1])
	# 	C=A*x
	# 	data.set(C)
	# 	val=str(C)
	A=int(val)
	operator="*"
	val=val+"*"
	data.set(val)
def btndiv_isclicked():
	global val
	global A
	global operator
	A=int(val)
	operator="/"
	val=val+"/"
	data.set(val)
def btnequals_isclicked():
	global val
	global A
	global operator
	val2=val
	if operator=="+":
		x=int(val2.split('+')[1])
		C=A+x
		data.set(C)
		val=str(C)
	elif operator=="-":
		x=int(val2.split('-')[1])
		C=A-x
		data.set(C)
		val=str(C)
	elif operator=="*":
		x=int(val2.split('*')[1])
		C=A*x
		data.set(C)
		val=str(C)
	elif operator=="/":
		x=int(val2.split('/')[1])
		C=int(A/x)
		data.set(C)
		val=str(C)
	
	       
# # creating single frame:
# frame1=Frame(root,bg="blue")
# frame1.pack(expand=True,fill="both")

#creating multiple frames:
frame1=Frame(root,bg="blue")
frame1.pack(expand=True,fill="both")

frame2=Frame(root,bg="red")
frame2.pack(expand=True,fill="both")

frame3=Frame(root,bg="pink")
frame3.pack(expand=True,fill="both")

frame4=Frame(root,bg="violet")
frame4.pack(expand=True,fill="both")

btn1 =Button(
	frame1,
	text="1",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn1_isclicked,
)
btn1.pack(side=LEFT,expand="True",fill="both")

btn2 =Button(
	frame1,
	text="2",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn2_isclicked,
)
btn2.pack(side=LEFT,expand="True",fill="both")

btn3 =Button(
	frame1,
	text="3",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn3_isclicked,
)
btn3.pack(side=LEFT,expand="True",fill="both")

btnplus =Button(
	frame1,
	text="+",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btnplus_isclicked,
)
btnplus.pack(side=LEFT,expand="True",fill="both")

btn4 =Button(
	frame2,
	text="4",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn4_isclicked,
)
btn4.pack(side=LEFT,expand="True",fill="both")
btn5 =Button(
	frame2,
	text="5",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn5_isclicked,
)
btn5.pack(side=LEFT,expand="True",fill="both")
btn6 =Button(
	frame2,
	text="6",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn6_isclicked,
)
btn6.pack(side=LEFT,expand="True",fill="both")
btnminus =Button(
	frame2,
	text="-",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btnminus_isclicked,

)
btnminus.pack(side=LEFT,expand="True",fill="both")

btn7 =Button(
	frame3,
	text="7",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn7_isclicked,
)
btn7.pack(side=LEFT,expand="True",fill="both")
btn8 =Button(
	frame3,
	text="8",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn8_isclicked,
)
btn8.pack(side=LEFT,expand="True",fill="both")
btn9 =Button(
	frame3,
	text="9",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn9_isclicked,
)
btn9.pack(side=LEFT,expand="True",fill="both")
btnmul =Button(
	frame3,
	text="*",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btnmul_isclicked,

)
btnmul.pack(side=LEFT,expand="True",fill="both")
btnC =Button(
	frame4,
	text="C",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btnC_isclicked,
)
btnC.pack(side=LEFT,expand="True",fill="both")
btn0 =Button(
	frame4,
	text="0",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btn0_isclicked,

)
btn0.pack(side=LEFT,expand="True",fill="both")
btnequals =Button(
	frame4,
	text="=",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btnequals_isclicked

)
btnequals.pack(side=LEFT,expand="True",fill="both")
btndiv =Button(
	frame4,
	text="/",
	font=("Verdana",22,),
	relief=GROOVE,
	border=0,
	command=btndiv_isclicked,

)
btndiv.pack(side=LEFT,expand="True",fill="both")


root.mainloop()#creating tk
