# File Organizer

## Overview

This Python script is designed to organize files in a specified directory by moving them into subdirectories based on their file extensions or categories. The script features a graphical user interface (GUI) built with CustomTkinter.

## Features

- **Graphical User Interface (GUI)**: The program uses CustomTkinter to provide a user-friendly interface.
- **Organize by Extension or Category**: Files can be organized by their extensions or by predefined categories (e.g., documents, images, videos).
- **Error Handling**: The program checks for the existence of the provided paths and alerts the user if the path does not exist.

## Prerequisites

- Python 3.x installed on your system.
- The CustomTkinter and Tkinter libraries.
- A file named `extensions.py` containing predefined categories and their associated file extensions.

### Installing Required Libraries

You can install CustomTkinter using pip:

```bash
pip install customtkinter
```

Ensure you also have Tkinter installed, which is usually included with Python installations.

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

3. **Ensure you have the `extensions.py` file in the same directory as the script.**

## Usage

1. **Run the script:**

    ```bash
    python file_organizer.py
    ```

2. **Enter the required paths in the GUI:**

    - **Source Directory**: The path to the directory containing the files you want to organize.
    - **Destination Directory**: The path to the directory where the organized files will be moved.

3. **Click the "START" button to begin organizing the files.**

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

The script is divided into several functions for better readability and maintainability:

```python
import os
from pathlib import Path
import shutil
import customtkinter
import tkinter
import extensions

list_of_extensions = []
root = customtkinter.CTk()
root.geometry("1000x500")
root.title("FILE ORGANIZER")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

Greeting = customtkinter.CTkLabel(
    master=root,
    text=f"Hello {os.getlogin()}",
    font=("Roboto", 40)
)
Greeting.place(
    relx=0.5,
    rely=0.1,
    anchor=tkinter.CENTER
)

question_for_path = customtkinter.CTkLabel(
    master=root,
    text="Enter the path: ",
    font=("Roboto", 20)
)
question_for_path.place(
    relx=0.5,
    rely=0.2,
    anchor=tkinter.CENTER
)

entry_for_path = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Enter the path to a directory with files to organize",
    width=350,
    height=30,
    corner_radius=15
)
entry_for_path.place(
    relx=0.5,
    rely=0.3,
    anchor=tkinter.CENTER
)

question_for_path = customtkinter.CTkLabel(
    master=root,
    text="Now we need you to enter a directory path,\n in which filtered files will go:\n",
    font=("Roboto", 20)
)
question_for_path.place(
    relx=0.5,
    rely=0.5,
    anchor=tkinter.CENTER
)

entry_for_direction_path = customtkinter.CTkEntry(
    master=root,
    placeholder_text="Enter the path to a direction directory",
    width=350,
    height=30,
    corner_radius=15
)
entry_for_direction_path.place(relx=0.5,
                               rely=0.6,
                               anchor=tkinter.CENTER
                               )

def main_functionality():
    Issue_alert = customtkinter.CTkLabel(
        master=root,
        text=f"Path does not exist",
        font=("Roboto", 24)
    )
    Success_alert = customtkinter.CTkLabel(
        master=root,
        text=f"The files were organized",
        font=("Roboto", 24)
    )

    path = entry_for_path.get()
    filtered_path = entry_for_direction_path.get()

    try:
        os.chdir(filtered_path)
        os.chdir(path)
    except:
        Issue_alert.place(
            relx=0.5,
            rely=0.9,
            anchor=tkinter.CENTER
        )
        return None

    Issue_alert.place_forget()
    Success_alert.place_forget()

    os.chdir(path)

    move_files_version_category(path, filtered_path)
    Success_alert.place(
        relx=0.5,
        rely=0.9,
        anchor=tkinter.CENTER
    )


button_to_start_the_function = customtkinter.CTkButton(
    master=root,
    width=200,
    height=60,
    text="START",
    font=("Roboto", 20),
    command=main_functionality
)
button_to_start_the_function.place(
    relx=0.5,
    relx=0.8,
    anchor=tkinter.CENTER
)

def get_extensions():
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        list_of_extensions.append(file_extension.strip(".").upper())

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
            shutil.move(file, f"{filtered_path}\{file_extension}")

def check_which_folder_and_move2(file_extension, file, filtered_path):
    was_changed = False
    for ext_list_and_name in extensions.extensions:
        if file_extension in ext_list_and_name[0]:
            Path(ext_list_and_name[1]).mkdir(exist_ok=True)
            shutil.move(file, f"{filtered_path}\{ext_list_and_name[1]}")
            was_changed = True
            break
    if not was_changed:
        Path("OTHER").mkdir(exist_ok=True)
        shutil.move(file, f"{filtered_path}\OTHER")

def move_files_version_category(path, filtered_path):
    os.chdir(path)
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".")
        if file_extension != "":
            check_which_folder_and_move2(file_extension, file, filtered_path)

if __name__ == "__main__":
    root.mainloop()
```

### Function Descriptions

- **get_path(prompt)**: Pobiera ścieżkę od użytkownika na podstawie przekazanego komunikatu.
- **get_extensions()**: Skanuje katalog źródłowy i zbiera rozszerzenia plików.
- **create_directories(filtered_path)**: Tworzy katalogi na podstawie zebranych rozszerzeń plików w katalogu docelowym.
- **move_files(path, filtered_path)**: Przenosi pliki z katalogu źródłowego do odpowiednich katalogów w katalogu docelowym.
- **check_which_folder_and_move2(file_extension, file, filtered_path)**: Sprawdza, do jakiego folderu przenieść plik na podstawie jego rozszerzenia.
- **move_files_version_category(path, filtered_path)**: Przenosi pliki z katalogu źródłowego do odpowiednich katalogów w katalogu docelowym na podstawie kategorii.

### Key Modules Used

- `os`: Provides functions for interacting with the operating system, like changing directories and listing files.
- `pathlib`: Offers an object-oriented interface to handle filesystem paths.
- `shutil`: Contains high-level file operations, such as copying and moving files.
- `customtkinter` and `tkinter`: Used for creating the graphical user interface.

## Notes

- The script assumes that the provided paths are valid and accessible.
- Ensure that the destination directory exists and is writable.
- If the directory contains files with no extensions, they will be moved to an "OTHER" directory.

## License

This project is licensed under the MIT License.