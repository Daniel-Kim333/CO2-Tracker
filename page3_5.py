from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create a window
root = Tk()
root.title("CO2 Tracker")
root.geometry("500x500")
root['bg'] = '#42f584'

# Create the middle frame
top_frame = ttk.LabelFrame(root, text="<The results> ")
top_frame.grid(row=0, column=0, padx=70, pady=50, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=70, pady=0, sticky="NSEW")

# Create and set the message text variable
description_text = StringVar()
description_text.set("""These was your activities for a day:

    1) driving for _hrs = {}

    2) used _ disposable items = {}

Your activities affect the environment and indicates this =>
you might make amount of glacier melted and
""")

# create and pack the description label
description_label = ttk.Label(top_frame, textvariable=description_text)
description_label.grid(row=0, column=0, columnspan=3, sticky="NSEW")

# Open Image
image1 = Image.open("glacier.jpg")

# resize the logo image
resized = image1.resize((300, 200), Image.Resampling.LANCZOS)
new_image1 = ImageTk.PhotoImage(resized)
myimage1 = Label(top_frame, image=new_image1)
myimage1.grid(row=1, column=0)

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
"""

# Create submit button to create & save a file and quit the program
submit_button = ttk.Button(bottom_frame, text="Submit")
submit_button.grid(row=3, column=3)

# Run the main window loop
root.mainloop()
