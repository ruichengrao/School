
# import required module 
from tkinter import *
  
# create object
root = Tk()
  
# create button to implement destroy()
Button(root, text="Quit", command=root.destroy).pack()
  
root.mainloop()
