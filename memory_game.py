from tkinter import *
from random import random
import time
from tkinter import messagebox

pencere = Tk()
pencere.title('Memory Game')
pencere.geometry("391x230")
hafiza = []
global bilinen
bilinen = 0


def acbe(a):
    if len(hafiza) == 0:
        for i in atananlar:
            if a == i[0]:
                ilk_buton = i[2]
                ilk_buton.config(text=i[1], state="disable")
                ilk_buton.config(bg='dark green', fg='white', font=('verdana', 12))
                hafiza.append(i)
    else:
        for i in atananlar:
            if a == i[0]:
                ikinci_buton = i[2]
                ikinci_buton.config(text=i[1], state="disable")
                ikinci_buton.config(bg='dark green', fg='white', font=('verdana', 12))
                if i[1] == hafiza[0][1]:
                    global bilinen
                    bilinen = bilinen + 1
                    hafiza.clear()
                    if bilinen == 8:
                        messagebox.showinfo("Memory Game", "Congratulations You're done!")
                else:
                    ikinci_buton.after(100, lambda x=i[2]: acbunu(x))


def acbunu(ikinci_buton):
    birinci_buton = hafiza[0][2]
    birinci_buton.config(text="Find Me", state="active")
    birinci_buton.config(bg='dark green', fg='white', font=('verdana', 12))
    ikinci_buton.config(text="Find Me", state="active")
    ikinci_buton.config(bg='dark green', fg='white', font=('verdana', 12))
    time.sleep(0.2)
    hafiza.clear()


sayilarimiz = [1,2,3,4,5,6,7,8]
sayilarimiz = sayilarimiz * 2
atananlar = []
satirno = 0
for satir in range(0, 4):
    sutunno = 0
    for sutun in range(0, 4):
        deger = len(sayilarimiz)
        ilk = str(satirno)+str(sutunno)
        ikinci = int(random()*deger)

        butonx = Button(pencere, text="Find Me", command=lambda a=ilk: acbe(a), height=2, width=8, padx=5, pady=5)
        butonx.config(bg='dark green', fg='white', font=('verdana', 12))
        atanacak = (ilk, sayilarimiz[ikinci], butonx)
        atananlar.append(atanacak)
        sayilarimiz.pop(ikinci)
        butonx.grid(row=satirno, column=sutunno)
        sutunno = sutunno + 1
    satirno += 1

pencere.mainloop()
