# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

################
#tkinter terminology
#master = parent element
#relief = boarder style
#side = alignment (acts like float)
################

from music_sorter import Music_Sorter
import tkinter
from tkinter import filedialog
from tkinter.constants import EW, RIGHT

#get directory from field
def getDirectory(directory_field):
    return directory_field.get()

#upon button click, opens file browser and puts selection in ent_directory
def browse():
    path = filedialog.askdirectory()
    ent_directory.insert(tkinter.END, path)

#run sorting file 
def call_sorter(directory_field):
    sorter = Music_Sorter()
    sorter.parent_dir = getDirectory(directory_field)
    sorter.file()

#creation of GUI items
window = tkinter.Tk() #creates window
window.title("MP3 Sorter")
window.geometry("800x500") #width in pixels, not letters

#containing frame
frm_container = tkinter.Frame(master=window)
frm_container.columnconfigure(1, minsize=100)

frm_directory0 = tkinter.Frame(master=frm_container, relief=tkinter.RIDGE, borderwidth=2)
frm_directory1 = tkinter.Frame(master=frm_container, relief=tkinter.RIDGE, borderwidth=2) #creates frame, assigns border type and width
lbl_directory = tkinter.Label(master=frm_directory0, text="Select a target directory:") #sets label
ent_directory = tkinter.Entry(master=frm_directory1, width=100) #creates text field
btn_directory = tkinter.Button(master=frm_directory1, text="Browse", command=browse, width=10)

frm_action = tkinter.Frame(master=frm_container, relief=tkinter.RIDGE, borderwidth=2)
btn_sort = tkinter.Button(master=frm_action, text="Start", command=lambda: call_sorter(ent_directory), width=10)

#"packing" items into window and frames
frm_container.pack()
frm_directory0.grid(row=0, column=1, sticky="w")
frm_directory1.grid(row=1, column=1)
lbl_directory.pack(side=tkinter.LEFT) #adds label to frame
ent_directory.pack(side=tkinter.LEFT, fill=tkinter.X)
btn_directory.pack(side=tkinter.LEFT)

frm_action.grid(row=2, column=1)
btn_sort.pack(side=tkinter.RIGHT)

window.mainloop()  #keeps the event loop running and window open