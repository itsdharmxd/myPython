import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('1200x1000')
button_tk=tk.Button(root,text='click me',state='normal')#command=a_function<=haveing commands to work
button_tk.pack()
button_ttk=tk.Button(root,text='click me',state='normal')
button_ttk.pack()



root.mainloop()