from tkinter import *
import os
from tkinter.messagebox import showinfo

# Notepad is Created By SACHIN Sharma

from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import*
from datetime import datetime
from tkinter.filedialog import  askopenfilename, asksaveasfilename


root = Tk()
file = ''


# code by mr SAchin sharma for open file function New
def New():

    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

# for new file open to writew text
TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

#................................ this is about the openFile function for open exixting docuuments ...........................
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()



    # this is abpout the save file
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def New():
    t = showinfo("successfully Exexcuted ","yes or no ")
def cut():
    TextArea.event_generate("<<Cut>>")

def Copy():
    TextArea.event_generate("<<Copy>>")


def Paste():
    TextArea.event_generate("<<Paste>>")










# Sachin Sharma


# this is about to create the gui for noteoad ............................................
# root.geometry('350x700')
root.title("NotePad")
root.resizable(800,600)
notepad= ScrolledText(root,width = 90 , height = 40)

filemenu = Menu(root)
m1 = Menu(filemenu,tearoff = 0)
#or m1= Menu(filemenu)

m1.add_command(label = "New",command = New)
m1.add_command(label = "open",command = openFile)
m1.add_separator()
m1.add_command(label = "Save",command = saveFile)
m1.add_command(label = "SaveAs",command = New)
m1.add_separator()
m1.add_command(label = "Print",command = New)
m1.add_separator()
m1.add_command(label = "Exit" ,command = quit)
filemenu.add_cascade(label = "File",menu = m1)



# FOR ANOTHER CASCADE Edit

m2 = Menu(filemenu,tearoff = 0)
m2.add_command(label = "Undo",command = New)
m2.add_command(label = "Redo",command = New)
m2.add_separator()

m2.add_command(label = "Cut",command = cut)
m2.add_command(label = "Copy",command = Copy)
m2.add_command(label = "Paste",command = Paste)
m2.add_separator()
m2.add_command(label = "Delete",command = New)
m2.add_command(label = "Rename",command = New)
m2.add_separator()
m2.add_command(label = "Find" ,command = New)
filemenu.add_cascade(label = "Edit",menu = m2)

m2 = Menu(filemenu,tearoff = 0)
m2.add_command(label = "Font",command = New)
m2.add_command(label = "WordFormat",command = New)
m2.add_separator()# for separeting the commamdn by line
m2.add_command(label = "StatusBar",command = New)
m2.add_command(label = "Zoom",command = New)
m2.add_separator()
m2.add_command(label = "Exit" ,command = quit)
filemenu.add_cascade(label = "View",menu = m2)






root.config(menu = filemenu)











root.mainloop()

