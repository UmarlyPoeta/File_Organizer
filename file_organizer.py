import os
from pathlib import Path
import shutil

list_of_extensions = []

def get_path():
    return input("Enter the path: ")


def get_extensions():
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]  # Split the file name and its extension
        list_of_extensions.append(file_extension.strip(".").upper())  # Collect unique extensions in uppercase


def create_directories():
    for file in list_of_extensions:
        Path(file).mkdir(exist_ok=True)

def move_files():
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".").upper()
        if file_extension != "":
            shutil.move(file, file_extension)

def main():
    try:
        os.chdir(get_path)
    except:
        print("Path does not exist")
        exit()
    
    get_extensions()
    
    create_directories()
    
    move_files()


if __name__=="__main__":
    main()