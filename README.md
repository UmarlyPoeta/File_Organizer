# File Organizer

## Overview

This Python script organizes files in a specified directory by their extensions through a graphical user interface (GUI). It creates separate folders for each file extension in a user-defined directory and moves the corresponding files into these folders.

## Features

- Graphical User Interface (GUI) using CustomTkinter.
- Prompts the user to input a source directory path containing the files to be organized.
- Prompts the user to input a destination directory path where the organized files will be stored.
- Scans the specified source directory and identifies all file extensions.
- Creates a folder for each unique file extension in the specified destination directory.
- Moves files into their respective extension folders in the destination directory.
- Provides feedback on whether the operation was successful or if there was an error with the provided paths.

## Prerequisites

- Python 3.x installed on your system.
- Install required libraries:
  - `customtkinter`
  - `tkinter`
- Basic knowledge of using the command line or terminal.
- Ensure the destination directory exists and is writable.

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone <repository_url>
    ```

    or download the script file directly.

2. **Navigate to the directory containing the script:**

    ```bash
    cd path_to_script_directory
    ```

3. **Install the required packages:**

    ```bash
    pip install customtkinter
    ```

## Usage

1. **Run the script:**

    ```bash
    python file_organizer_gui.py
    ```

2. **Follow the on-screen prompts:**

    - Enter the path to the directory you want to organize in the first entry box.
    - Enter the path to the directory where you want the organized files to be moved in the second entry box.

3. **Click the "Enter to start" button:**

    - The script will scan the source directory, create directories in the destination directory based on file extensions, and move files accordingly.
    - If the provided source path does not exist, an alert will be displayed.

## Example

Given a source directory with the following files:

```
document1.txt
image1.jpeg
presentation1.pdf
document2.txt
```

And specifying `D:\FILE_ORGANIZER` as the destination directory, after running the script, the directory `D:\FILE_ORGANIZER` will have the following structure:

```
D:\FILE_ORGANIZER\
    TXT\
        document1.txt
        document2.txt
    JPEG\
        image1.jpeg
    PDF\
        presentation1.pdf
```

## Code Explanation

The script is divided into several functions and a GUI setup for better readability and maintainability:

```python
import os
from pathlib import Path
import shutil
import customtkinter
import tkinter

# Global variables and GUI setup
list_of_extensions = []
root = customtkinter.CTk()
root.geometry("1000x500")
root.title("FILE ORGANIZER")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

Greeting = customtkinter.CTkLabel(master=root, text=f"Hello {os.getlogin()}", font=("Roboto", 24))
Greeting.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

question_for_path = customtkinter.CTkLabel(master=root, text="Enter the path: ", font=("Roboto", 20))
question_for_path.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

Entry_for_path = customtkinter.CTkEntry(master=root, width=280, height=30, corner_radius=15)
Entry_for_path.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

question_for_path = customtkinter.CTkLabel(master=root, text="Now we need you to enter a directory path, in which filtered files will go:", font=("Roboto", 20))
question_for_path.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Entry_for_direction_path = customtkinter.CTkEntry(master=root, width=280, height=30, corner_radius=15)
Entry_for_direction_path.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

# Main functionality
def main_functionality():
    Issue_alert = customtkinter.CTkLabel(master=root, text="Path does not exist", font=("Roboto", 24))
    Success_alert = customtkinter.CTkLabel(master=root, text="The files were organized", font=("Roboto", 24))
    
    path = Entry_for_path.get()
    filtered_path = Entry_for_direction_path.get()
    try:
        os.chdir(path)
    except FileNotFoundError:
        Issue_alert.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        return None
    Issue_alert.place_forget()
    get_extensions()
    create_directories(filtered_path)
    move_files(path, filtered_path)
    Success_alert.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

button_to_start_the_function = customtkinter.CTkButton(master=root, fg_color="lightgray", width=200, height=60, text="Enter to start", font=("Roboto", 20), text_color="black", command=main_functionality)
button_to_start_the_function.place(relx=0.5, relx=0.8, anchor=tkinter.CENTER)

# Helper functions
def get_extensions():
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]  # Split the file name and its extension
        list_of_extensions.append(file_extension.strip(".").upper())  # Collect unique extensions in uppercase

def create_directories(filtered_path):
    os.chdir(filtered_path)
    for file in list_of_extensions:
        Path(file).mkdir(exist_ok=True)

def move_files(path, filtered_path):
    os.chdir(path)
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".").upper()
        if file_extension != "":
            shutil.move(file, f"{filtered_path}\\{file_extension}")

if __name__ == "__main__":
    root.mainloop()
```

### Function Descriptions

- **get_path()**: Prompts the user to enter a directory path.
- **get_extensions()**: Scans the source directory and collects file extensions.
- **create_directories(filtered_path)**: Creates directories based on the collected file extensions in the destination directory.
- **move_files(path, filtered_path)**: Moves files from the source directory to their respective extension directories in the destination directory.
- **main_functionality()**: Orchestrates the execution of the above functions and handles the main workflow, including GUI interactions.

### Key Modules Used

- `os`: Provides functions for interacting with the operating system, like changing directories and listing files.
- `pathlib`: Offers an object-oriented interface to handle filesystem paths.
- `shutil`: Contains high-level file operations, such as copying and moving files.
- `customtkinter`: Provides advanced and customizable widgets for the GUI.
- `tkinter`: Standard Python interface to the Tk GUI toolkit.

## Notes

- The script assumes that the provided paths are valid and accessible.
- Ensure that the destination directory exists and is writable.
- If the directory contains files with no extensions, they will not be moved.

## License

This project is licensed under the MIT License.

---

Feel free to modify and adapt the script to your needs. Contributions are welcome!
