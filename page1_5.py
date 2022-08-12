from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def next_page():
    root.destroy()
    import page2_9

# Create a window
root =Tk()
root.title("CO2 Tracker")
root.geometry("500x500")
root['bg'] = '#42f584'


# Create the middle frame
top_frame = ttk.LabelFrame(root, text="<Welcome> ")
top_frame.grid(row=0, column=0, padx=70, pady=50, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root, text="Enter your name: ")
bottom_frame.grid(row=1, column=0, padx=70, pady=0, sticky="NSEW")

# Create and set the message text variable
description_text = StringVar()
description_text.set(""" 
This is CO2 tracker app.
You can acknowledge how you affect on the environment through.
It will show the effects to glaciers, climate and ozone layer.""")

# create and pack the description label
description_label = ttk.Label(top_frame, textvariable=description_text)
description_label.grid(row=1, column=0)

# Open Image
logo_image = Image.open("logo.png")

# resize the logo image
resized = logo_image.resize((300, 200), Image.Resampling.LANCZOS)
new_logo_image = ImageTk.PhotoImage(resized)
myimage = Label(top_frame, image=new_logo_image)
myimage.grid(row=0, column=0)

# create a function to restore the users' input and display with description in GUI
def printValue():
    pname = player_name.get()
    Label(bottom_frame, text=f'{pname}, Registered!').grid(row=1, column=1)

player_name = Entry(bottom_frame)
player_name.grid(row=0, column=0)

Button(bottom_frame, text="Submit", padx=10, pady=5,command=printValue).grid(row=2, column=1)

# Set another button to move on
Button(bottom_frame, text="Next", padx=10, pady=5, command=next_page).grid(row=2, column=5)

# Run the main window loop
root.mainloop()
