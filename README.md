# File Organizer

## Overview

This Python script organizes files in a given directory by their extensions. It creates separate folders for each file extension and moves the corresponding files into these folders.

## Features

- Prompts the user to input a directory path.
- Scans the specified directory and identifies all file extensions.
- Creates a folder for each unique file extension.
- Moves files into their respective extension folders.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of using the command line or terminal.

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
    Enter the path:
    ```

3. **The script will:**
    - List all files in the specified directory along with their extensions.
    - Create directories named after the file extensions (e.g., `TXT`, `PDF`, `JPEG`).
    - Move each file into the corresponding directory based on its extension.

## Example

Given a directory with the following files:

```
document1.txt
image1.jpeg
presentation1.pdf
document2.txt
```

After running the script, the directory structure will be:

```
TXT/
    document1.txt
    document2.txt
JPEG/
    image1.jpeg
PDF/
    presentation1.pdf
```

## Code Explanation

```python
import os
from pathlib import Path
import shutil

# Prompt user to enter the path of the directory to organize
path = input("Enter the path: ")
list_of_extensions = []

# Change the current working directory to the specified path
os.chdir(path)

# Iterate over all files in the directory
for i in os.listdir():
    name, ext = os.path.splitext(i)  # Split the file name and its extension
    print(name, ext)
    list_of_extensions.append(ext.strip(".").upper())  # Collect unique extensions in uppercase

# Create directories for each unique file extension
for i in list_of_extensions:
    Path(i).mkdir(exist_ok=True)

# Move files into their respective directories based on their extensions
for i in os.listdir():
    name, ext = os.path.splitext(i)
    ext = ext.strip(".").upper()
    print(ext)
    if ext != "":
        shutil.move(i, ext)
```

### Key Modules Used

- `os`: Provides functions for interacting with the operating system, like changing directories and listing files.
- `pathlib`: Offers an object-oriented interface to handle filesystem paths.
- `shutil`: Contains high-level file operations, such as copying and moving files.

## Notes

- The script assumes that the provided path is valid and accessible.
- If the directory contains files with no extensions, they will not be moved.

## License

This project is licensed under the MIT License.

---

Feel free to modify and adapt the script to your needs. Contributions are welcome!