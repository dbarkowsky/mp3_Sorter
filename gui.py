# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

################
#tkinter terminology
#master = parent element
#relief = border style
#side = alignment (acts like float)
################

from music_sorter import Music_Sorter
import tkinter
from tkinter import Scrollbar, filedialog
from tkinter.constants import DISABLED, EW, LEFT, NORMAL, RIGHT

#get directory from field
def get_directory(directory_field):
    return directory_field.get()

#upon button click, opens file browser and puts selection in ent_directory
def browse():
    path = filedialog.askdirectory()
    ent_directory.insert(tkinter.END, path)

#run sorting file 
def call_sorter(sorter, directory_field, output):
    sorter.parent_dir = get_directory(directory_field)
    sorter.output_field = output
    sorter.file()
    btn_next.config(state=NORMAL)

#move to next page to fill in metadata
def fill_in_page(frm_container, sorter):
    print("in fill_in_page")
    #destroy all items inside frm_container (start fresh)
    for item in frm_container.winfo_children():
        item.destroy()

    #create 1 row for each failed song; populate rows with fields/data
    row_index = 0
    for failed_song in sorter.failed_songs:
        file_name = failed_song[failed_song.rindex("\\")+1:]

        #Create and pack file name
        frm_failed_song = tkinter.Frame(master=frm_container)
        frm_failed_song.grid(row=row_index, column=0, sticky="w")
        lbl_song = tkinter.Label(master=frm_failed_song, text=file_name, justify=LEFT)
        lbl_song.pack(side=tkinter.LEFT)
        #create and pack Artist fields
        frm_artist = tkinter.Frame(master=frm_container)
        frm_artist.grid(row=row_index, column=1)
        ent_artist = tkinter.Entry(master=frm_artist)
        ent_artist.pack()
        #create and pack Album fields
        frm_album = tkinter.Frame(master=frm_container)
        frm_album.grid(row=row_index, column=2)
        ent_album = tkinter.Entry(master=frm_album)
        ent_album.pack()
        #create and pack Year fields
        frm_year = tkinter.Frame(master=frm_container)
        frm_year.grid(row=row_index, column=3)
        ent_year = tkinter.Entry(master=frm_year)
        ent_year.pack()

        row_index += 1
    
    


###### initial window stuff goes below ######

#creation of GUI items
window = tkinter.Tk() #creates window
window.title("MP3 Sorter")
window.geometry("775x500") #width in pixels, not letters (width x height)

#create Music_Sorter class object
sorter = Music_Sorter()

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

#output box
frm_output = tkinter.Frame(master=frm_container)
txt_output = tkinter.Text(master=frm_output, width=95, height=10)
txt_output.config(state=DISABLED)
txt_output.configure(font=("Consolas", 10))
scroll = tkinter.Scrollbar(master=frm_output, command=txt_output.yview)
txt_output['yscrollcommand'] = scroll.set

#Start button and next button
frm_action = tkinter.Frame(master=frm_container)
btn_sort = tkinter.Button(master=frm_action, text="Start", command=lambda: call_sorter(sorter, ent_directory,txt_output), width=10) #lambda format keeps method from calling at startup
btn_next = tkinter.Button(master=frm_action, text="Next", command=lambda: fill_in_page(frm_container, sorter), width=10)

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

#packing output box
frm_output.grid(row=3, column=1, sticky="ew", padx=10, pady=20)
txt_output.pack(side=tkinter.LEFT)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#packing start button
frm_action.grid(row=4, column=1, sticky="es", padx=10, pady=10)
btn_next.pack(side=tkinter.RIGHT)
btn_sort.pack(side=tkinter.RIGHT)
btn_next.config(state=DISABLED)

window.mainloop()  #keeps the event loop running and window open