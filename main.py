import os

desktop_pointers = []
desktop_directories = []
desktop_files = []


def get_desktop_files(pointers, directories, files):
    #get path for desktop; 
    #expanduser('~') returns home directory of current user
    #join() joins home directory with Desktop to get full path.
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    #Loop over Desktop Files
    for filename in os.listdir(desktop_path): #returns list of all files and directories in desktop folder.
        #new_filename = os.path.join(desktop_path, filename)
        #print(filename)
        root_extension_tuple = os.path.splitext(filename)
        #print(filename)
        name = root_extension_tuple[0] # Spotify
        extension = root_extension_tuple[1] # .url
        if (extension == ".url" or extension == ".lnk"): # if ext is shortcut or pointer.
            desktop_pointers.append([name, extension])
        elif (extension == ''): # if ext is dir
            desktop_directories.append(filename)
        else: # if ext is anything else.
            desktop_files.append(filename)
        
    print("Directories: \n")
    for directory in desktop_directories:
       print(directory)
    
    print("Shortcuts: \n")
    for name, extension in desktop_pointers:
        print("Name: " + name + "\n" "Extension: " + extension)

    print("Files: \n")
    for file in desktop_files:
        print(file)

if __name__ == "__main__":
    get_desktop_files(desktop_pointers, desktop_directories, desktop_files)
