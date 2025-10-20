import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

# Create main window
window = Tk()
window.title("Easy Cleaner")
window.geometry("500x300")

# Functions
selected_paths = []


#1
def select_files():
    global selected_paths
    selected_paths = filedialog.askopenfilenames(title="Select files to delete")
    if selected_paths:
        files_list.delete(0, END)
        for file in selected_paths:
            files_list.insert(END, file)

#2
def select_folder():
    global selected_paths
    folder = filedialog.askdirectory(title="Select folder to delete")
    if folder:
        selected_paths = [folder]
        files_list.delete(0, END)
        files_list.insert(END, folder)

#3
def delete_files():
    if not selected_paths:
        messagebox.showwarning("Warning", "No files or folders selected!")
        return




    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete the selected files/folders?")
    if confirm:
        for path in selected_paths:
            try:

                if os.path.isfile(path):
                    os.remove(path)

                elif os.path.isdir(path):
                    shutil.rmtree(path)


            except Exception as e:
                messagebox.showerror("Error", f"Cannot delete:\n{path}\n\n{e}")
        messagebox.showinfo("Done", "Selected files/folders have been deleted!")
        files_list.delete(0, END)
        selected_paths.clear()

# UI Layout
Label(window, text="File Cleaner", font=("Arial", 16, "bold")).pack(pady=10)

Button(window, text="Select Files", command=select_files, width=20).pack(pady=5)
Button(window, text="Select Folder", command=select_folder, width=20).pack(pady=5)
Button(window, text="Delete Selected", command=delete_files, width=20, bg="red", fg="white").pack(pady=5)

files_list = Listbox(window, width=45, height=8)
files_list.pack(pady=10)

window.mainloop()