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
    """ Obtains and filters all desktop files into three seperate categories:
        Shortcuts, Directories, and Files.

    Returns:
        List[List[string]]: desktop_files, [0] = desktop_pointers, [1] = desktop_directories, [2] = desktop_files
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

    while (True):
        print("How can I help? (type e to exit Neatipy)")
        print("1. Organize Desktop Files and Folders")
        print("2. Display Downloads Folder")
        print("3. Clear Download Files")
        print("4. Clear Desktop Files")

        choice = input()
        if choice == "e":
            break
        
        choice = int(choice)
        
        if choice == 1:
            warning = input("Warning: this is a destrutive action. Would you like to proceed?: (y or n)")
            if warning == 'y':    
                try:
                    desktop_files = filter_desktop_files()
                except:
                    print("An error has occured when fetching and filtering desktop files and an exception was thrown.")
                else:
                    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                    directory_path_shortcuts = os.path.join(desktop_path, "Shortcuts")
                    if not os.path.exists(directory_path_shortcuts):
                        os.mkdir(directory_path_shortcuts)
                    else:
                        shutil.rmtree(directory_path_shortcuts)
                        os.mkdir(directory_path_shortcuts)
                        
                    directory_path_directories = os.path.join(desktop_path, "Directories")
                    if not os.path.exists(directory_path_directories):
                        os.mkdir(directory_path_directories)
                    else:
                        shutil.rmtree(directory_path_directories)
                        os.mkdir(directory_path_directories)
                        
                    directory_path_files = os.path.join(desktop_path, "Files")
                    if not os.path.exists(directory_path_files):
                        os.mkdir(directory_path_files)
                    else:
                        shutil.rmtree(directory_path_files)
                        os.mkdir(directory_path_files)
                # Add Files to each Directory
                for shortcut in desktop_files[0]: #shortcuts
                    path = f"{desktop_path}\{shortcut[0]}{shortcut[1]}"
                    shutil.copy(path, directory_path_shortcuts) #shortcuts / pointers go to shortcuts folder
                for directory in desktop_files[1]:
                    path = f"{desktop_path}\{directory}"
                    directory_path = directory_path_directories + r"\\" + directory
                    shutil.copytree(path, directory_path) #shortcuts / pointers go to shortcuts folder
                 
            elif warning == 'n':
                print("Operation Cancelled")
                continue
            else:
                print("Invalid input... back to main menu")
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