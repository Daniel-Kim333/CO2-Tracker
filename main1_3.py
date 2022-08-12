from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def next_page():
    root.destroy()
    import page2_8

# Create a window
root =Tk()
root.title("CO2 Tracker")
root.geometry("500x500")

# Create the Top frame for logo
top_frame = ttk.LabelFrame(root)
top_frame.grid(row=0, column=0, padx=70, pady=10, sticky="NSEW")

# Create the middle frame
mid_frame = ttk.LabelFrame(root, text="<Welcome> ")
mid_frame.grid(row=1, column=0, padx=70, pady=10, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root, text="Enter your name: ")
bottom_frame.grid(row=2, column=0, padx=70, pady=10, sticky="NSEW")

# Create and set the message text variable
description_text = StringVar()
description_text.set(""" 
This is CO2 tracker app.
You can acknowledge how you affect on the environment through.
It will show the effects to glaciers, climate and ozone layer.""")

# create and pack the description label
description_label = ttk.Label(mid_frame, textvariable=description_text)
description_label.grid(row=1, column=0)

# Open Image
logo_image = Image.open("logo.png")

# resize the logo image
resized = logo_image.resize((300, 200), Image.Resampling.LANCZOS)
new_logo_image = ImageTk.PhotoImage(resized)
myimage = Label(mid_frame, image=new_logo_image)
myimage.grid(row=0, column=0)

# Create and set the 'Name' for users to write
name_text = StringVar()
name_text.set("Name: ")

# place the name_text label
name_text_label = ttk.Label(bottom_frame, textvariable=name_text)
name_text_label.grid(row=0, column=1)

# Create a StringVar to store user's name
name = StringVar()

# Create a text entry field
name_entry = ttk.Entry(bottom_frame, textvariable=name)
name_entry.grid(row=0, column=2)

# Create a submit_button to store and move next page
submit_button = ttk.Button(bottom_frame, text="Submit", command=next_page)
submit_button.grid(row=3, column=1)

# Run the main window loop
root.mainloop()
