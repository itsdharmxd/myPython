import cx_Freeze
import sys
import os
if sys.platform == 'win32':
    base ='Win32GUI'
os.environ['TCL_LIBRARY'] = r'C:\Users\dharmesh\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\dharmesh\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'   
executabiles = [cx_Freeze.Executable('D_pad.py',base=base,icon='icon.ico')]

cx_Freeze.setup(

    name ="D_pad",
    options ={'build.exe':{'packages':['tkinter','os'],'include_files':['icon.ico','tcl86t.dll','tk86t.dll','icons']}},
    version ='0.01',
    description ='Tkinter Application',
    executables =executabiles,

)