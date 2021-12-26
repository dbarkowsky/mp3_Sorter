# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

from tkinter.constants import NORMAL
import eyed3
import os
import shutil
import tkinter

class Music_Sorter:

    #constructor using instance variables
    def __init__(self):
        self.parent_dir = os.getcwd()
        self.counter = 0 #counts files sorted
        self.output_field = tkinter.Text() #for gui output
        self.failed_songs = []  #list for songs that failed to sort (missing info?)
        self.failed_counter = 0 #counts failures

    def file(self):
        print("Target folder: " + self.parent_dir)
        self.output_field.config(state=NORMAL)
        self.output_field.insert(tkinter.END, ">>Target folder: " + self.parent_dir)
        #loop through files
        for song in os.listdir(self.parent_dir):
            just_song = song
            song = self.parent_dir + "/" + song
            print("for loop entered for " + song)
            #if file and mp3
            if os.path.isfile(song) and song.endswith(".mp3"):
                print(song + " is loaded")
                #give file to eyeD3
                file_name = eyed3.load(song)

                try:
                    #get artist name
                    artist = file_name.tag.artist
                    print(artist)
                    
                    #check if folder exists
                    if os.path.isdir(artist):
                        print(artist + " folder already exists")
                        folder = os.path.join(self.parent_dir, artist)
                    else:
                        #create folder from artist name
                        folder = os.path.join(self.parent_dir, artist)
                        os.mkdir(folder)
                        print("Creating " + folder)

                    #copy file
                    shutil.copy2(song,folder)
                    print("Filed " + song + " successfully.")
                    self.output_field.insert(tkinter.END, "\n>>Filed " + just_song + " in " + artist + " folder.")
                    self.counter += 1

                    #delete original file
                    os.remove(song)
                        
                except :
                    print("File \"" + song + "\" does not have artist information. No action taken.")
                    self.output_field.insert(tkinter.END, "\n>>File \"" + just_song + "\" does not have artist information. No action taken.")
                    self.failed_songs.append(song)
                    self.failed_counter += 1

        print("Moved " + str(self.counter) + " files into Artist folders.")
        self.output_field.insert(tkinter.END, "\n>>Moved " + str(self.counter) + " file(s) into Artist folders.")
        self.output_field.insert(tkinter.END, "\n>>" + str(self.failed_counter) + " song(s) failed to file properly.")