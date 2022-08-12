from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

my_list1 = [line.split(',') for line in open("data1.txt")]
a= my_list1

my_list2 = [line.split(',') for line in open("data2.txt")]
b=my_list2

my_list3 = [line.split(',') for line in open("data.txt")]
name=my_list3

def exit():
    root.destroy()

# Create a window
root = Tk()
root.title("CO2 Tracker")
root.geometry("600x500")
root['bg'] = '#42f584'

# Create the middle frame
top_frame = ttk.LabelFrame(root, text="<The results> ")
top_frame.grid(row=0, column=0, padx=50, pady=50, sticky="NSEW")

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=50, pady=0, sticky="NSEW")


# Set Labels to display the questions which are text
description1=Label(top_frame, text="These was {} activities for a day:".format(name))
description2=Label(top_frame, text="1) your drive makes {}kg of CO2".format(a))
description3=Label(top_frame, text="2) The disposable cups you used makes {}kg of CO2".format(b))
description4=Label(top_frame, text="The carbon emission you've made lets glacier molten, destroy ozone layer and pollute the air.")

# Place the labels in specific regions
description1.grid(row=1,column=1)
description2.grid(row=2,column=1)
description3.grid(row=3,column=1)
description4.grid(row=4,column=1)


# Open Image
image1 = Image.open("glacier.jpg")

# resize the logo image
resized = image1.resize((165, 100), Image.Resampling.LANCZOS)
new_image1 = ImageTk.PhotoImage(resized)
myimage1 = Label(bottom_frame, image=new_image1)
myimage1.grid(row=1, column=0)


# Open Image
image1 = Image.open("air pollution.jpg")

# resize the logo image
resized = image1.resize((165, 100), Image.Resampling.LANCZOS)
new_image2 = ImageTk.PhotoImage(resized)
myimage2 = Label(bottom_frame, image=new_image2)
myimage2.grid(row=1, column=1)

# Open Image
image1 = Image.open("ozone layer.jfif")

# resize the logo image
resized = image1.resize((165, 100), Image.Resampling.LANCZOS)
new_image3 = ImageTk.PhotoImage(resized)
myimage3 = Label(bottom_frame, image=new_image3)
myimage3.grid(row=1, column=2)


# Create submit button to create & save a file and quit the program
submit_button = ttk.Button(bottom_frame, text="Exit", command=exit)
submit_button.grid(row=3, column=1)

# Run the main window loop
root.mainloop()
