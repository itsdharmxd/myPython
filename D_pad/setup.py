import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\dharmesh\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\dharmesh\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable(r"C:\Users\dharmesh\Documents\PYTHON\D_pad\D_pad.py", base=base, icon=r"C:\Users\dharmesh\Documents\PYTHON\D_pad\icon.ico")]


cx_Freeze.setup(
    name = "D_pad",
    options = {r"C:\Users\dharmesh\Documents\PYTHON\D_pad\build_exe": {"packages":["tkinter","os"], "include_files":[r"C:\Users\dharmesh\Documents\PYTHON\D_pad\icon.ico",r'C:\Users\dharmesh\Documents\PYTHON\D_pad\tcl86t.dll',r'C:\Users\dharmesh\Documents\PYTHON\D_pad\tk86t.dll', r'C:\Users\dharmesh\Documents\PYTHON\D_pad\icons']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )