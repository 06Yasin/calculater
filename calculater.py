
from tkinter import *
from tkinter import messagebox
window= Tk()
window.title("Calculater")
window.geometry("270x300+400+250")
window.resizable(FALSE,FALSE)

tank= ""

def math(key):
    global tank
    if key in "0123456789":
        screen.insert(END,key)
        tank= tank + key
    
    if key in ".()":
        screen.insert(END,key)
        tank += key
     
    if key in "+-/*":
        screen.insert(END,key)
        tank = tank + key
    
    if key== "=":

        if (tank[-1] in "/*-+"):
            messagebox.showerror("Incorrect Command","Incorrect Command")
            return
        try:
            screen.delete(0,END)
            calculation = eval(tank,{"__builtins__":NONE},{})
            tank = str(calculation)
            screen.insert(END,tank)
        except ZeroDivisionError:
            messagebox.showerror("MATH ERRROR","A number cannot be divided into 0")
            screen.delete(0,END)
            tank= ""

    if key == "C":
        screen.delete(0,END)
        tank = ""
    if key == "CE":
        tank = tank[:-1]
        screen.delete(0,END)
        screen.insert(0,tank)
    
def do_backSpace(event):
    global tank
    tank = tank[:-1]
    screen.delete(0,END)
    screen.insert(0,tank)


window.bind("<BackSpace>",do_backSpace)


screen = Entry(width=40,justify=RIGHT)
screen.grid(row=0,column=0,columnspan=3,ipadx=4)

liste = ["1","2","3","4","5","6","7","8","9","0",".","(",")","+","-","/","*","=","C","CE"]

row = 1
column = 0

for i in liste:
    komut = lambda x=i : math(x)
    Button(text=i,font= "verdana 8 bold",width=10,height=2,relief=RAISED,command=komut).grid(row=row,column=column)
    column+=1
    if column > 2:
        column=0
        row += 1


window.mainloop()