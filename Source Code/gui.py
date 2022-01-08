# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

################
#tkinter terminology
#master = parent element
#relief = border style
#side = alignment (acts like float)
################

from os import stat
from tkinter import font
from music_sorter import Music_Sorter
import tkinter
import tkinter.font
from tkinter import filedialog
from tkinter.constants import DISABLED, LEFT, NORMAL, X
import eyed3

#get directory from field
def get_directory(directory_field):
    return directory_field.get()

#upon button click, opens file browser and puts selection in ent_directory
def browse():
    path = filedialog.askdirectory()
    ent_directory.insert(tkinter.END, path)

#run sorting file 
def call_sorter(sorter, directory_field, output):
    output.config(state=NORMAL)
    sorter.parent_dir = get_directory(directory_field)
    sorter.output_field = output
    sorter.file()
    if sorter.failed_counter == 0 and sorter.counter == 0:
        output.insert(tkinter.END, "\n>>There don't appear to be any .mp3 files here.\n>>Please double-check your directory.\n")
    elif sorter.failed_counter == 0:
        output.insert(tkinter.END, "\n>>All files sorted successfully.\n>>You may now close the window.\n")
        btn_sort.config(state=DISABLED)
    else:
        btn_next.config(state=NORMAL)
        output.insert(tkinter.END, "\n>>Click Next to address failed files.\n")
        btn_sort.config(state=DISABLED)
    output.config(state=DISABLED)

#destroy all objects in passed container (usually a frame)
def destroy_children(container):
    for item in container.winfo_children():
        item.destroy()

#move to next page to fill in metadata
def fill_in_page(frm_container, sorter):
    print("in fill_in_page")
    #destroy all items inside frm_container (start fresh)
    destroy_children(frm_container)
    

    #prepare constants
    list_dict = {
        "FILE_PATH": 0,
        "TITLE": 1,
        "ARTIST": 2,
        "ALBUM": 3,
        "YEAR": 4
    }

    #prepare 2d array that will hold data
    song_list = [] #file name, title, artist, album, year

    #variables to control rows
    row_index = 0 #row that it should be on (includes array locations)
    row_offset = 0 #offset to keep the array in bounds while changing GUI

    #instruction text and header font variable
    instructions = "These files were missing important metadata tags. \nThe Artist and Album tags are mandatory for filing. \nThe Year tag is optional. \nFill in these fields, then click 'Tag & File' to continue. \nFiles without Artist and Album information will not be sorted."
    header_font = tkinter.font.Font(size=11, weight="bold", underline=1)


    #create and pack instructions
    frm_text_blurb = tkinter.Frame(master=frm_container)
    frm_text_blurb.grid(row=row_index + row_offset, column=0, sticky="w", pady=(1,4))
    lbl_text_blurb = tkinter.Label(master=frm_text_blurb, text=instructions, justify=LEFT)
    lbl_text_blurb.pack(side=tkinter.LEFT)
    row_offset += 1

    #create headers columns
    frm_failed_song_header = tkinter.Frame(master=frm_container)
    frm_failed_song_header.grid(row=row_index + row_offset, column=0, pady=3, padx=2)
    lbl_failed_song_header = tkinter.Label(master=frm_failed_song_header, text="File Name", justify=LEFT, font=header_font)
    lbl_failed_song_header.pack(side=tkinter.LEFT)

    frm_title_header = tkinter.Frame(master=frm_container)
    frm_title_header.grid(row=row_index + row_offset, column=1, padx=2)
    lbl_title_header = tkinter.Label(master=frm_title_header, text="Song Name", justify=LEFT, font=header_font)
    lbl_title_header.pack(side=tkinter.LEFT)

    frm_artist_header = tkinter.Frame(master=frm_container)
    frm_artist_header.grid(row=row_index + row_offset, column=2, padx=2)
    lbl_artist_header = tkinter.Label(master=frm_artist_header, text="Artist", justify=LEFT, font=header_font)
    lbl_artist_header.pack(side=tkinter.LEFT)

    frm_album_header = tkinter.Frame(master=frm_container)
    frm_album_header.grid(row=row_index + row_offset, column=3, padx=2)
    lbl_album_header = tkinter.Label(master=frm_album_header, text="Album", justify=LEFT, font=header_font)
    lbl_album_header.pack(side=tkinter.LEFT)

    frm_year_header = tkinter.Frame(master=frm_container)
    frm_year_header.grid(row=row_index + row_offset, column=4, padx=2)
    lbl_year_header = tkinter.Label(master=frm_year_header, text="Year", justify=LEFT, font=header_font)
    lbl_year_header.pack(side=tkinter.LEFT)     

    row_offset += 1

    #create 1 row for each failed song; populate rows with fields/data 
    for failed_song in sorter.failed_songs:
        #get just file name
        file_name = failed_song[failed_song.rindex("\\")+1:]
        #get metadata from file, insert into song_list
        eyed3_file = eyed3.load(failed_song)
        try:
            song_list.append([  failed_song, 
                                eyed3_file.tag.title,
                                eyed3_file.tag.artist,
                                eyed3_file.tag.album,
                                eyed3_file.tag.getBestDate().year]) #Tag doesn't have a year attr.; but eyed3 has core.Date object with year attr.
        except Exception:
            song_list.append([  failed_song, 
                                eyed3_file.tag.title,
                                eyed3_file.tag.artist,
                                eyed3_file.tag.album,
                                None]) #If year doesn't exist. Otherwise causes error.
        
        print(song_list[row_index])

        #Create and pack file name
        frm_failed_song = tkinter.Frame(master=frm_container, width=60)
        frm_failed_song.grid(row=row_index + row_offset, column=0, sticky="w", pady=3, padx=2)
        lbl_song = tkinter.Label(master=frm_failed_song, text=file_name, justify=LEFT, width=60, anchor="w")
        lbl_song.pack(side=tkinter.LEFT, expand=False)
        #create and pack Title fields
        frm_title = tkinter.Frame(master=frm_container)
        frm_title.grid(row=row_index + row_offset, column=1, padx=2)
        ent_title = tkinter.Entry(master=frm_title, width=30)
        if song_list[row_index][list_dict["TITLE"]] != None:
            ent_title.insert(tkinter.END, song_list[row_index][list_dict["TITLE"]])
        ent_title.pack()
        #create and pack Artist fields
        frm_artist = tkinter.Frame(master=frm_container)
        frm_artist.grid(row=row_index + row_offset, column=2, padx=2)
        ent_artist = tkinter.Entry(master=frm_artist, width=30)
        if song_list[row_index][list_dict["ARTIST"]] != None:
            ent_artist.insert(tkinter.END, song_list[row_index][list_dict["ARTIST"]])
        ent_artist.pack()
        #create and pack Album fields
        frm_album = tkinter.Frame(master=frm_container)
        frm_album.grid(row=row_index + row_offset, column=3, padx=2)
        ent_album = tkinter.Entry(master=frm_album, width=30)
        if song_list[row_index][list_dict["ALBUM"]] != None:
            ent_album.insert(tkinter.END, song_list[row_index][list_dict["ALBUM"]])
        ent_album.pack()
        #create and pack Year fields
        frm_year = tkinter.Frame(master=frm_container)
        frm_year.grid(row=row_index + row_offset, column=4, padx=2)
        ent_year = tkinter.Entry(master=frm_year, width=12)
        if song_list[row_index][list_dict["YEAR"]] != None:
            ent_year.insert(tkinter.END, song_list[row_index][list_dict["YEAR"]])
        ent_year.pack()

        row_index += 1

    #add Tag & File button
    frm_action = tkinter.Frame(master=frm_container)
    frm_action.grid(row=row_index + row_offset, column=4, sticky="e", pady=3)
    btn_tag_file = tkinter.Button(master=frm_action, text="Tag & File", width=10, command=lambda: tag_and_file(sorter, song_list, frm_container))
    btn_tag_file.pack()

#get info from entry fields and update song_list[][]
def tag_and_file(sorter, song_list, frm_container):
    print("in tag_and_file")

    row_index = 0
    column_index = 1
    for frame in frm_container.winfo_children():
        if column_index > 4: #Year = 4, so we increment row and reset column
            row_index += 1
            column_index = 1
        if frame.winfo_class() == "Frame":
            for item in frame.winfo_children():
                if item.winfo_class() == "Entry":
                    print(item.get())
                    print(row_index)
                    print(column_index)
                    if item.get() == None:
                        song_list[row_index][column_index] = ""
                    else:
                        song_list[row_index][column_index] = item.get()
                    column_index += 1

    print(song_list)

    #clear container again
    destroy_children(frm_container)

    #create and pack output box
    frm_output = tkinter.Frame(master=frm_container)
    frm_output.grid(row=0, column=1, pady=3)
    txt_output = tkinter.Text(master=frm_output, width=120, height=25)
    scroll = tkinter.Scrollbar(master=frm_output, command=txt_output.yview)
    txt_output['yscrollcommand'] = scroll.set
    txt_output.pack()

    #create and pack buttons
    frm_buttons = tkinter.Frame(master=frm_container)
    frm_buttons.grid(row=1, column=1, sticky="e", pady=3)
    btn_close = tkinter.Button(master=frm_buttons, text="Close", width=10, command=lambda: window.destroy())
    btn_close.pack(side=tkinter.RIGHT)
    btn_tag_file = tkinter.Button(master=frm_buttons, text="Back", width=10,command=lambda: fill_in_page(frm_container, sorter))
    btn_tag_file.pack(side=tkinter.RIGHT)
    

    #reset sorter's variables
    sorter.output_field = txt_output
    sorter.failed_counter = 0
    sorter.counter = 0
    sorter.failed_songs = []

    #add new data and call file() again
    sorter.add_data(song_list)
    sorter.file()

    if sorter.failed_counter == 0:
        txt_output.insert(tkinter.END, "\n>>All files sorted successfully.\n>>You may now close the window.")
        btn_tag_file.config(state=DISABLED)
    else:
        txt_output.insert(tkinter.END, "\n>>Click 'Back' to investigate these files again or click 'Close' to leave them unfiled.")
    txt_output.config(state=DISABLED)
    
    


###### initial window stuff goes below ######

#creation of GUI items
window = tkinter.Tk() #creates window
window.title("MP3 Sorter")
window.geometry("1200x500") #width in pixels, not letters (width x height)

#create Music_Sorter class object
sorter = Music_Sorter()

#containing frame
frm_container = tkinter.Frame(master=window, relief=tkinter.RIDGE, borderwidth=2) #creates frame, assigns border type and width
frm_container.columnconfigure(1, minsize=100)

#intro text
frm_text0 = tkinter.Frame(master=frm_container)
lbl_text0 = tkinter.Label(master=frm_text0, text="Thank you for using this MP3 sorting tool. \n\nThis program is designed to target one folder and sort loose MP3 files into folders matching their artist and album tags. \n\nIt does not run recursively.\nIt will delete original files after moving them.\nBe certain before running that you want everything in the folder sorted. \nLeave the directory field blank to sort the current working directory.", justify=LEFT)

#folder entry and browse button
frm_directory0 = tkinter.Frame(master=frm_container)
frm_directory1 = tkinter.Frame(master=frm_container) #creates frame, assigns border type and width
lbl_directory = tkinter.Label(master=frm_directory0, text="Select a target directory:") #sets label
ent_directory = tkinter.Entry(master=frm_directory1, width=100) #creates text field
btn_directory = tkinter.Button(master=frm_directory1, text="Browse", command=browse, width=10)

#output box
frm_output = tkinter.Frame(master=frm_container)
txt_output = tkinter.Text(master=frm_output, width=95, height=13)
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