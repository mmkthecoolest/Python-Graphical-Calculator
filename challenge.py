try:
	import tkinter
except ImportError:
	import Tkinter as tkinter

import functions

num1 = 0
num2 = 0
attempt = 0
arithmetic = 0
mainWindow = tkinter.Tk()

def concat(char):
	if resultvar.get() == "0":
		resultvar.set(char)
		return
	str = resultvar.get()
	resultvar.set(str + char)
	return

def zero():
	resultvar.set("0")
	return


def operation(str, arith_type):
	global num1
	num1 = int(str)
	global arithmetic
	arithmetic = arith_type
	zero()
	return

def calculation(string, arith_type):
	global num1, attempt

	if attempt >= 1:
		return
	attempt = attempt + 1
	if arithmetic == 0:
		operation(string, arith_type)

		return


	elif arithmetic == 1:
		num1 = num1 + int(string)
		#resultvar.set(str(num1))
		zero()
		return

	elif arithmetic == 2:
		num1 = num1 - int(string)
		#resultvar.set(str(num1))
		zero()
		return

	elif arithmetic == 3:
		num1 = num1 / int(string)
		#resultvar.set(str(num1))
		zero()
		return

	elif arithmetic == 4:
		num1 = num1 * int(string)
		zero()
		return

	return

def equal(string, arith_type):
	global arithmetic, attempt
	attempt = 0
	if arithmetic == 0:

		return

	else:
		calculation(string, arith_type)
		resultvar.set(str(num1))
		arithmetic = 0
		return

def clear():
	global arithmetic
	global num1, attempt

	attempt = 0
	num1 = 0
	arithmetic = 0
	zero()
	return

mainWindow.title("Calculator")
mainWindow.geometry("247x203-8-200") # offset position to 6 by 10
mainWindow.minsize(247, 203)
mainWindow["padx"] = 8

#rows x columns = 6 x 4
mainWindow.rowconfigure(0,weight=0)
mainWindow.rowconfigure(1,weight=2)
mainWindow.rowconfigure(2,weight=2)
mainWindow.rowconfigure(3,weight=2)
mainWindow.rowconfigure(4,weight=2)
mainWindow.rowconfigure(5,weight=2)

mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.columnconfigure(2,weight=1)
mainWindow.columnconfigure(3,weight=1)

resultvar = tkinter.StringVar()

result = tkinter.Entry(mainWindow, textvariable=resultvar)
result.grid(row=0, column=0, columnspan=4, sticky="we")

button_c = tkinter.Button(text="C", relief="groove", command=clear)
button_ce = tkinter.Button(text="CE", relief="groove", command=zero)
button_1 = tkinter.Button(text="1", relief="groove", command=lambda: concat("1"))
button_2 = tkinter.Button(text="2", relief="groove", command=lambda: concat("2"))
button_3 = tkinter.Button(text="3", relief="groove", command=lambda: concat("3"))
button_4 = tkinter.Button(text="4", relief="groove", command=lambda: concat("4"))
button_5 = tkinter.Button(text="5", relief="groove", command=lambda: concat("5"))
button_6 = tkinter.Button(text="6", relief="groove", command=lambda: concat("6"))
button_7 = tkinter.Button(text="7", relief="groove", command=lambda: concat("7"))
button_8 = tkinter.Button(text="8", relief="groove", command=lambda: concat("8"))
button_9 = tkinter.Button(text="9", relief="groove", command=lambda: concat("9"))
button_0 = tkinter.Button(text="0", relief="groove", command=lambda: concat("0"))
button_plus = tkinter.Button(text="+", relief="groove", command=lambda: calculation(resultvar.get(), 1))
button_minus = tkinter.Button(text="-", relief="groove", command=lambda: calculation(resultvar.get(), 2))
button_divide = tkinter.Button(text="/", relief="groove", command=lambda: calculation(resultvar.get(), 3))
button_multiply = tkinter.Button(text="*", relief="groove", command=lambda: calculation(resultvar.get(), 4))
button_equal = tkinter.Button(text="=", relief="groove", command=lambda: equal(resultvar.get(), arithmetic))

button_c.grid(row=1, column=0, sticky="nsew")
button_ce.grid(row=1, column=1, sticky="nsew")
button_7.grid(row=2,column=0, sticky="nsew")
button_8.grid(row=2,column=1, sticky="nsew")
button_9.grid(row=2,column=2, sticky="nsew")
button_plus.grid(row=2,column=3, sticky="nsew")
button_4.grid(row=3,column=0, sticky="nsew")
button_5.grid(row=3,column=1, sticky="nsew")
button_6.grid(row=3,column=2, sticky="nsew")
button_minus.grid(row=3,column=3, sticky="nsew")
button_1.grid(row=4,column=0, sticky="nsew")
button_2.grid(row=4,column=1, sticky="nsew")
button_3.grid(row=4,column=2, sticky="nsew")
button_multiply.grid(row=4,column=3, sticky="nsew")
button_0.grid(row=5,column=0, sticky="nsew")
button_equal.grid(row=5,column=1, sticky="nsew",columnspan=2)
button_divide.grid(row=5,column=3, sticky="nsew")


zero()
mainWindow.mainloop()