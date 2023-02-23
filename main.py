from tkinter import *
from tkinter import messagebox
# TODO 1: math function
def add(add1,add2):
    tx.delete(0, "end")
    tx.insert(0, add1 + add2)
    return add1+add2
def sub(sub1,sub2):
    tx.delete(0, "end")
    tx.insert(0, sub1 - sub2)
    return sub1-sub2
def div(div1,div2):
    tx.delete(0, "end")
    tx.insert(0, div1 / div2)
    return div1/div2
def mut(mut1,mut2):
    tx.delete(0, "end")
    tx.insert(0, mut1 * mut2)
    return mut1*mut2
def mod(mod_num, num):
    tx.delete(0, "end")
    tx.insert(0, num%mod_num)
    return num%mod_num
def root(num, root_num):
    tx.delete(0, "end")
    tx.insert(0, num**(1/root_num))
    return  num ** (1/root_num)



# TODO 2: gui for the calculator
pow_g = 0

def cal_gui():
    global ip
    num_list = []
    def power():
        global pow_g,tx
        if pow_g % 2 == 0:
            canver.itemconfig(p,image=pw_up)
            tx = Entry(canver, width=16, font=("Haettenschweiler", 16), justify=RIGHT, fg="#10171d", bg="#72d6b2")
            tx.place(x=25.7, y=23)
        else:
            num_list.clear()
            tx.destroy()
            canver.itemconfig(p,image=pw_down)
        pow_g += 1
    # TODO 3: the make the number on the gui respond to it click

    def zerof():
        try:
            tx.delete(0, "end")
            num_list.append("0")
            tt = "".join(num_list)
            tx.insert(0,tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def onef():
        try:
            tx.delete(0, "end")
            num_list.append("1")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def twof():
        try:
            tx.delete(0, "end")
            num_list.append("2")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def threef():
        try:
            tx.delete(0, "end")
            num_list.append("3")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def fourf():
        try:
            tx.delete(0, "end")
            num_list.append("4")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def fivef():
        try:
            tx.delete(0, "end")
            num_list.append("5")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def sixf():
        try:
            tx.delete(0, "end")
            num_list.append("6")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def sevenf():
        try:
            tx.delete(0, "end")
            num_list.append("7")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def eightf():
        try:
            tx.delete(0, "end")
            num_list.append("8")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def ninef():
        try:
            tx.delete(0, "end")
            num_list.append("9")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def eqf():
        global recode
        tx.delete(0, "end")
        tt = "".join(num_list)
        num_list.clear()
        num2 = float(tt)

        if command == "+":
            num_list.append(str(add(num1,num2)))
            recode.append(str(f"{num1} {command} {num2} = {add(num1,num2)}"))
        elif command == "-":
            num_list.append(str(sub(num1,num2)))
            recode.append(str(f"{num1} {command} {num2} = {sub(num1, num2)}"))
        elif command == "*":
            num_list.append(str(mut(num1, num2)))
            recode.append(str(f"{num1} {command} {num2} = {mut(num1, num2)}"))
        elif command == "/":
            num_list.append(str(div(num1, num2)))
            recode.append(str(f"{num1} {command} {num2} = {div(num1, num2)}"))
        elif command == "%":
            num_list.append(str(mod(num2, num1)))
            recode.append(str(f"{num2} {command} {num1} = {mod(num2, num1)}"))
        elif command == "**":
            num_list.append(str(root(num1, num2)))
            recode.append(str(f"{num1} {command} {num2} = {root(num1, num2)}"))

    def dotf():
        try:
            tx.delete(0, "end")
            num_list.append(".")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def psf():
        global command, num1
        try:
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            if "-" in tt:
                num1 = -num1
                num_list.clear()
                num_list.append(str(num1))
            else:
                num1 = num1
                num_list.clear()
                num_list.append(str(f"-{num1}"))
            tt = "".join(num_list)
            tx.insert(0,tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def adf():
        global command,num1
        try:
            command = "+"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")


    def mpf():
        global command,num1
        try:
            command = "*"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def dvf():
        global command, num1
        try:
            command = "/"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def spf():
        global command, num1
        try:
            command = "-"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def modf():
        global command, num1
        try:
            command = "%"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def rootf():
        global command, num1
        try:
            command = "**"
            tx.delete(0, "end")
            tt = "".join(num_list)
            num1 = float(tt)
            num_list.clear()
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def add_memory_f():
        try:
            with open("cal.txt", mode="r") as file:
                ltd = file.read()
                td = ltd.replace("[", "")
                ltd = ltd.replace("]", "")
                ltd = ltd.replace("'", "")
                list_recode = ltd.split(",")

                list_recode.append(str(recode).replace("[","").replace("]","").replace(","," :"))
                recode.clear()

                with open("cal.txt", mode="w") as file:
                    file.write(str(list_recode))
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def remove_memory_f():
        try:
            with open("cal.txt", mode="r") as file:
                ltd = file.read()
                ltd = ltd.replace("[","")
                ltd = ltd.replace("]","")
                ltd = ltd.replace("'", "")
                list_recode = ltd.split(",")
                list_recode.pop(-1)
            with open("cal.txt", mode="w") as file:
                file.write(f"{list_recode}")
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    def memory_f():
        try:
            with open("cal.txt", mode="r") as file:
                ltd = file.read()
                ltd = ltd.replace("[", "")
                ltd = ltd.replace("]", "")
                ltd = ltd.replace("'", "")
                ltd = ltd.replace(",", "\n")
                messagebox.showinfo("Memory", f"Your math history is:\n {ltd}")
        except:
            messagebox.showerror("Power", "you most power on the calculator")
    def clsf():
        try:
            num_list.pop(-1)
            tx.delete(0, "end")
            tt = "".join(num_list)
            tx.insert(0, tt)
        except:
            messagebox.showerror("Power", "you most power on the calculator")

    canver.delete(lg)
    canver.itemconfig(background, image=bd)
    Button(image=seven, border=0, command=sevenf).place(x=1,y=90)
    Button(image=eight, border=0, command=eightf).place(x=37, y=90)
    Button(image=nine, border=0, command=ninef).place(x=73, y=90)
    Button(image=four, border=0, command=fourf).place(x=1, y=120)
    Button(image=five, border=0, command=fivef).place(x=37, y=120)
    Button(image=six, border=0, command=sixf).place(x=73, y=120)
    Button(image=one, border=0, command=onef).place(x=1, y=150)
    Button(image=two, border=0, command=twof).place(x=37, y=150)
    Button(image=three, border=0, command=threef).place(x=73, y=150)
    Button(image=zero, border=0, command=zerof).place(x=1, y=180)
    Button(image=dot, border=0, command=dotf).place(x=37, y=180)
    Button(image=ps, border=0, command=psf).place(x=73, y=180)
    Button(image=ad, border=0, command=adf).place(x=110, y=154)
    Button(image=eq, border=0, command=eqf).place(x=147, y=182)
    Button(image=sp, border=0, command=spf).place(x=147, y=154)
    Button(image=mp, border=0, command=mpf).place(x=110, y=120)
    Button(image=modo, border=0, command=modf).place(x=110, y=90)
    Button(image=rt, border=0, command=rootf).place(x=147, y=90)
    Button(image=dv, border=0, command=dvf).place(x=147, y=120)
    Button(image=on, border=0, command=power ).place(x=147, y=71)
    Button(image=cls, border=0, command=clsf).place(x=110, y=71)
    Button(image=m_, border=0, command=remove_memory_f).place(x=73, y=71)
    Button(image=m__, border=0, command=add_memory_f).place(x=37, y=71)
    Button(image=mrc, border=0, command=memory_f).place(x=1, y=71)
    p= canver.create_image(92,35.8,image=pw_down)


def loading():
    global background, lg

    background = canver.create_image(91.5, 112, image=bblogo)
    lg = canver.create_image(90, 90, image=logo)
    home.after(3000,cal_gui)

home = Tk()
recode = []
home.geometry("185x230")
bd = PhotoImage(file="image/bdy.png")
zero = PhotoImage(file="image/0.png")
one = PhotoImage(file="image/1.png")
two = PhotoImage(file="image/2.png")
three = PhotoImage(file="image/3.png")
four = PhotoImage(file="image/4.png")
five = PhotoImage(file="image/5.png")
six = PhotoImage(file="image/6.png")
seven = PhotoImage(file="image/7.png")
eight = PhotoImage(file="image/8.png")
nine = PhotoImage(file="image/9.png")
ad = PhotoImage(file="image/+.png")
sp = PhotoImage(file="image/m.png")
dv = PhotoImage(file="image/d.png")
mp = PhotoImage(file="image/x.png")
dot =PhotoImage(file="image/-.png")
ps = PhotoImage(file="image/+or-.png")
eq = PhotoImage(file="image/eq.png")
modo = PhotoImage(file="image/modo.png")
rt = PhotoImage(file="image/root.png")
on = PhotoImage(file="image/on.png")
cls = PhotoImage(file="image/cls.png")
m_ = PhotoImage(file="image/m-.png")
m__ = PhotoImage(file="image/m+.png")
mrc = PhotoImage(file="image/mrc.png")
pw_up = PhotoImage(file="image/power.png")
pw_down = PhotoImage(file="image/power_down.png")
logo = PhotoImage(file="image/logo.png")
bblogo = PhotoImage(file="image/logoback.png")
canver = Canvas(width=183,height=234)
loading()
canver.place(x=-1,y=0)

home.mainloop()



