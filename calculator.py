from tkinter import *
import math

# specifications of the GUI
me = Tk()
me.geometry("354x460")
me.title("CALCULATOR")
melabel = Label(me, text="CALCULATOR",fg='white', bg='black', font=("verdana", 30))
melabel.pack(side=TOP)
me.config(background='black')

textin = StringVar()
operator = ""
num = ""


def clickbut(number):  # lambda:clickbut(1)
    global operator
    global num
    if number != '+' or number != '-' or number != '*' or number != '/' or number != '%' or number != '**' :
        num = num + str(number)
    operator = operator + str(number)
    textin.set(operator)

def logbut():
    global operator
    global num
    if num:
        num = float(num)
        operator = math.log(num)
        operator = str(operator)
        textin.set(operator)
        operator = ''
        num = ''

def sqrtbut():
    global operator
    global num
    if num:
        num = float(num)
        operator = math.sqrt(num)
        operator = str(operator)
        textin.set(operator)
        operator = ''
        num = ''

def perbut():
    global operator
    global num
    if num:
        num = float(num)
        operator = num/100
        operator = str(operator)
        textin.set(operator)
        operator = ''
        num = ''

def equlbut():
    global operator
    try:
        op = (eval(operator))
        op = str(op)
    except ZeroDivisionError:
        op = "Error: cannot divide by 0"
    textin.set(op)
    operator = ''


def clrbut():
    textin.set('')
    global operator
    operator = ''


metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='white')
metext.pack()

but1 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)

but2 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but2.place(x=10, y=170)

but3 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but3.place(x=10, y=240)

but4 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but4.place(x=75, y=100)

but5 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)

but6 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but6.place(x=75, y=240)

but7 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but7.place(x=140, y=100)

but8 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but8.place(x=140, y=170)

but9 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)

but0 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)

butdot = Button(me, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=75, y=310)

butpl = Button(me, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(me, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butml = Button(me, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=205, y=240)

butdiv = Button(me, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=310)

butclear = Button(me, padx=14, pady=14, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=100)

butequal = Button(me, padx=80, pady=14, bd=4, bg='white', command=equlbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)


butlog = Button(me, padx=7.4, pady=14, bd=4, bg='white', text="log", command=logbut,
                font=("Courier New", 16, 'bold'))
butlog.place(x=270, y=170)

butpow = Button(me, padx=7, pady=14, bd=4, bg='white', text="x^y", command=lambda: clickbut("**"),
                font=("Courier New", 16, 'bold'))
butpow.place(x=270, y=240)

butsqrt = Button(me, padx=20, pady=14, bd=4, bg='white', text="√", command=sqrtbut,
                font=("Courier New", 16, 'bold'))
butsqrt.place(x=270, y=310)

butmod = Button(me, padx=14, pady=14, bd=4, bg='white', text="%", command=lambda: clickbut("%"),
                font=("Courier New", 16, 'bold'))
butmod.place(x=205, y=380)

butper = Button(me, padx=7.4, pady=14, bd=4, bg='white', text="per", command=perbut,
                font=("Courier New", 16, 'bold'))
butper.place(x=270, y=380)

me.mainloop()