import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import sys
"""
__        __         _      _____ _                
\ \      / /__  _ __| | __ |_   _(_)_ __ ___   ___ 
 \ \ /\ / / _ \| '__| |/ /   | | | | '_ ` _ \ / _ \
  \ V  V / (_) | |  |   <    | | | | | | | | |  __/
   \_/\_/ \___/|_|  |_|\_\   |_| |_|_| |_| |_|\___|V0.1
"""

# základ okna
okno = tk.Tk()
okno.title("Evidence pracovní doby")
# ikona okna
ikona = PhotoImage(file="/home/jakub/GitHub/Work_time/program/clock.png")
okno.iconphoto(False, ikona)

# menubar ###############################################
def openfile():
    """Položka "Otevřít" v menu "Soubor" """
    input = filedialog.askopenfile(initialdir="/")
    print(input)
    for i in input:
        print(i)

def savefile(): 
    """ Položka "Uložit" v menu "Soubor" """ 
    data = [('All tyes(*.*)', '*.*')]
    file = asksaveasfile(filetypes = data, defaultextension = data)

def savefileas():
    """ Položka "Uložit jako" v menu "Soubor" """     

def info_menu():
    """ Položka "Info" v menu"""
    info_okno = tk.Toplevel()
    info_okno.title("Info")
    Label(info_okno, image=ikona).grid(row=0, column=0, pady=5)
    Label(info_okno, text="WORK TIME v0.1", font="bold").grid(row=1, column=0, sticky="we", pady=5, padx=5)
    Label(info_okno, text="Jakub Kolář\nkolarkuba@gmail.com\n2022").grid(row=2, column=0, sticky="we", pady=5, padx=5)
    close_button = Button(info_okno,text = "Zavřít",command=lambda:info_okno.destroy()).grid(row=3, column=0, pady=5)
    
mb = Menu(okno)
file_menu = Menu(mb, tearoff=0)
file_menu.add_command(label="Otevřít", command=openfile)
file_menu.add_command(label="Uložit", command=savefile)
file_menu.add_command(label="Uložit jako", command=savefileas)
file_menu.add_separator()
file_menu.add_command(label="Zavřít", command=lambda:okno.destroy())
mb.add_cascade(label="Soubor", menu=file_menu)
mb.add_command(label="Info", command=info_menu)
okno.config(menu=mb)

# Jméno ###############################################
jmeno = Entry(okno)
jmeno.insert(10,"Jméno")
jmeno.grid(row=2, column=0, sticky="w", padx=5)

# Měsíc ###############################################
mesic = Entry(okno)
mesic.insert(10,"Měsíc")
mesic.grid(row=3, column=0, sticky="w", padx=5)

# Součet ###############################################
Label(okno, text="Celkem hodin").grid(row=2, column=0, sticky="e", padx=5)
#vypocet_hodin = 
odpracovano = 0
soucet = Entry(okno, textvariable=odpracovano, width=5).grid(row=3, column=0, sticky="e", padx=5)

def soucet():
    total = 0.0
    for data in listBox.get_children():
        total += float(listBox.item(child, 'values')[3])
    
    lbl = Label(root,text=total,font=('helvetica',18))
    lbl.grid(row=5)

# tabulka ###############################################
tabulka = ttk.Treeview(okno)
tabulka.grid(row=4, column=0, sticky="w", padx=5)
# nastavení sloupců
tabulka["columns"] = ("Datum", "Od", "Do", "Hodin", "Misto", "Poznamka")
tabulka.column("#0", width=0,  stretch=NO)
tabulka.column("Datum", anchor=CENTER, width=80)
tabulka.column("Od", anchor=CENTER, width=80)
tabulka.column("Do", anchor=CENTER, width=80)
tabulka.column("Hodin", anchor=CENTER, width=80)
tabulka.column("Misto", anchor=CENTER, width=150)
tabulka.column("Poznamka", anchor=CENTER, width=80)
# nastavení popisků sloupců
tabulka.heading("#0",text="",anchor=CENTER)
tabulka.heading("Datum",text="Datum",anchor=CENTER)
tabulka.heading("Od",text="Od",anchor=CENTER)
tabulka.heading("Do",text="Do",anchor=CENTER)
tabulka.heading("Hodin",text="Hodin",anchor=CENTER)
tabulka.heading("Misto",text="Místo",anchor=CENTER)
tabulka.heading("Poznamka",text="Poznámka",anchor=CENTER)

# data ###############################################
data = []
global count
count = 1   
for zaznam in data:      
    tabulka.insert(parent='', index="end", iid=count, text="", values=(zaznam[0], zaznam[1], zaznam[2], zaznam[3], zaznam[4], zaznam[5]))       
    count += 1

# Rámec vkládacích polí ###############################################
Input_frame = Frame(okno)
Input_frame.grid(row=5, column=0)
# Popisky vkládacích polí
Datum = Label(Input_frame,text="Datum")
Datum.grid(row=0,column=0)
Od = Label(Input_frame,text="Od")
Od.grid(row=0,column=1)
Do = Label(Input_frame,text="Do")
Do.grid(row=0,column=2)
Hodin = Label(Input_frame,text="")
Hodin.grid(row=0, column=3)
Misto = Label(Input_frame,text="Místo")
Misto.grid(row=0,column=4)
Poznamka = Label(Input_frame,text="Poznámka")
Poznamka.grid(row=0,column=5)
# vkládací pole
Datum_entry = DateEntry(Input_frame, width=8)
Datum_entry.grid(row=1,column=0)
Od_entry = Entry(Input_frame, width=8)
Od_entry.grid(row=1,column=1)
Do_entry = Entry(Input_frame, width=8)
Do_entry.grid(row=1,column=2)
Hodin_entry = Entry(width=0)
Misto_entry = Entry(Input_frame, width=24)
Misto_entry.grid(row=1,column=4)
Poznamka_entry = Entry(Input_frame, width=15)
Poznamka_entry.grid(row=1,column=5)

# Rámec tlačítek ###############################################
Button_frame = Frame(okno)
Button_frame.grid(row=6, column=0)

def input_record():
    """ nastavení vyčítaní vkládacích polí"""
    global count
    tabulka.insert(
    parent="",
    index="end",
    iid = count,
    text="",
    values=(
    Datum_entry.get(),
    Od_entry.get(),
    Od_entry.get(),
    Hodin_entry.get(),
    Misto_entry.get(),
    Poznamka_entry.get()))
    count += 1   
    Datum_entry.delete(0,END)
    Od_entry.delete(0,END)
    Do_entry.delete(0,END)
    Misto_entry.delete(0,END)
    Poznamka_entry.delete(0,END)
    # čítač hodin
    odpracovano += int(vypocet_hodin)

def delete():
    """ Smazání vybraných dat z tabulky"""
    selected_item = tabulka.selection()[0]
    tabulka.delete(selected_item)
         
# button "Vložit záznam"
butt_plus = PhotoImage(file="/home/jakub/GitHub/Work_time/program/plus.png")
Input_button = Button(Button_frame, command=input_record, image=butt_plus, relief="flat").grid(row=0, column=0, pady=5)

# button "Smazat záznam"
butt_minus = PhotoImage(file="/home/jakub/GitHub/Work_time/program/minus.png")
delete_button = Button(Button_frame, command=delete, image=butt_minus, relief="flat").grid(row=0, column=1, pady=5)

# metoda hlavního okna mainloop, udržuje okno otevřené
okno.mainloop()