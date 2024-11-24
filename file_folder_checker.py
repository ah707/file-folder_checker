import tkinter as tk
import os

def check_path():
    path = entry.get()

    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]
    path = path.replace("\\", "/")
    
    if os.path.exists(path):
        if os.path.isfile(path):
            result_label.config(text="This is a file and it exists", fg="green")
        elif os.path.isdir(path):
            result_label.config(text="This is a folder and it exists", fg="blue")
    else:
        result_label.config("Path does not exist.", fg="red")

root = tk.Tk()
root.title("File/Folder Path Checker")
root.geometry("400x300")

tk.Label(root, text="Enter file or folder path:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Checker Path", command=check_path).pack(pady=5)

result_label = tk.Label(root, text="", font=("Verdana", 12))
result_label.pack(pady=10)

root.mainloop()


