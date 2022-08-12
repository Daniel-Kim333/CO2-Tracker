from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from page2_1 import *



# Create a window
root =Tk()
root.title("CO2 Tracker")
root.geometry("600x500+500+0")

root['background']='#79F777'

f1 = Frame(root, bg="grey", relief = SUNKEN)
f1.pack(side=CENTER)

# Create and set the message text variable
description_text = StringVar()
description_text.set("""These were your activites for a day:
    driving for _hrs = 
    used _ disposable items = 

Your activies affect the environment and indicates this =>
you might make amount of glacier melted and""")

# create and pack the description label
description_label = ttk.Label(f1, textvariable=description_text).place(relx=.5, rely=.5,anchor= CENTER)
description_label.pack()
# description_label.grid(row=0, column=1, sticky="NSEW")

"""
# Open Image
image1 = Image.open("glacier.jpg")

# resize the logo image
resized = image1.resize((300, 200), Image.Resampling.LANCZOS)
new_image1 = ImageTk.PhotoImage(resized)
myimage1 = Label(f1, image=new_image1)
myimage1.pack()
#myimage1.grid(row=1, column=0)

# Run the main window loop
root.mainloop()

"""

"""
# Open Image
image1 = Image.open("air pollution.jpg")

# resize the logo image
resized = image1.resize((300, 200), Image.Resampling.LANCZOS)
new_image2 = ImageTk.PhotoImage(resized)
myimage2 = Label(image=new_image2)
myimage2.grid(row=1, column=1)

# Open Image
image1 = Image.open("ozone layer.jfif")

# resize the logo image
resized = image1.resize((300, 200), Image.Resampling.LANCZOS)
new_image3 = ImageTk.PhotoImage(resized)
myimage3 = Label(image=new_image3)
myimage3.grid(row=1, column=2)

# Run the main window loop
root.mainloop()

"""
