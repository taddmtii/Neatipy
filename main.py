import os
import shutil

def get_download_files():
    """ Obtains files in Downloads folder and stores them in a list.

    Returns:
        List[string]: downloads_files
    """
    downloads_files = []
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    for filename in os.listdir(downloads_path):
        downloads_files.append(filename)
    return downloads_files

def filter_desktop_files():
    """ Obtains and filters all desktop files.

    Returns:
        List[List[string]]: desktop_files that gives all files filtered and , [0] = desktop_pointers, [1] = desktop_directories, [2] = desktop_files
    """
    desktop_pointers = []
    desktop_directories = []
    desktop_files = []
    all_desktop_files = []
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    for filename in os.listdir(desktop_path):
        root_extension_tuple = os.path.splitext(filename)
        name = root_extension_tuple[0] # Spotify
        extension = root_extension_tuple[1] # .url
        if (extension == ".url" or extension == ".lnk"): # if ext is shortcut or pointer.
            desktop_pointers.append([name, extension])
        elif (extension == ''): # if ext is dir
            desktop_directories.append(filename)
        else: # if ext is anything else.
            desktop_files.append(filename)
    all_desktop_files.append(desktop_pointers)
    all_desktop_files.append(desktop_directories)
    all_desktop_files.append(desktop_files)
    
    return all_desktop_files

if __name__ == "__main__":

    print("How can I help?")
    print("1. Clean Desktop Files")
    print("2. Display Downloads Folder")
    print("3. Clear Download Files") 

    choice = input()
    choice = int(choice)
    
    if choice == 1:
        try:
            desktop_files = filter_desktop_files()
        except:
            print("An error has occured and an exception was thrown.")
        else:
            print(desktop_files)
    elif choice == 2:
        download_files = get_download_files()
        print("Files and Directories in Downloads:")
        for file in download_files:
            print(file)
    elif choice == 3:
        download_files = get_download_files()
        if download_files == []:
            print("Nothing to delete, you're all cleaned up!")
        for file in download_files:
            path = os.path.join(r"C:\Users\taddt\Downloads", file)
            if os.path.exists(path):
                try:
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                        print("Directory " + file + " was successfully deleted.")
                        continue
                    os.remove(path)
                except:
                    print()
                    print(f"Exception was thrown on file {file}, moving onto next file.")
                else:
                    print("File " + file + " was successfully deleted.")

    #for num, file in list(enumerate(download_files)):
        #print(str(num + 1) + ": " + file)