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
from tkinter.constants import EW, LEFT, RIGHT

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
window.geometry("775x375") #width in pixels, not letters (width x height)

#containing frame
frm_container = tkinter.Frame(master=window, relief=tkinter.RIDGE, borderwidth=2) #creates frame, assigns border type and width
frm_container.columnconfigure(1, minsize=100)

#intro text
frm_text0 = tkinter.Frame(master=frm_container)
lbl_text0 = tkinter.Label(master=frm_text0, text="Thank you for using this MP3 sorting tool. \n\nThis program is designed to target one folder and sort loose MP3 files into folders matching their artist tags. \n\nIt does not run recursively.\nIt will delete original files after moving them.\nBe certain before running that you want everything in the folder sorted.", justify=LEFT)

#folder entry and browse button
frm_directory0 = tkinter.Frame(master=frm_container)
frm_directory1 = tkinter.Frame(master=frm_container) #creates frame, assigns border type and width
lbl_directory = tkinter.Label(master=frm_directory0, text="Select a target directory:") #sets label
ent_directory = tkinter.Entry(master=frm_directory1, width=100) #creates text field
btn_directory = tkinter.Button(master=frm_directory1, text="Browse", command=browse, width=10)

#Start button
frm_action = tkinter.Frame(master=frm_container)
btn_sort = tkinter.Button(master=frm_action, text="Start", command=lambda: call_sorter(ent_directory), width=10) #lambda format keeps method from calling at startup

#"packing" items into window and frames
frm_container.pack()

#packing text blurb
frm_text0.grid(row=0, column=1, sticky="w", pady=(10, 20), padx=10)
lbl_text0.pack(side=tkinter.LEFT)

#packing directory selection
frm_directory0.grid(row=1, column=1, sticky="w", padx=10)
frm_directory1.grid(row=2, column=1, padx=10)
lbl_directory.pack(side=tkinter.LEFT) #adds label to frame
ent_directory.pack(side=tkinter.LEFT, fill=tkinter.X)
btn_directory.pack(side=tkinter.LEFT)

#packing start button
frm_action.grid(row=3, column=1, sticky="es", padx=10, pady=(100, 10))
btn_sort.pack(side=tkinter.RIGHT)

window.mainloop()  #keeps the event loop running and window open