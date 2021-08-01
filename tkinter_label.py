import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('1200x1200')
label_tk=tk.Label(root,text='dharmesh')
label_tk.config(text='Dharmesh i love you',font='Time 30',fg='red',justify='right',bg='orange',wraplength='900')
label_ttk=ttk.Label(root,text='dharmesh')
label_ttk.config(text='Dharmesh i love you',font='Time 30',foreground='yellow',justify='right',background='red',wraplength='900')
label_tk.pack()
label_ttk.pack()
root.mainloop()
