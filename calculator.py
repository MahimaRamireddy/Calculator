""" a dummy doc string"""
from tkinter import*
import ast
EXPRESSION=""
def press(num):
    """ a dummy doc string"""
    global EXPRESSION
    EXPRESSION=EXPRESSION+str(num)
    equation.set(EXPRESSION)

def clear():
    """ a dummy doc string"""
    global EXPRESSION
    EXPRESSION=""
    equation.set("")

def equal():
    """ a dummy doc string"""
    global EXPRESSION
    total=str(ast.literal_eval(EXPRESSION))
    equation.set(total)
    EXPRESSION=""
top=Tk()
top.title("simple calculator")
top.geometry("340x300")
top.resizable(width=False, height=False)

equation=StringVar()

expression_field=Entry(top,textvariable=equation)
expression_field.grid(rowspan=4, columnspan=4,ipadx=84,ipady=10)


button1=Button(top,text="1", height=1,width=7,command=lambda:press("1"))
button1.grid(row=5,column=0)

button2=Button(top,text="2", height=1,width=7,command=lambda : press("2"))
button2.grid(row=5,column=1)

button3=Button(top,text="3", height=1,width=7,command=lambda : press("3"))
button3.grid(row=5,column=2)

button4=Button(top,text="4", height=1,width=7,command=lambda : press("4"))
button4.grid(row=6,column=0)

button5=Button(top,text="5", height=1,width=7,command=lambda : press("5"))
button5.grid(row=6,column=1)

button6=Button(top,text="6", height=1,width=7,command=lambda : press("6"))
button6.grid(row=6,column=2)

button7=Button(top,text="7", height=1,width=7,command=lambda : press("7"))
button7.grid(row=7,column=0)

button8=Button(top,text="8", height=1,width=7,command=lambda : press("8"))
button8.grid(row=7,column=1)

button9=Button(top,text="9", height=1,width=7,command=lambda : press("9"))
button9.grid(row=7,column=2)

decimal=Button(top,text=".", height=1,width=7,command=lambda : press("."))
decimal.grid(row=8,column=0)

button0=Button(top,text="0", height=1,width=7,command=lambda : press("0"))
button0.grid(row=8,column=1)

equal=Button(top,text="=", height=1,width=7,command=equal)
equal.grid(row=8,column=2)

plus=Button(top,text="+", height=1,width=7,command=lambda : press("+"))
plus.grid(row=5,column=3)

minus=Button(top,text="-", height=1,width=7,command=lambda : press("-"))
minus.grid(row=6,column=3)

multiply=Button(top,text="*", height=1,width=7,command=lambda : press("*"))
multiply.grid(row=7,column=3)

divide=Button(top,text="/", height=1,width=7,command=lambda : press("/"))
divide.grid(row=8,column=3)

clear=Button(top,text="clear", height=1,width=7,command=clear)
clear.grid(row=9,column=1,columnspan=2)

top.mainloop()
 