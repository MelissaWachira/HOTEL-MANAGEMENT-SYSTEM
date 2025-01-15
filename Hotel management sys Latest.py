from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
import tempfile


root = Tk()
root.geometry("1300x620+50+50")
root.title("melissa")
root.resizable(FALSE,FALSE)
root.overrideredirect(1)

#loading
def start():
    import time

    my_pb["value"] = 10
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 30
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 60
    root.update_idletasks()
    time.sleep(1)

    my_pb["value"] = 80
    root.update_idletasks()
    time.sleep(0)

    my_pb["value"] = 100
    root.update_idletasks()
    time.sleep(0)

    top.deiconify()
    load.destroy()

load = Toplevel()
load.geometry("400x200+500+50")
load.title("loading page")
load.resizable(FALSE,FALSE)
load.configure(bg="white")
mn = Label(load, font=("arial 18 bold"), fg="black", bg="white")
mn.place(x=170, y=60)
my_pb = Progressbar(load, orient='horizontal', mode='determinate', length=350)
my_pb.place(x=20, y=120)
label_1 = Label(load, text="Loading", fg='black', font=("Microsoft YaHei UI Light", 11), bg="white")
label_1.pack(side=TOP)
label_2=Label(load,text="Please Wait....",bg="white")
label_2.place(x=150,y=90)
start=Button(load,text='Start',command=start)
start.place(x=170,y=160)
load.overrideredirect(1)
#login
top=Toplevel()
top.geometry('400x300+50+50')
top.resizable(FALSE,FALSE)
top.title("melissa")
top.configure(bg="white")
top.overrideredirect(1)
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")


user = Entry(top, width=25, bd=5, relief=FLAT, fg="black", border=2, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, "Password")


code = Entry(top, show="*", bd=5, width=25, relief=FLAT, fg="black", border=2, bg="white",
             font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

def login():
    username = user.get()
    password = code.get()

    if username == "melissa" and password == "morgan":
        top.destroy()
        root.deiconify()

    elif username != "melissa":
         messagebox.showerror("Invalid", "invalid username")
    elif password != "morgan":
        messagebox.showerror("Invalid", "invalid password")
        root.deiconify()
        top.destroy()


l1 = Label(root, text="HOTEL MANAGEMENT SYSTEM", font=('arial', 36, 'bold'))
l1.place(x=200, y=0)
can_cvas = Canvas(root, width=1300, height=5)
line = can_cvas.create_line(0, 0, 1300, 0, width=10, fill="deep sky blue")
can_cvas.place(x=0, y=50)
name = Label(root, text="Customer Name", font=('arial', 16, 'bold'), fg="navy")
name.place(x=0, y=65)
e1 = Entry(root, font=('arial', 15))
e1.place(x=180, y=60, width=430, height=30)
can_vas = Canvas(root, width=620, height=15)
line2 = can_vas.create_line(0, 0, 620, 0, width=15, fill="midnight blue")
can_vas.place(x=0, y=95)
# cold drinks
f1 = Frame(root, width=300, height=485)
f1.place(x=0, y=105)
canvas1 = Canvas(f1, width=295, height=480)
rectangle = canvas1.create_rectangle(3, 15, 290, 475, outline="dim grey")
canvas1.place(x=3, y=5)
colddrinks = Label(f1, text="Cold Drinks", font=('arial', 18, 'bold'), fg="navy")
colddrinks.place(x=15, y=5)
soda = Label(f1, text="Soda", font=('arial', 16, 'bold'), fg="purple")
soda.place(x=15, y=55)
sodaentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
sodaentry.place(x=110, y=55, width=180, height=30)
water = Label(f1, text="Water", font=('arial', 16, 'bold'), fg="purple")
water.place(x=15, y=105)
waterentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
waterentry.place(x=110, y=105, width=180, height=30)
juice = Label(f1, text="Juice", font=('arial', 16, 'bold'), fg="purple")
juice.place(x=15, y=155)
juiceentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
juiceentry.place(x=110, y=155, width=180, height=30)
wine = Label(f1, text="Wine", font=('arial', 16, 'bold'), fg="purple")
wine.place(x=15, y=205)
wineentry = Entry(f1, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
wineentry.place(x=110, y=205, width=180, height=30)
# foods
f2 = Frame(root, width=310, height=490)
f2.place(x=301, y=105)
canvas2 = Canvas(f2, width=305, height=485)
rectangle2 = canvas2.create_rectangle(3, 15, 300, 480, outline="dim grey")
canvas2.place(x=3, y=5)
foods = Label(f2, text="Foods", font=('arial', 18, 'bold'), fg="navy")
foods.place(x=15, y=5)
matoke = Label(f2, text="Matoke", font=('arial', 16, 'bold'), fg="purple")
matoke.place(x=15, y=65)
matokeentry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
matokeentry.place(x=110, y=65, width=190, height=30)
rice = Label(f2, text="Rice", font=('arial', 16, 'bold'), fg="purple")
rice.place(x=15, y=125)
riceentry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
riceentry.place(x=110, y=125, width=190, height=30)
posho = Label(f2, text="Posho", font=('arial', 16, 'bold'), fg="purple")
posho.place(x=15, y=185)
poshoentry = Entry(f2, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
poshoentry.place(x=110, y=185, width=190, height=30)

# hot drinks
f3 = Frame(f1, width=280, height=235)
f3.place(x=10, y=241)
canvas3 = Canvas(f3, width=275, height=230)
rectangle3 = canvas3.create_rectangle(5, 15, 270, 225, outline="dim grey")
canvas3.place(x=5, y=5)
hotdrinks = Label(f3, text="Hot Drinks", font=('arial', 18, 'bold'), fg="navy")
hotdrinks.place(x=15, y=5)
coffee = Label(f3, text="Coffee", font=('arial', 16, 'bold'), fg="purple")
coffee.place(x=15, y=45)
coffeeentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
coffeeentry.place(x=120, y=45, width=150, height=30)
milk = Label(f3, text="Milk", font=('arial', 16, 'bold'), fg="purple")
milk.place(x=15, y=105)
milkentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
milkentry.place(x=120, y=105, width=150, height=30)
blacktea = Label(f3, text="Black Tea", font=('arial', 16, 'bold'), fg="purple")
blacktea.place(x=15, y=165)
blackteaentry = Entry(f3, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
blackteaentry.place(x=120, y=165, width=150, height=30)

# sauce
f4 = Frame(f2, width=290, height=270)
f4.place(x=10, y=211)
canvas4 = Canvas(f4, width=285, height=265)
rectangle4 = canvas4.create_rectangle(5, 15, 280, 255, outline="dim grey")
canvas4.place(x=5, y=5)
sauce = Label(f4, text="Sauce", font=('arial', 18, 'bold'), fg="navy")
sauce.place(x=15, y=5)
meat = Label(f4, text="Meat", font=('arial', 16, 'bold'), fg="purple")
meat.place(x=15, y=65)
meatentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
meatentry.place(x=130, y=65, width=150, height=30)
beans = Label(f4, text="Beans", font=('arial', 16, 'bold'), fg="purple")
beans.place(x=15, y=125)
beansentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
beansentry.place(x=130, y=125, width=150, height=30)
vegies = Label(f4, text="Vegetables", font=('arial', 16, 'bold'), fg="purple")
vegies.place(x=15, y=185)
vegiesentry = Entry(f4, bg="light blue", font=('arial', 17, 'bold'), justify=RIGHT)
vegiesentry.place(x=130, y=185, width=150, height=30)

# receipt
f5 = Frame(root, width=375, height=430)
f5.place(x=606, y=55)
canvas5 = Canvas(f5, width=370, height=425)
rectangle5 = canvas5.create_rectangle(5, 15, 365, 420, outline="dim grey")
canvas5.place(x=5, y=5)
receipt = Label(f5, text="Receipt", font=('arial', 18, 'bold'), fg="navy")
receipt.place(x=15, y=5)
txt = Text(f5, width=42, height=22, wrap=WORD)
txt.place(x=20, y=50)

# calculator
f6 = Frame(root, width=315, height=430)
f6.place(x=981, y=55)
canvas6 = Canvas(f6, width=310, height=425)
rectangle6 = canvas6.create_rectangle(5, 5, 300, 420, outline="dim grey")
canvas6.place(x=5, y=5)
calc = Label(f6, text="Calculator", font=('arial', 12), fg="black")
calc.place(x=15, y=0)

text_input = StringVar()
operator = ""

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")

def btnequals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

txtDisplay = Entry(f6, font=('arial', 20, 'bold'), textvariable=text_input, bd=8, insertwidth=4,
                           bg='yellow', justify='right')
txtDisplay.place(x=15, y=20, width=280)

b7 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='7',
                    command=lambda: btnclick(7)).place(x=15, y=70)
b8 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='8',
                    command=lambda: btnclick(8)).place(x=85, y=70)
b9 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='9',
                    command=lambda: btnclick(9)).place(x=155, y=70)
baddition = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='+', width=2,
                           command=lambda: btnclick("+")).place(x=225, y=70)

b4 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='4',
                    command=lambda: btnclick(4)).place(x=15, y=140)
b5 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='5',
                    command=lambda: btnclick(5)).place(x=85, y=140)
b6 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='6',
                    command=lambda: btnclick(6)).place(x=155, y=140)
bsubtraction = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='-', width=2,
                              command=lambda: btnclick("-")).place(x=225, y=140)

b1 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='1',
                    command=lambda: btnclick(1)).place(x=15, y=210)
b2 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='2',
                    command=lambda: btnclick(2)).place(x=85, y=210)
b3 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='3',
                    command=lambda: btnclick(3)).place(x=155, y=210)
bmultiplication = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='*', width=2,
                                 command=lambda: btnclick("*")).place(x=225, y=210)

b0 = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='0',
                    command=lambda: btnclick(0)).place(x=15, y=280)
bdecimal = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='.',
                          command=lambda: btnclick(".")).place(x=85, y=280)
bclear = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='C',
                        command=lambda: btncleardisplay()).place(x=155, y=280)
bdivision = Button(f6, padx=12, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='/', width=2,
                           command=lambda: btnclick("/")).place(x=225, y=280)

bequals = Button(f6, padx=16, pady=6, bd=4, fg="black", font=('arial', 20, 'bold'), text='=', width=14,
                         command=btnequals).place(x=15, y=350)

def Reset():
    e1.delete(0,END)
    sodaentry.delete(0,END)
    waterentry.delete(0,END)
    juiceentry.delete(0, END)
    wineentry.delete(0, END)
    coffeeentry.delete(0, END)
    milkentry.delete(0, END)
    blackteaentry.delete(0, END)
    matokeentry.delete(0, END)
    riceentry.delete(0, END)
    poshoentry.delete(0, END)
    meatentry.delete(0, END)
    beansentry.delete(0, END)
    vegiesentry.delete(0, END)
    taxentry.delete(0, END)
    totalentry.delete(0, END)
    txt.delete('0.0',END)

def Exit():
    Exit = messagebox.askyesno("Quit System", "Do you want to Quit?")
    if Exit > 0:
        root.destroy()
        return

def printreceipt():
    r = txt.get("1.0", "end-1c")
    filename = tempfile.mktemp(".txt")
    open(filename, "w").write(r)
    os.startfile(filename, "print")

# total
def Total():
    try:
        a1 = int(sodaentry.get())
    except:
        a1 = 0
    try:
        a2 = int(waterentry.get())
    except:
        a2 = 0
    try:
        a3 = int(juiceentry.get())
    except:
        a3 = 0
    try:
        a4 = int(wineentry.get())
    except:
        a4 = 0
    try:
        a5 = int(coffeeentry.get())
    except:
        a5 = 0
    try:
        a6 = int(milkentry.get())
    except:
        a6 = 0
    try:
        a7 = int(blackteaentry.get())
    except:
        a7 = 0
    try:
        a8 = int(matokeentry.get())
    except:
        a8 = 0
    try:
        a9 = int(riceentry.get())
    except:
        a9 = 0
    try:
        a10 = int(poshoentry.get())
    except:
        a10 = 0
    try:
        a11 = int(meatentry.get())
    except:
        a11 = 0
    try:
        a12 = int(beansentry.get())
    except:
        a12 = 0
    try:
        a13 = int(vegiesentry.get())
    except:
        a13 = 0

    sodaprice = 70.0
    waterprice = 20.0
    juiceprice = 60.0
    wineprice = 150.0
    matokeprice = 100.0
    riceprice = 70.0
    poshoprice = 90.0
    coffeeprice = 50.0
    milkprice = 25.0
    blackteaprice = 30.0
    meatprice = 200.0
    beansprice = 15.0
    vegiesprice = 20.0

    totsoda = float(a1) * sodaprice
    totwater = float(a2) * waterprice
    totjuice = float(a3) * juiceprice
    totwine = float(a4) * wineprice
    totcoffee = float(a5) * coffeeprice
    totmilk = float(a6) * milkprice
    totblacktea = float(a7) * blackteaprice
    totmatoke = float(a8) * matokeprice
    totrice = float(a9) * riceprice
    totposho = float(a10) * poshoprice
    totmeat = float(a11) * meatprice
    totbeans = float(a12) * beansprice
    totvegies = float(a13) * vegiesprice

    totalcost = (totsoda + totwater + totjuice + totwine + totcoffee + totmilk + totblacktea + totmatoke
                         + totrice + totposho + totmeat + totbeans + totvegies)
    paytax = (totalcost * 0.06)
    tax.set(paytax)
    overall = "Kshs", (paytax + totalcost)
    mytotal.set(overall)

    sentense = ("Hello, " + e1.get() + "\n Items   Amount   price"
                                                 "\n  Soda       " + str(
    sodaentry.get()) + "      " +
                str(sodaprice) + "\n  Water      " + str(waterentry.get()) + "      " +
                str(waterprice) + "\n  Juice      " + str(juiceentry.get()) + "      " +
                str(juiceprice) + "\n  Wine       " +
                str(wineentry.get()) + "      " + str(wineprice) + "\n  Matoke     " +
                str(matokeentry.get()) + "      " + str(matokeprice)
                        + "\n  Rice       " + str(riceentry.get()) + "      " + str(riceprice) + "\n  Posho      " +
                str(poshoentry.get()) + "      " + str(poshoprice) + "\n  Coffee     "
                        + str(coffeeentry.get()) + "      " + str(coffeeprice) + "\n  Milk       " +
                str(milkentry.get()) + "      " + str(milkprice) + "\n  Black Tea  " +
                str(blackteaentry.get()) + "      " + str(blackteaprice) + "\n  Meat       " +
                str(meatentry.get()) + "      " + str(meatprice) + "\n  Beans      " +
                str(beansentry.get()) + "      " +
                str(beansprice) + "\n  Vegetables " + str(vegiesentry.get()) + "      " +
                str(vegiesprice) + "\n\n  Tax   " + str(taxentry.get()) + "\n\n  Total   " +
                str(totalentry.get()) +
                        "\n\nThank you for your visit ")
    txt.insert(0.0, sentense)

tax = StringVar()
mytotal = StringVar()

lbltax = Label(root, text="Tax", font=('arial', 16, 'bold'), fg="purple")
lbltax.place(x=700, y=490)
taxentry = Entry(root, bg="powder blue", font=('arial', 17, 'bold'), justify=RIGHT, textvariable=tax)
taxentry.place(x=850, y=490, width=350, height=30)
btotal = Button(root, text="Total", fg="purple", bg="grey", font=('arial', 18, 'bold'), command=Total)
btotal.place(x=650, y=530, width=180, height=30)
totalentry = Entry(root, bg="powder blue", font=('arial', 17, 'bold'), justify=RIGHT, textvariable=mytotal)
totalentry.place(x=850, y=530, width=350, height=30)
print = Button(root, text="Print Receipt", fg="purple", bg="grey", font=('arial', 18, 'bold'),
                       command=printreceipt)
print.place(x=650, y=580, width=180, height=30)
reset = Button(root, text="Reset", fg="purple", bg="grey", font=('arial', 18, 'bold'), command=Reset)
reset.place(x=850, y=580, width=180, height=30)
exit = Button(root, text="Exit", fg="purple", bg="grey", font=('arial', 18, 'bold'), command=Exit)
exit.place(x=1020, y=580, width=180, height=30)



def exit():
    root.destroy()

Button(top, width=39, pady=7, text="Log in", command=login, bg="black", fg="white", border=0).place(x=35, y=204)
Button(top, width=39, pady=7, text="Cancel", bg="black", fg="white", command=exit, border=0).place(
        x=35, y=244)

top.withdraw()
root.withdraw()
root.mainloop()