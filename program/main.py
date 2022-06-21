import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo,askquestion
from tkinter import filedialog
import sys
import csv
import webbrowser

"""
__        __         _      _____ _                
\ \      / /__  _ __| | __ |_   _(_)_ __ ___   ___ 
 \ \ /\ / / _ \| '__| |/ /   | | | | '_ ` _ \ / _ \
  \ V  V / (_) | |  |   <    | | | | | | | | |  __/
   \_/\_/ \___/|_|  |_|\_\   |_| |_|_| |_| |_|\___|V0.1
"""

def jdi_na_web():
    """ otevře odkaz v prohlížeči """
    webbrowser.open_new(url)
    


# základ okna ###############################################
okno = tk.Tk()
okno.title("Evidence pracovní doby")
okno.resizable(False, False)
# ikona okna
ikona = PhotoImage(file="/home/jakub/GitHub/Work_time/program/clock.png")
okno.iconphoto(True, ikona)

# menubar ###############################################
def openfile():
    """Položka "Otevřít" v menu "Soubor" """
    

def save(): 
    """ Položka "Uložit" v menu "Soubor" """ 
    vykaz = open("vykaz.csv", "a", encoding="utf-8", newline="")
    vykaz_zapis = csv.writer(vykaz)
    vykaz_zapis.writerow([Datum_vstup.get(), Od_vstup.get(), Do_vstup.get(), vypocet_za_den(), Misto_vstup.get(), Poznamka_vstup.get()])
    vykaz.close()
    showinfo("Potvrzení", "Vložení a uložení záznamu\nproběhlo v pořádku.")
    

def info():
    """ Položka "Info" v menu"""
    info_okno = tk.Toplevel()
    info_okno.title("Info")
    Label(info_okno, image=ikona).grid(row=0, column=0, pady=5)
    Label(info_okno, text="WORK TIME v0.1", font="bold").grid(row=1, column=0, sticky="we", pady=5, padx=5)
    Label(info_okno,text="Program pro záznam odpracovaných hodin.").grid(row=2, column=0, sticky="we", pady=5, padx=5)
    autori = Label(info_okno)
    autori.grid(row=3, column=0)
    Label(autori, text="Jakub Kolář\nkolarkuba@gmail.com", font=("Helvetica", 9)).grid(row=0, column=0, sticky="we", pady=5, padx=5)
    
    Label(info_okno, text="Tento program je šířen bez jakékoliv záruky.\nPodrobnosti naleznete v", font=("Helvetica", 9)).grid(row=4, column=0, padx=20)
    odkaz_gnu = Label(info_okno, text="GNU GENERAL Public License, verze 3 nebo novější.\n", fg="blue", cursor="hand2", font=("Helvetica", 9)).grid(row=5, column=0)
    odkaz_gnu.bind("<Button-1>", lambda:jdi_na_web("https://www.gnu.org/licenses/gpl-3.0.html"))

mb = Menu(okno, relief="flat")
file_menu = Menu(mb, tearoff=0, relief="flat")
file_menu.add_command(label="🗁 Otevřít poslední", command=openfile)
file_menu.add_command(label="🖫 Uložit", command=save)
file_menu.add_separator()
file_menu.add_command(label="Info", command=info)
file_menu.add_command(label="Zavřít", command=lambda:okno.destroy())
mb.add_cascade(label="≡", menu=file_menu, font=(18))
okno.config(menu=mb)

def info():
    """ Položka "Info" v menu"""
    info_okno = tk.Toplevel()
    info_okno.title("Info")
    Label(info_okno, image=ikona).grid(row=0, column=0, pady=5)
    Label(info_okno, text="WORK TIME v0.1", font="bold").grid(row=1, column=0, sticky="we", pady=5, padx=5)
    Label(info_okno, text="Jakub Kolář\nkolarkuba@gmail.com\n2022").grid(row=2, column=0, sticky="we", pady=5, padx=5)

# tabulka dat ###############################################
radek = 1
celkem_h = 0

def smazat():
    Od_vstup.destroy()

# popisky tabulky
popisky = Frame(okno)
popisky.grid(row=2, column=0)
Datum = Label(popisky,text="Datum", width=8, bg="gray", fg="black").grid(row=0,column=0)
Od = Label(popisky,text="Od", width=8, bg="gray", fg="black").grid(row=0,column=1)
Do = Label(popisky,text="Do", width=8, bg="gray", fg="black").grid(row=0,column=2)
Hodin = Label(popisky,text="Hodin", bg="gray", width=5, fg="black").grid(row=0,column=3)
Misto = Label(popisky,text="Místo", width=24, bg="gray", fg="black").grid(row=0,column=4)
Poznamka = Label(popisky,text="Poznámka", width=15, bg="gray", fg="black").grid(row=0,column=5)
celkem = Label(popisky, text="Celkem", width=8, bg="gray", fg="black").grid(row=47,column=0, pady=5, sticky="w")
vypln = Label(popisky, bg="gray").grid(row=47,column=1, sticky="we")
vypln1 = Label(popisky, bg="gray").grid(row=47,column=2, sticky="we")
celkem_h_cislo = Label(popisky, text=celkem_h, fg="black", width=5, bg="gray").grid(row=47,column=3, pady=5, sticky="w")

def vypocet_za_den():
    """ vypočte počet odpracovaných hodin za den """
    global celkem_h
    od = Od_vstup.get()
    do = Do_vstup.get()
    rozbor_od = od.split(":")
    rozbor_do = do.split(":")
    prevod_od = (int(rozbor_od[0]) + float(rozbor_od[1])/60)
    prevod_do = (int(rozbor_do[0]) + float(rozbor_do[1])/60)
    celkem_h = (float(celkem_h) + (prevod_do-prevod_od))
    celkem_h_cislo = Label(popisky, bg="gray", text=celkem_h, width=5).grid(row=47,column=3, pady=5, sticky="w")
    return (prevod_do-prevod_od)

# vkládací pole ###############################################
Input_frame = Frame(okno)
Input_frame.grid(row=50, column=0)
Label(okno, text="vložit nový záznam", font=("Helvetica", 8)).grid(row=49, column=0, padx=5, sticky="w")
ttk.Separator(okno, orient="horizontal").grid(row=48, column=0, pady=15, sticky="we")

Datum_vstup = DateEntry(Input_frame, width=8)
Datum_vstup.grid(row=1,column=0)
Od_vstup = Entry(Input_frame, width=8)
Od_vstup.insert(0, "od")
Od_vstup.grid(row=1,column=1)
Do_vstup = Entry(Input_frame, width=8)
Do_vstup.insert(0, "do")
Do_vstup.grid(row=1,column=2)
Misto_vstup = Entry(Input_frame, width=25)
Misto_vstup.insert(0, "místo")
Misto_vstup.grid(row=1,column=4)
Poznamka_vstup = Entry(Input_frame, width=15)
Poznamka_vstup.insert(0, "poznámka")
Poznamka_vstup.grid(row=1,column=5)

# Rámec tlačítek ###############################################
Button_frame = Frame(okno)
Button_frame.grid(row=51, column=0) 

# button "+"
def pridat():
    """ přidá nový záznam do tabulky """
    global radek
    global zaznam
    global vypocet_za_den
    try:
        Label(popisky, text=vypocet_za_den()).grid(row=radek, column=3)
        Label(popisky, text=Datum_vstup.get()).grid(row=radek, column=0)
        Label(popisky, text=Od_vstup.get()).grid(row=radek, column=1)
        Label(popisky, text=Do_vstup.get()).grid(row=radek, column=2)
        Label(popisky, text=Misto_vstup.get()).grid(row=radek, column=4)
        Label(popisky, text=Poznamka_vstup.get()).grid(row=radek, column=5)
        radek += 1
        save()
    except:
        showinfo("Chyba", "Záznam nevložen.\nZkontroluj vkládaná data.")

Input_button = Button(Button_frame, text="✚", command=pridat, relief="flat", font=(18), foreground="#7289da", activeforeground="#7289da")
Input_button.grid(row=0, column=0, pady=5)



okno.mainloop()