from tkinter import Tk, filedialog
root = Tk() 
root.withdraw() 
root.attributes('-topmost', True) 
open_file = filedialog.askdirectory() 
print(open_file) 
