# C:\Users\Dylan\AppData\Local\Programs\Python\Python310

import eyed3
import os
import shutil

counter = 0

#assume running from target folder
parent_dir = os.getcwd()
print("Running in " + parent_dir)

#loop through files
for path in os.listdir(parent_dir):
    #if file and mp3
    if os.path.isfile(path) and path.endswith(".mp3"):
        #give file to eyeD3
        file_name = eyed3.load(path)

        try:
            #get artist name
            artist = file_name.tag.artist
            ######print(artist)
            
            #check if folder exists
            if os.path.isdir(artist):
                print(artist + " folder already exists")
                folder = os.path.join(parent_dir, artist)
            else:
                #create folder from artist name
                folder = os.path.join(parent_dir, artist)
                os.mkdir(folder)
                print("Creating " + folder)

            #copy file
            shutil.copy2(path,folder)
            print("Filed " + path + " successfully.")
            counter += 1

            #delete original file
            os.remove(path)
                
        except :
            print("File \"" + path + "\" does not have artist information. No action taken.")

print("Moved " + str(counter) + " files into Artist folders.")