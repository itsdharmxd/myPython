import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('GUI')
#win.mainloop()
name_label=ttk.Label(win,text='ENTER YOUR NAME =')       #LABEL CREATION
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='ENTER YOUR AGE =')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win,text='ENTER YOUR EMAIL=')
email_label.grid(row=2,column=0,sticky=tk.W)

gender_lable=ttk.Label(win,text='SELECT YOUR GENDER=')
gender_lable.grid(row=3,column=0)


name_var=tk.StringVar()                                          #ENTRY BOX CREATION
name_entry_box=ttk.Entry(win,width=16,textvariable=name_var)
name_entry_box.grid(row=0,column=1)
name_entry_box.focus()

age_var=tk.StringVar()
age_entry_box=ttk.Entry(win,width=16,textvariable=age_var)
age_entry_box.grid(row=1,column=1)
age_entry_box.focus()

email_var=tk.StringVar()
email_entry_box=ttk.Entry(win,width=16,textvariable=email_var)
email_entry_box.grid(row=2,column=1)
email_entry_box.focus()
def action():
    user_name=name_var.get()
    user_age=age_var.get()
    user_email=email_var.get()
    user_gender=gender_var.get()
    usertype=user_type.get()
    if user_cheak.get():
        subscribe='yes'
    else:
        subscribe='no'    
    with open(r'C:\Users\dharmesh\Documents\PYTHON\file_data.txt','w') as f:
          f.write(f'{user_name },{user_age},{user_email},{user_gender},{usertype},{subscribe}')
    submit_button.configure(foreground='Blue')    
    name_entry_box.delete(0,tk.END)
    age_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
          
submit_button=tk.Button(win,text="submit",command=action)
submit_button.grid(row=6,column=1)
#combo box claaa
gender_var=tk.StringVar()
gender_combo_box=ttk.Combobox(win,width=16,textvariable=gender_var,state='readonly')
gender_combo_box['values']=('MALE','FEMALE','OTHER')
gender_combo_box.current(0)
gender_combo_box.grid(row=3,column=1)
#radio button
user_type=tk.StringVar()
radio_student=ttk.Radiobutton(win,text='student',value='student',variable=user_type)
radio_student.grid(row=4,column=0)

radio_teacher=ttk.Radiobutton(win,text='teacher',value='teacher',variable=user_type)
radio_teacher.grid(row=4,column=1)

#cheak button
user_cheak= tk.IntVar()
cheak_button=ttk.Checkbutton(win,text='cheak if you have subscribe',variable=user_cheak)
cheak_button.grid(row=5,columnspan=3)




win.mainloop()