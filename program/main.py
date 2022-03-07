import tkinter as tk
"""
__        __         _      _____ _                
\ \      / /__  _ __| | __ |_   _(_)_ __ ___   ___ 
 \ \ /\ / / _ \| '__| |/ /   | | | | '_ ` _ \ / _ \
  \ V  V / (_) | |  |   <    | | | | | | | | |  __/
   \_/\_/ \___/|_|  |_|\_\   |_| |_|_| |_| |_|\___|V0.1
"""

# vytvoří instanci třídy
window = tk.Tk()  

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

# metoda hlavního okna mainloop, udržuje okno otevřené
window.mainloop()