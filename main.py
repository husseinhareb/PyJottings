import tkinter as tk
import ttkbootstrap as tb
from PIL import Image
from ttkbootstrap.constants import *
Image.CUBIC = Image.BICUBIC

root = tk.Tk(className="monitoring_widget")
theme = tb.Style("darkly")
root.configure(bg="#3b3b3b")
root.geometry('300x660')

settings_frame = tb.Frame(root,
                     width=80,
                     height=60,
                     )
settings_frame.pack(pady=10,padx=10)
settings_frame.place(x=10,y=10)
root.mainloop()