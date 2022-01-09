from tkinter import *

#Creating Root Window
root = Tk()
root.title("My GUI")


def DisplayInputResult():
    newWindow = Toplevel(root)
    newWindow.title("Hello")
    lblInputResult = Label(newWindow, text = CreateResultMessage(myEntryWidget.get()), justify=LEFT)
    lblInputResult.grid(row=0,column=0)

def CreateResultMessage(Input):
    Result = f"""
    Hello, {str(Input)}.
    This is my first python project. 
    Did you know, There is {str(len(Input))} letters in {str(Input)}
    """
    return Result

#Creating Input Box
myEntryWidget = Entry(root, width=20)
myEntryWidget.grid(row=0, column=1)
myEntryWidget.focus_set()

#Creating a Button widget
btnConfirm = Button(root, text="Confirm", command=DisplayInputResult)
btnConfirm.grid(row=4, column=3)

btnCancel = Button(root, text="Cancel", command=root.quit)
btnCancel.grid(row=4, column=4)

#Creating a label widget
lbl1 = Label(root, text="Please Enter your Name:")
lbl1.grid(row=0, column=0)

#Creating a Blank label widget
lbl1 = Label(root, text="")
lbl1.grid(row=1, column=0)

#Main Loop allowing program to run
root.mainloop()