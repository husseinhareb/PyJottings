import tkinter as tk
from ttkbootstrap import Style, Button, LabelFrame, Window

def open_new_window():
    add_note = tk.Toplevel(root)
    add_note.title("addnote")
    add_note.geometry('200x200')
    note = tk.StringVar()

    # Create the Entry widget using tk.Entry
    note_entry = tk.Entry(add_note, textvariable=note)
    note_entry.pack()
root = Window(themename="superhero")
root.title("PyJottings")
root.geometry('300x660+40+40')

style = Style('superhero')

settings_frame = LabelFrame(root,
                            text="Settings",
                            width=80,
                            height=640)
settings_frame.pack(pady=10, padx=10)
settings_frame.place(x=10, y=10)

add_button = Button(settings_frame,
                    text="+",
                    command=open_new_window)
add_button.pack(pady=10, padx=10)

root.mainloop()
