import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

root = tk.Tk()
root.title("Simple Tkinter App")

style = Style("lumen")

mainframe = ttk.LabelFrame(root, text="Settings")
mainframe.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # Adjust padx and pady as needed


# Run the Tkinter event loop
root.mainloop()
