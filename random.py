import random
import os
import tkinter as tk
from tkinter.ttk import Label, Button
from texttable import Texttable

root = tk.Tk()
root.title("Random")

root.geometry('400x200')
root.resizable(False, False) #create UI
rand = 0
text_insert = 0
result = 0
table = Texttable()


table.set_chars(['-', '|', '+', '='])
table.header(['Random','Try','Result'])
table.set_cols_dtype(['t','i','a'])
table.set_cols_align(["c", "c", "c"])
table.set_cols_valign(["m", "m", "m"])
table.set_cols_width([7,7,7])
table.set_deco( Texttable.BORDER|Texttable.HEADER |Texttable.HLINES| Texttable.VLINES)


file = '/'
with open('Shore.txt', 'w') as f:
    pass

def to_rand(): #function to rundom
    global rand
    global text_insert
    rand=random.randint(1,10)
    text_insert=textBoxx.get('1.0','end-1c')
    
    label.config(text=rand)
    if rand == int(text_insert):
        label.config(text="WINN")
        result = ("WINN")
    else:
        result = ("LOSE")
    
    table.add_row([rand,text_insert,result]) #добавление столбца, для добавления серии нужен спсисок списков переданный функции add_rows
    with open('Shore.txt', 'w') as f:
        f.write(table.draw())
        f.close

label = tk.Label(
    root,
    text=rand,
    font=("Helvetica", 14) #label with random number
)
label.pack(ipadx=10,
           ipady=10
)

textBoxx = tk.Text(root,
                   height = 1,
                   width  = 10
)            #insert your text
textBoxx.pack(
    ipadx=10,
    ipady=10
)
textBoxx.insert('1.0','number')

random_button = tk.Button(
    root,
    text="random",
    command=to_rand
)                           #Button to random
random_button.pack(
    ipadx=5,
    ipady=5,
)

root.mainloop()