import tkinter as tk
import sqlite3
from ttkbootstrap import *

#Database Creation
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
#Function for adding notes trigger
def add_note_to_db(note):
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', ('Untitled', note))

    db.commit()
    db.close()

#Function for displaying notes from the database
def display_notes(note_container):
    for widget in note_container.winfo_children():
        widget.destroy()

    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()

    # Create a vertical scrollbar
    scrollbar = Scrollbar(note_container)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a canvas to contain the notes and associate it with the scrollbar
    canvas = tk.Canvas(note_container, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    # Create a frame to hold the notes inside the canvas
    notes_frame = tk.Frame(canvas)
    notes_frame.pack(fill=tk.BOTH, expand=True)

    for index, note in enumerate(notes, start=1):
        note_frame = tk.Frame(notes_frame, relief=tk.RIDGE, borderwidth=2)
        note_frame.pack(pady=10, padx=10)
        note_text = tk.Text(note_frame, wrap=tk.WORD, height=4, width=30)
        note_text.insert(tk.END, f"{index}. {note[2]}")
        note_text.config(state=tk.DISABLED)
        note_text.pack(pady=5, padx=10)

        button_frame = tk.Frame(note_frame)
        button_frame.pack(pady=5)

        delete_button = tk.Button(button_frame, text="󰆴", command=lambda i=note[0]: delete_note(i),font=("Jetbrains Nerd Font",8))
        delete_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(button_frame, text="󰘙", command=lambda i=note[0], c=note[2]: edit_note(i, c),font=("Jetbrains Nerd Font",8))
        edit_button.pack(side=tk.RIGHT, padx=5)

    # Update the window of the canvas after adding all note frames
    notes_frame.update_idletasks()

    # Configure the canvas to scroll
    canvas.config(scrollregion=canvas.bbox("all"))

    # Set the canvas window to the frame height to enable scrolling
    canvas.create_window((0, 0), window=notes_frame, anchor=tk.NW)

    db.close()

#Function to delete all notes(Deletes everything in the database)
def clear_notes():
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes')

    db.commit()
    db.close()
    display_notes(notes_container)  

def delete_note(note_id):
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))

    db.commit()
    db.close()
    display_notes(notes_container)  
#Function for editing previous notes
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

    edit_accept = tk.Button(edit_button_frame, text="", command=save_edit,font=("Jetbrains Nerd Font",8))
    edit_accept.pack(side=tk.LEFT,padx=2)

    edit_cancel = tk.Button(edit_button_frame, text="󰜺", command=edit_note_window.destroy,font=("Jetbrains Nerd Font",8))
    edit_cancel.pack(side=tk.LEFT,padx=2)

#Function for adding notes
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

    note_accept = tk.Button(note_button_frame, text="", command=save_note,font=("Jetbrains Nerd Font",8))
    note_accept.pack(side=tk.LEFT,padx=2)

    note_cancel = tk.Button(note_button_frame, text="󰜺", command=add_note_window.destroy,font=("Jetbrains Nerd Font",8))
    note_cancel.pack(side=tk.LEFT,padx=2)


create_database()



root = Window(themename="superhero")
root.title("PyJottings")
root.geometry('360x660+40+40')

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
