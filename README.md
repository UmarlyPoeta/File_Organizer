# File Organizer

## Overview

The **File Organizer** is a Python-based GUI application designed to help you organize your files efficiently. Using a simple and intuitive interface, you can categorize and move your files into specified directories based on their extensions or predefined categories.

## Features

- Organize files by their extensions.
- Organize files by predefined categories.
- Simple and intuitive GUI built using `customtkinter`.
- Dark mode appearance for a sleek user experience.

## Installation

To run the File Organizer, ensure you have the following dependencies installed:

- Python 3.x
- `customtkinter` library
- `tkinter` library
- `extensions` module (ensure it contains the category definitions for organizing files)

You can install `customtkinter` using pip:

```bash
pip install customtkinter
```

## Usage

1. **Clone the repository or download the script:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the script:**
   ```bash
   python file_organizer.py
   ```

3. **Using the GUI:**
   - Enter the path to the directory containing the files you want to organize.
   - Enter the path to the directory where the organized files will be moved.
   - Choose the method of organization: by extensions or by predefined categories.
   - Click the "START" button to begin organizing your files.

## GUI Layout

- **Greeting:** Displays a welcome message with your username.
- **Path Input:** Two fields to enter the source directory and the target directory paths.
- **Organization Method:** A dropdown to select the method of organization.
- **Start Button:** Initiates the file organization process.

## Example

1. **Organize by Extensions:**
   - All files with the same extension (e.g., .txt, .jpg) will be moved to corresponding directories named after their extensions.

2. **Organize by Categories:**
   - Files are moved into predefined categories such as `Documents`, `Images`, `Videos`, etc., based on their extensions as defined in the `extensions` module.

## Helper Functions

- **get_extensions():** Collects unique file extensions from the source directory.
- **create_directories(filtered_path):** Creates directories in the target path based on collected extensions.
- **move_files(path, filtered_path):** Moves files to directories based on their extensions.
- **check_which_folder_and_move(file_extension, file, filtered_path):** Moves files to predefined category directories.
- **move_files_version_category(path, filtered_path):** Organizes and moves files into category directories.

## `extensions` Module

Ensure you have an `extensions` module that defines the categories for file organization. An `extensions.py` might look like this:

```python

text_formats_extensions = [
    "doc",
    "docx",
    "odt",
    "pdf",
    "rtf",
    "tex",
    "txt",
    "wpd"
]
video_extensions = [
    "3g2",
    "3gp",
    "avi",
    "flv",
    "h264",
    "m4v",
    "mkv",
    "mov",
    "mp4",
    "mpg",
    "mpeg",
    "rm",
    "swf",
    "vob",
    "webm",
    "wmv"
]

...
...
...

# extensions = lists contating each category of extensions / Name of the directory
extensions = [
    [text_formats_extensions,"DOCUMENTS"],
    [video_extensions,"VIDEOS"],
    [compressed_extensions,"COMPRESSED"],
    [internet_related_extensions,"INTERNET RELATED FILES"],
    [image_extensions,"IMAGES"],
    [exec_extensions,"EXECS"],
    [disk_extensions,"DISK RELATED FILES"],
    [audio_extensions,"AUDIO FILES"],
    [system_related_extensions,"SYSTEM RELATED FILES"],
    [spreadsheet_extensions,"SPREADSHEETS"],
    [presentation_extensions,"PRESENTATIONS"],
    [fonts_extensions,"FONTS"],
    [data_extensions,"DATA FILES"]
]
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to contribute to this project by submitting issues or pull requests. Enjoy organizing your files with ease!
