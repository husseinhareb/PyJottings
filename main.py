import tkinter as tk
import ttkbootstrap as tb
from PIL import Image
from ttkbootstrap.constants import *
Image.CUBIC = Image.BICUBIC

root = tb.Window(themename="superhero")
root.title("PyJottings")
root.configure()
root.geometry('300x660')

settings_frame = tb.LabelFrame(root,
                     text="Settings",
                     width=80,
                     height=640,
                     )
settings_frame.pack(pady=10,padx=10)
settings_frame.place(x=10,y=10)


root.mainloop()