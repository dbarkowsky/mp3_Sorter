# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

import eyed3
import os
import shutil

class Music_Sorter:

    #constructor using instance variables
    def __init__(self):
        self.parent_dir = os.getcwd()
        self.counter = 0

    def file(self):
        print("Target folder: " + self.parent_dir)
        #loop through files
        for song in os.listdir(self.parent_dir):
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
                    self.counter += 1

                    #delete original file
                    os.remove(song)
                        
                except :
                    print("File \"" + song + "\" does not have artist information. No action taken.")

        print("Moved " + str(self.counter) + " files into Artist folders.")


#assume running from target folder
#parent_dir = os.getcwd()
#print("Running in " + parent_dir)

#test cases
#test_sort = Music_Sorter()
#test_sort.parent_dir =  os.getcwd()
#test_sort.file()