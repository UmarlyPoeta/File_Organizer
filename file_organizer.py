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


def create_directories(filtered_path):
    os.chdir(filtered_path)
    for file in list_of_extensions:
        Path(file).mkdir(exist_ok=True)

def move_files(path,filtered_path):
    os.chdir(path)
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".").upper()
        if file_extension != "":
            shutil.move(file, f"{filtered_path}\{file_extension}")

def main():
    path=get_path()
    print("Now we need you to enter a directory path, in which filtered files will go\n")
    filtered_path=get_path()
    try:
        os.chdir(path)
    except:
        print("Path does not exist")
        exit()
    get_extensions()
    
    create_directories(filtered_path)
    
    move_files(path,filtered_path)


if __name__=="__main__":
    main()