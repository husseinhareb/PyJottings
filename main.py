import tkinter as tk
from ttkbootstrap import Style, Button, LabelFrame, Window

def add_note():
    add_note = tk.Toplevel(root)
    add_note.title("addnote")
    add_note.geometry('200x200')
    note = tk.StringVar()

    # Create the Entry widget using tk.Entry
    note_entry = tk.Entry(add_note, textvariable=note)
    note_entry.pack(padx = 10,pady=10)
    note_accept = tk.Button(add_note,
                    text="",
                    )
    note_accept.pack()
    note_cancel = tk.Button(add_note,
                   text="",
                    )
    note_cancel.pack()

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
                    command=add_note)
add_button.pack(pady=10, padx=10)

root.mainloop()
