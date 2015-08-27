from tkinter import * 
from Unzip_File import *

'''
Simple File Unzipper GUI
'''

root = Tk()
root.wm_title("File Unzipper") 

def unzip_action():
	usr1 = entry_1.get()
	usr2 = entry_2.get()
	usr3 = entry_3.get()

	Unzip = UnzipFile(str(usr1),str(usr2),usr3.encode('ascii'))
	Unzip.unzip()


label_1 = Label(root, text='Filename') # create a label with name Filename
label_2 = Label(root, text='File Destination')
label_3 = Label(root, text='File Password')

Unzipbtn = Button(root, text='Unzip', command=unzip_action) # button click unzips file

entry_1 = Entry(root)  # entry fields for input
entry_2 = Entry(root)
entry_3 = Entry(root)

label_1.grid(row=0, sticky=E) # placement assignment
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)

entry_1.grid(row=0, column=1) # placement assignment
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
Unzipbtn.grid(row=3, column=2)

#c = Checkbutton(root, text='Keep me logged in') # creates a checkbutton
#c.grid(columnspan=2) # places the checkbutton
root.mainloop()
