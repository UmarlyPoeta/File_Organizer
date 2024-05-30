import os
from pathlib import Path
import shutil
import customtkinter
import tkinter
import extensions

# Global variables
list_of_extensions = []
root = customtkinter.CTk()
root.geometry("1000x500")
root.title(" FILE ORGANIZER")


# GUI setup
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



Greeting = customtkinter.CTkLabel(
    master=root,
    text=f"Hello {os.getlogin()}",
    font=("Roboto",40)
    )
Greeting.place(
    relx=0.5,
    rely=0.1,
    anchor=tkinter.CENTER
    )

question_for_path = customtkinter.CTkLabel(
    master=root,
    text="Enter the path: ",
    font=("Roboto",20)
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
    font=("Roboto",20)
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

# Main functionality
def main_functionality():
    
    Issue_alert = customtkinter.CTkLabel(
        master=root,
        text=f"Path does not exist",
        font=("Roboto",24)
        )
    Success_alert = customtkinter.CTkLabel(
        master=root,
        text=f"The files were organized",
        font=("Roboto",24)
        )
    
    path = entry_for_path.get()
    filtered_path = entry_for_direction_path.get()
 
    #checks if path exists
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
    
    #get_extensions()

    #create_directories(filtered_path)

    move_files_version_category(path,filtered_path)
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
    font=("Roboto",20),
    command=main_functionality
    )
button_to_start_the_function.place(
    relx=0.5,
    rely=0.8,
    anchor=tkinter.CENTER
    )


# Helper functions
## EXTENSION VERSION
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

## CATEGORY VERSION
#automated
def check_which_folder_and_move2(file_extension, file, filtered_path):
    was_changed = False
    for ext_list_and_name in extensions.extensions:
        if file_extension in ext_list_and_name[0]:
            Path(ext_list_and_name[1]).mkdir(exist_ok=True)
            shutil.move(file, f"{filtered_path}\{ext_list_and_name[1]}")
            was_changed=True
            break
    if not was_changed:
        Path("OTHER").mkdir(exist_ok=True)
        shutil.move(file, f"{filtered_path}\OTHER")


def move_files_version_category(path,filtered_path):
    os.chdir(path)
    for file in os.listdir():
        file_extension = os.path.splitext(file)[1]
        file_extension = file_extension.strip(".")
        if file_extension != "":
            check_which_folder_and_move2(file_extension, file, filtered_path)
#


# __name__ check and tkinter mainloop
if __name__=="__main__":
    root.mainloop()    