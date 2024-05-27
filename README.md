# File Organizer

## Overview

This Python script organizes files in a specified directory by their extensions. It creates separate folders for each file extension in a user-defined directory and moves the corresponding files into these folders.

## Features

- Prompts the user to input a directory path containing the files to be organized.
- Prompts the user to input a directory path where the organized files will be stored.
- Scans the specified source directory and identifies all file extensions.
- Creates a folder for each unique file extension in the specified destination directory.
- Moves files into their respective extension folders in the destination directory.

## Prerequisites

- Python 3.x installed on your system.
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

## Usage

1. **Run the script:**

    ```bash
    python file_organizer.py
    ```

2. **Enter the path to the directory you want to organize when prompted:**

    ```
    Enter the path: /path/to/source/directory
    ```

3. **Enter the path to the directory where you want the organized files to be moved:**

    ```
    Enter the path: /path/to/destination/directory
    ```

4. **The script will:**
    - List all files in the specified source directory along with their extensions.
    - Create directories named after the file extensions in the specified destination directory.
    - Move each file into the corresponding directory based on its extension in the destination directory.

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

def move_files(path, filtered_path):
    os.chdir(path)
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".").upper()
        if file_extension != "":
            shutil.move(file, f"{filtered_path}\\{file_extension}")

def main():
    path = get_path()
    print("Now we need you to enter a directory path, in which filtered files will go\n")
    filtered_path = get_path()
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Path does not exist")
        exit()
    get_extensions()
    create_directories(filtered_path)
    move_files(path, filtered_path)

if __name__ == "__main__":
    main()
```

### Function Descriptions

- **get_path()**: Prompts the user to enter a directory path.
- **get_extensions()**: Scans the source directory and collects file extensions.
- **create_directories(filtered_path)**: Creates directories based on the collected file extensions in the destination directory.
- **move_files(path, filtered_path)**: Moves files from the source directory to their respective extension directories in the destination directory.
- **main()**: Orchestrates the execution of the above functions and handles the main workflow.

### Key Modules Used

- `os`: Provides functions for interacting with the operating system, like changing directories and listing files.
- `pathlib`: Offers an object-oriented interface to handle filesystem paths.
- `shutil`: Contains high-level file operations, such as copying and moving files.

## Notes

- The script assumes that the provided paths are valid and accessible.
- Ensure that the destination directory exists and is writable.
- If the directory contains files with no extensions, they will not be moved.

## License

This project is licensed under the MIT License.

---

Feel free to modify and adapt the script to your needs. Contributions are welcome!