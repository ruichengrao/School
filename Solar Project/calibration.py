# Import Module
from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("MSH Solar Interface")
# Set geometry(widthxheight)
root.geometry('350x200')


# adding a label to the root window
lb0 = Label(root, text = "Weather Determined Solar Tracking")
lb0.grid()
lbS = Label(root, text = "")
lbS.grid()

lbl = Label(root, text = "Nearest Address")
lbl.grid()
lb2 = Label(root, text = "City*")
lb2.grid()
lb3 = Label(root, text = "State/Proviences/Regions*")
lb3.grid()
#
lbW = Label(root, text = " * - Optionial determine to use sensors or")
lbA = Label(root, text = " calculations to track ")
lbD = Label(root, text = " the sun")
lbW.grid()
lbA.grid()
lbD.grid()
 
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =2)
txt2 = Entry(root, width=10)
txt2.grid(column =1, row =3)
txt3 = Entry(root, width=10)
txt3.grid(column =1, row =4)
 
# function to display user text when
# button is clicked
def clicked():
    result = txt.get()
    result2 = txt2.get()
    result3 = txt3.get()
    result4 = txt3.get()

 
# button widget with red color text inside

btn2 = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
btn3 = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
btn4 = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn2.grid(column=2, row=2)
btn3.grid(column=2, row=3)
btn4.grid(column=2, row=4)



# Execute Tkinter
root.mainloop()