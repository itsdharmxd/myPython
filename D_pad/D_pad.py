import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,font,messagebox,filedialog
import os
main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title('DHARMESH_TAB_EDITOR ') 
main_application.iconbitmap(r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icon.ico')
################################################--------------------MAIN MENU 
main_menu=tk.Menu(main_application)
#file icon
new_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\new.png')
open_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\open.png')
save_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\save.png')
save_as_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\save_as.png')
exit_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\exit.png')

file= tk.Menu(main_menu,tearoff=False)
#file commnds


#edit icons
copy_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\copy.png')
paste_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\paste.png')
cut_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\cut.png')
clear_all_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\clear_all.png')
find_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\find.png')

edit= tk.Menu(main_menu,tearoff=False)
#edir commands


#view icon 
tool_bar_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\tool_bar.png')
status_bar_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\status_bar.png')

view= tk.Menu(main_menu,tearoff=False)
#view command


#colour theam
light_default_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\light_default.png')
light_plus_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\light_plus.png')
dark_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\dark.png')
red_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\red.png')
monokai_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\monokai.png')
night_blue_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\night_blue.png')
colour_theme= tk.Menu(main_menu,tearoff=False)

theme_choise=tk.StringVar()
colour_choise=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
colour_dict={
      'Light Default':('#000000','#ffffff'),#('text colour','theme colour')
      'Light Plus':('#474747','#e0e0e0'),
      'Dark':('#c4c4c4','#2d2d2d'),
      'Red':('#2d2d2d','#ffe8e8'),
      'Monokai':('#d3b774','#474747'),
      'Night Blue':('#ededed','#6b9dc2')

}



main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Colur Theme',menu=colour_theme)


#------------------------------------------------------------------END OF MAIN MENU
##################################################-----------------TOOLBAR
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=10,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

#bold italic Underline  font left right center icon
bold_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\bold.png')
italic_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\italic.png')
undeline_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\underline.png')
font_colour_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\font_color.png')
align_left_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\align_left.png')
align_center_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\align_center.png')
align_right_icon=tk.PhotoImage(file=r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons\align_right.png')

#bold italic Underline  font left right center buttons
bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=2)

italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=2)

underline_button=ttk.Button(tool_bar,image=undeline_icon)
underline_button.grid(row=0,column=4,padx=2)

font_colour_button=ttk.Button(tool_bar,image=font_colour_icon)
font_colour_button.grid(row=0,column=5,padx=2)

align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=2)

align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=2)

align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=2)

#------------------------------------------------------------------END OF TOOL  BAR


#######################################################-------------TEXT EDITOR
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)


#scroll bar
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


#change font and size function
current_font_family='Arial'
current_font_size=12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontsize(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_size.bind('<<ComboboxSelected>>',change_fontsize)    
font_box.bind('<<ComboboxSelected>>',change_font)   

#button functionality

#--------bold button
def change_bold():
    text_property=tk.font.Font(font=(text_editor['font']))
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    elif text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_button.configure(command=change_bold)
def change_italic():
    text_property=tk.font.Font(font=(text_editor['font']))
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    elif text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_button.configure(command=change_italic)
def change_underline():
    text_property=tk.font.Font(font=(text_editor['font']))
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    elif text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_button.configure(command=change_underline)

#colour choser
def change_colour():
    colour_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_var[1])
font_colour_button.configure(command=change_colour)


def align_to_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=align_to_left)   
def align_to_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_button.configure(command=align_to_center)   
def align_to_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_button.configure(command=align_to_right)   






text_editor.configure(font=('Arial',12))
#-------------------------------------------------------------------END OF TEXT EDITOR
#########################################################-----------MAIN STATUS BAR

status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def change_text(event=None):
     global text_changed
     text_changed=True
     if text_editor.edit_modified(): 
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
     text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',change_text)



#-------------------------------------------------------------------END OF mainN STATUS BAR
###########################################################---------MAIN MENU FUNCTIONALITY
#filecommands

url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)


file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))                
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

def save_file(event=None):
     global url 
     try :
         if url:
             
             content=str(text_editor.get(1.0,tk.END))
             with open(url,'w',encoding='utf-8') as fw:
                 fw.write(content)
         else:
             
             url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All files','*.*')))
             content2=text_editor.get(1.0,tk.END)
             url.write(content2)
             url.close()
     except:
         
         return               



file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

def save_as_file(event=None):
     global url 
     try :
             content=text_editor.get(1.0,tk.END)             
             url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All files','*.*')))
             url.write(content)
             url.close()
     except:
         
         return  
file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=save_as_file)

def exit_func(event=None):
    global url,text_changed
      
    try:
      if text_changed:
              
              mbox=messagebox.askyesnocancel('Warning','Do you want to save the file')
              if mbox is True:
                  if url:
                      content=text_editor.get(1.0,tk.END)
                      with open(url,'w',encoding='utf=8') as fw:
                          fw.write(content)
                          main_application.destroy()
                  else:
                       content2=str(text_editor.get(1.0,tk.END))
                       url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                       url.write(content2)
                       url.close()
                       main_application.destroy()
              elif  mbox is False:
                  main_application.destroy()
      else:
              
              main_application.destroy()
    except:
          return                             



file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+E',command=exit_func)

#edit commands


edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+del',command=lambda : text_editor.delete())

def find_func(event=None): 
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def Replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    #frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    #lable
    text_find_label=ttk.Label(find_frame,text='Find:')
    text_replace_label=ttk.Label(find_frame,text='Replace')
    #entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    #button
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=Replace)
    #label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=0,column=0,padx=4,pady=4)

    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

#view commands
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
         text_editor.pack_forget()
         status_bar.pack_forget()
         tool_bar.pack(side=tk.TOP,fill=tk.X)
         text_editor.pack(fill=tk.BOTH,expand=True)
         status_bar.pack(side=tk.BOTTOM)
         show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True           
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
 
#colour theam
def change_theme():
     chosen_theme=theme_choise.get()
     colout_tuple=colour_dict.get(chosen_theme)
     fg_colour,bg_colour=colout_tuple[0],colout_tuple[1]
     text_editor.config(background=bg_colour,fg=fg_colour )

count=0
for i in colour_dict:
    colour_theme.add_radiobutton(label=i,image=colour_choise[count],variable=theme_choise,compound=tk.LEFT,command=change_theme)
    count+=1
#-------------------------------------------------------------------END OF MAIN MENU FUNCTIONALITY
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Shift-s>',save_as_file)
main_application.bind('<Control-e>',exit_func)
main_application.bind('<Control-f>',find_func)
main_application.configure(menu=main_menu)

main_application.mainloop()
