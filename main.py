import tkinter as tk
import sqlite3
from ttkbootstrap import Style, Button, LabelFrame, Window

def create_database():
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    db.commit()
    db.close()

def add_note_to_db(note):
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', ('Untitled', note))

    db.commit()
    db.close()

import textwrap

# ... (other code remains the same)

def display_notes(note_container):
    for widget in note_container.winfo_children():
        widget.destroy()

    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    for idx, note in enumerate(notes, start=1):
        note_frame = tk.Frame(note_container, relief=tk.RIDGE, borderwidth=2)
        note_frame.pack(pady=5, padx=10, fill=tk.X)

        # Wrap the text using textwrap
        wrapped_note = textwrap.fill(note[2], width=18)

        note_label = tk.Label(note_frame, text=f"{idx}. {wrapped_note}", justify="left")
        note_label.pack(pady=5, padx=0)

    db.close()

    root.after(1000, lambda: display_notes(note_container))


def clear_notes():
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes')

    db.commit()
    db.close()

def add_note():
    def save_note():
        note_text = note_var.get()
        add_note_to_db(note_text)
        add_note.destroy()

    add_note = tk.Toplevel(root)
    add_note.title("addnote")
    add_note.geometry('250x100')
    note_var = tk.StringVar()

    note_label = tk.Label(add_note, text="Enter your note:")
    note_label.pack()
    note_entry = tk.Entry(add_note, textvariable=note_var, width=30)
    note_entry.pack(pady=5)

    button_frame = tk.Frame(add_note)
    button_frame.pack(pady=5)

    note_accept = tk.Button(button_frame, text="", command=save_note)
    note_accept.pack(side=tk.LEFT)

    note_cancel = tk.Button(button_frame, text="", command=add_note.destroy)
    note_cancel.pack(side=tk.LEFT)

create_database()

root = Window(themename="superhero")
root.title("PyJottings")
root.geometry('300x660+40+40')

style = Style('superhero')
settings_frame = LabelFrame(root, text="Settings", width=80, height=640)
settings_frame.pack(pady=10, padx=10)
settings_frame.place(x=10, y=10)

add_button = Button(settings_frame, text="+", command=add_note)
add_button.pack(pady=10, padx=10)

delete_button = Button(settings_frame, text="󰗨", command=clear_notes)
delete_button.pack(pady=10, padx=10)

edit_button = Button(settings_frame, text="󰤌")
edit_button.pack(pady=10, padx=10)

reminder_button = Button(settings_frame, text="󰀠")
reminder_button.pack(pady=10, padx=10)

clear_button = Button(settings_frame, text="", command=clear_notes)
clear_button.pack( pady=10, padx=10)

exit_button = Button(settings_frame, text="󰍃", command=root.destroy)
exit_button.pack( pady=10, padx=10)

# Create a container frame for notes
notes_container = tk.Frame(root)
notes_container.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

display_notes(notes_container)

root.mainloop()
