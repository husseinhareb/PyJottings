import tkinter as tk
import sqlite3
from ttkbootstrap import Style, Button, LabelFrame, Window


def create_database():
    db = sqlite3.connect('notes.db')
    cursor =db.cursor()

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

def display_notes():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    for note in notes:
        note_label = tk.Label(root, text=note[2])  # Note content is at index 2
        note_label.pack()

    db.close()
    root.after(1000,display_notes)

def clear_notes():
    db=sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes')

    db.commit()
    db.close()


def add_note():
    def save_note():
        note_text = note_var.get()
        add_note_to_db(note_text)
        add_note.destroy()

    # Update the displayed notes after adding a new note
    display_notes()
    
    add_note = tk.Toplevel(root)
    add_note.title("addnote")
    add_note.geometry('200x200')
    note_var = tk.StringVar()
    # Create the Entry widget using tk.Entry
    note_entry = tk.Entry(add_note, 
                          textvariable=note_var)
    note_entry.pack(padx = 10,pady=10)

    note_accept = tk.Button(add_note,
                            text="",
                            command=save_note
                            )
    note_accept.pack()
    note_cancel = tk.Button(add_note,
                            text="",
                            command=add_note.destroy
                            )
    note_cancel.pack()

create_database()

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

clear_button = Button(settings_frame,
                      text="",
                      command=clear_notes)
clear_button.pack()
display_notes()
root.mainloop()
