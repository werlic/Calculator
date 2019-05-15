from tkinter import ttk
from tkinter import *

top = Tk('Kalkulator', 'Kalkulator', 'Kalkulator')

def input(add):
    global id, entri
    entri.insert(id, str(add))
    id += 1

def in1():
    input(1)

def in2():
    input(2)

def in3():
    input(3)

def in4():
    input(4)

def in5():
    input(5)

def in6():
    input(6)

def in7():
    input(7)

def in8():
    input(8)

def in9():
    input(9)

def in0():
    input(0)

def intitik():
    input('.')

def delete():
    global id, entri
    entri.delete(id-1)
    id -= 1

def clear():
    global id, x, teks, angka, ha, lastop
    entri.delete(0, id + 1)
    ha = 0
    angka = []
    teks = ''
    lastop = ''
    label.config(text=teks)
    id = 0
    x = 0

def tambah():
    global x, id, teks, ha, lastop
    angka.append(float(entri.get()))
    entri.delete(0, id + 1)
    if(x == 0):
        ha = angka[x]
    elif (lastop == '-'):
        ha -= angka[x]
    elif (lastop == '/'):
        ha = ha / angka[x]
    elif (lastop == 'x'):
        ha = ha * angka[x]
    else:
        ha += angka[x]
    teks += str(angka[x]) + '+'
    label.config(text=teks)
    lastop = '+'
    id = 0
    x += 1

def kurang():
    global x, id, teks, ha, lastop
    angka.append(float(entri.get()))
    entri.delete(0, id + 1)
    if (x == 0):
        ha = angka[x]
    elif (lastop == '+'):
        ha += angka[x]
    elif (lastop == '/'):
        ha = ha / angka[x]
    elif (lastop == 'x'):
        ha = ha * angka[x]
    else:
        ha -= angka[x]
    teks += str(angka[x]) + '-'
    label.config(text=teks)
    lastop = '-'
    id = 0
    x += 1


def kali():
    global x, id, teks, ha, lastop
    angka.append(float(entri.get()))
    entri.delete(0, id + 1)
    if (x == 0):
        ha = angka[x]
    elif (lastop == '+'):
        ha += angka[x]
    elif (lastop == '-'):
        ha -= angka[x]
    elif (lastop == '/'):
        ha = ha / angka[x]
    else:
        ha = ha * angka[x]
    teks += str(angka[x]) + ' x '
    label.config(text=teks)
    lastop = 'x'
    id = 0
    x += 1

def bagi():
    global x, id, teks, ha, lastop
    angka.append(float(entri.get()))
    entri.delete(0, id + 1)
    if (x == 0):
        ha = angka[x]
    elif (lastop == '+'):
        ha += angka[x]
    elif (lastop == '-'):
        ha -= angka[x]
    elif (lastop == 'x'):
        ha = ha * angka[x]
    else:
        ha = ha / angka[x]
    teks += str(angka[x]) + '/'
    label.config(text=teks)
    lastop = '/'
    id = 0
    x += 1

def hitung():
    global id, x, ha, teks, lastop
    angka.append(float(entri.get()))
    entri.delete(0, id + 1)
    has()
    teks += ' = ' + str(ha)
    label.config(text=teks)
    id = 0
    x += 1

def has():
    global ha, teks, lastop
    if (lastop == '+'):
        ha += angka[x]
        teks += str(angka[x])
        label.config(text=teks)
    elif (lastop == '-'):
        ha -= angka[x]
        teks += str(angka[x])
        label.config(text=teks)
    elif (lastop == 'x'):
        ha = ha * angka[x]
        teks += str(angka[x])
        label.config(text=teks)
    elif (lastop == '/'):
        ha = ha / angka[x]
        teks += str(angka[x])
        label.config(text=teks)
    else:
        ha = angka[x]
        teks += str(angka[x])
        label.config(text=teks)

def bt_grid():
    clear.grid(column = 1, row=1)
    hapus.grid(column=2, row=1)
    bagi.grid(column=3, row=1)
    kali.grid(column=4, row=1)
    min.grid(column=4, row=2)
    plus.grid(column=4, row=3)
    hasil.grid(column=4, row=4)
    tujuh.grid(column=1, row=2)
    eight.grid(column=2, row=2)
    nine.grid(column=3, row=2)
    empat.grid(column=1, row=3)
    lima.grid(column=2, row=3)
    enam.grid(column=3, row=3)
    one.grid(column=1, row=4)
    two.grid(column=2, row=4)
    tiga.grid(column=3, row=4)
    zero.grid(column=2, row=5)
    koma.grid(column=1, row=5)

def button(name, com):
    bt = Button(jendela_button, bg='white', width=5, text=str(name), command=com)
    return bt


angka = []
teks = ''
id = 0
x = 0
lastop = ''

jendela = Frame(top, height=800, width=600)
jendela_button = Frame(jendela)
label = Label(jendela, text=teks)

kotak_in = StringVar
entri = Entry(jendela, textvariable=kotak_in, width=30)
jendela.grid(column=1, row=1)
label.grid(column=1, row=0)
entri.grid(column=1, row=1)


clear = button('C', clear)
hapus = button('Del', delete)
bagi = button('/', bagi)
kali = button('X', kali)
plus = button('+', tambah)
min = button('-', kurang)
hasil = button('=', hitung)
one = button('1', in1)
two = button('2', in2)
tiga = button('3', in3)
empat = button('4', in4)
lima = button('5', in5)
enam = button('6', in6)
tujuh = button('7', in7)
eight = button('8', in8)
nine = button('9', in9)
zero = button('0', in0)
koma = button('.', intitik)



jendela_button.grid(column=1, row=2)
bt_grid()
top.mainloop()