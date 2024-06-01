import os
from pathlib import Path
import shutil
import customtkinter
import tkinter
import extensions
import tkinter.messagebox

# Global variables
list_of_extensions = []
root = customtkinter.CTk()
root.geometry("1000x500")
root.title(" FILE ORGANIZER")
organize_mode = customtkinter.StringVar(
    value="Organize by categories"
    )



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

label_of_the_organize_mode = customtkinter.CTkLabel(
    master=root,
    text=f"Choose the method of\n organizing your files:",
    font=("Roboto",20)
)
label_of_the_organize_mode.place(
    relx=0.8,
    rely=0.7,
    anchor = tkinter.CENTER
)

choser_of_the_organize_mode = customtkinter.CTkComboBox(
    root,
    width=300,
    values=["Organize by categories", "Organize by extensions"],
    variable=organize_mode
    )
choser_of_the_organize_mode.place(
    relx=0.8,
    rely=0.8,
    anchor=tkinter.CENTER
    )

# Main functionality
def main_functionality():
    
    path = entry_for_path.get()
    filtered_path = entry_for_direction_path.get()
    mode = choser_of_the_organize_mode.get()
 
    #checks if path exists
    try:
        os.chdir(filtered_path)
        os.chdir(path)
    except:
        error_box("The path does not exist")
        return None
    
    
    os.chdir(path)
    
    if mode == "Organize by extensions":
        get_extensions()
        create_directories(filtered_path)
        move_files(path,filtered_path)
        list_of_extensions.clear()
    else:    
        move_files_version_category(path,filtered_path)
    
    error_box("The files were organized")


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

# HANDLING ERRORS
def error_box(msg):
    window_for_error = tkinter.Tk()
    window_for_error.wm_withdraw()
    tkinter.messagebox.showinfo(title="Error", message=msg)
    window_for_error.destroy()
    return None

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
def check_which_folder_and_move(file_extension, file, filtered_path):
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
            check_which_folder_and_move(file_extension, file, filtered_path)
#




# __name__ check and tkinter mainloop
if __name__=="__main__":
    root.mainloop()    