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

        note_label = tk.Label(note_frame, text=f"{idx}. {note[2]}", wraplength=220, justify="left")
        note_label.pack(pady=5, padx=10)

        delete_button = tk.Button(note_frame, text="Delete", command=lambda i=note[0]: delete_note(i))
        delete_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(note_frame, text="Edit", command=lambda i=note[0], c=note[2]: edit_note(i, c))
        edit_button.pack(side=tk.LEFT, padx=5)

    db.close()

    root.after(1000, lambda: display_notes(note_container))

def clear_notes():
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes')

    db.commit()
    db.close()

def delete_note(note_id):
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))

    db.commit()
    db.close()

def edit_note(note_id, current_content):
    def save_edit():
        new_content = edit_var.get()
        db = sqlite3.connect('notes.db')
        cursor = db.cursor()

        cursor.execute('UPDATE notes SET content = ? WHERE id = ?', (new_content, note_id))

        db.commit()
        db.close()
        edit_note_window.destroy()
        display_notes(notes_container)  

    edit_note_window = tk.Toplevel(root)
    edit_note_window.title("editnote")
    edit_note_window.geometry('250x100')
    edit_var = tk.StringVar(value=current_content)

    edit_label = tk.Label(edit_note_window, text="Edit your note:")
    edit_label.pack()
    edit_entry = tk.Entry(edit_note_window, textvariable=edit_var, width=30)
    edit_entry.pack(pady=5)

    edit_button_frame = tk.Frame(edit_note_window)
    edit_button_frame.pack(pady=5)

    edit_accept = tk.Button(edit_button_frame, text="Save", command=save_edit)
    edit_accept.pack(side=tk.LEFT)

    edit_cancel = tk.Button(edit_button_frame, text="Cancel", command=edit_note_window.destroy)
    edit_cancel.pack(side=tk.LEFT)

def add_note():
    def save_note():
        note_text = note_var.get()
        add_note_to_db(note_text)
        add_note_window.destroy()
        display_notes(notes_container)  # Update the displayed notes after adding

    add_note_window = tk.Toplevel(root)
    add_note_window.title("addnote")
    add_note_window.geometry('250x100')
    note_var = tk.StringVar()

    note_label = tk.Label(add_note_window, text="Enter your note:")
    note_label.pack()
    note_entry = tk.Entry(add_note_window, textvariable=note_var, width=30)
    note_entry.pack(pady=5)

    note_button_frame = tk.Frame(add_note_window)
    note_button_frame.pack(pady=5)

    note_accept = tk.Button(note_button_frame, text="Save", command=save_note)
    note_accept.pack(side=tk.LEFT)

    note_cancel = tk.Button(note_button_frame, text="Cancel", command=add_note_window.destroy)
    note_cancel.pack(side=tk.LEFT)

create_database()

root = Window(themename="superhero")
root.title("PyJottings")
root.geometry('360x660+40+40')

style = Style('superhero')
settings_frame = LabelFrame(root, text="Settings", width=80, height=640)
settings_frame.pack(pady=10, padx=10)
settings_frame.place(x=5, y=10)

add_button = Button(settings_frame, text="+", command=add_note)
add_button.pack(pady=10, padx=10)

delete_button = Button(settings_frame, text="󰗨", command=clear_notes)
delete_button.pack(pady=10, padx=10)


exit_button = Button(settings_frame, text="󰍃", command=root.destroy)
exit_button.pack(pady=10, padx=10)

# Create a container frame for notes
notes_container = tk.Frame(root)
notes_container.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

display_notes(notes_container)

root.mainloop()
