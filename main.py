import os
import shutil
import sys 

def get_download_files():
    """Obtains files in Downloads folder and stores them in a list.

    Returns:
        List[string]: List of files in the Downloads folder.
    """
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    return os.listdir(downloads_path)

def clear_downloads():
    """Clears all files and directories in the Downloads folder."""
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    for item in os.listdir(downloads_path):
        item_path = os.path.join(downloads_path, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Directory '{item}' was successfully deleted.")
            else:
                os.remove(item_path)
                print(f"File '{item}' was successfully deleted.")
        except Exception as e:
            print(f"Failed to delete '{item}': {e}")

if __name__ == "__main__":
    files = get_download_files()
    print("Current content in downloads:")
    print("--------------------------------------")
    for file in files:
        print(f"File or Directory: {file}")
    print("--------------------------------------")
    choice = input("Are you sure?: (y or n) ")
    if choice == 'y':
        try:
            clear_downloads()
        except:
            print("Something went wrong.")
        else:
            print("Downloads folder has been successfully cleared.")
    sys.exit()