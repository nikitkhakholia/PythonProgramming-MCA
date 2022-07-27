## Question
''' Create Menu based GUI application of your choice  using Tkinter 
        a) You can use date-frame or csv file for data processing and display statistical summary in the 
        form graphical representation using matplotlip (associate with any appropriate Widgets).
'''

##  Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 29 October 2021

from tkinter import *

def ptr():
	pass
# root element
root = Tk()
# frame inside root window
frame = Frame(root)

frame.pack()
root.geometry('500x200')
root.title('Lab 12')

# creating widget
widget_0 = Label(root, text="This is Tkinter Label", width=20, font=("bold", 20))
# placing widget
widget_0.place(x=100, y=10)

# creating widget
widget_1 =Label(root, text="This is Tkinter Text Field: ", width=20)
# placing widget
widget_1.place(x=40, y=50)

widget_2 = Entry(root, width=20)
# placing widget
widget_2.place(x=250, y=50)
#getting input
name = widget_2.get()


v = IntVar()
# placing widget
widget_3 =Radiobutton(root, text="Male", variable=v, value=1)
widget_3.place(x=80, y=80)
widget_4 =Radiobutton(root, text="Female", variable=v, value=2)
widget_4.place(x=200, y=80)

widget_5 = Button(root, command=ptr, height=2, width=10, text="Show")
widget_5.place(x=200, y=150)

widget_6 = Checkbutton( text="This is check box")
widget_6.place(x=200, y=120)

# opening plot
root.mainloop()
