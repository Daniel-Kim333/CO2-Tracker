from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def next_page():
    root.destroy()
    import page3

# Create a window
root = Tk()
root.title("CO2 Tracker")
root.geometry("600x500+500+0")

# Create the left frame
left_frame = ttk.LabelFrame(root, text="CO2 Tracker")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the text variable
description_text = StringVar()
description_text.set("Track your life! ")

# create and pack the description label
description_label = ttk.Label(left_frame, textvariable=description_text)
description_label.grid(row=2, column=1)

# Open Image
logo_image = Image.open("logo.png")

# resize the logo image
resized = logo_image.resize((150, 100), Image.Resampling.LANCZOS)
new_logo_image = ImageTk.PhotoImage(resized)
myimage = Label(left_frame, image=new_logo_image)
myimage.grid(row=1, column=0)

# Create the right frame
right_frame = ttk.LabelFrame(root, text="Actions")
right_frame.grid(row=0, column=1, padx=50, pady=30, sticky=NSEW)

# Create a label to set "type"
type_text = StringVar()
type_text.set("Type :")

# place the label and scale it
type_text_label = ttk.Label(right_frame, textvariable=type_text)
type_text_label.grid(row=1, column=1)

# Set up a variable and option list for the action Combobox
gas_type = ['Diesel', 'Petrol']
chosen_gas = StringVar()
chosen_gas.set(gas_type[0])

# Create the Combobox to select the gas type
gas_box = ttk.Combobox(right_frame, textvariable=chosen_gas, state="readonly")
gas_box['values'] = gas_type
gas_box.grid(row=2, column=1, padx=10, pady=3)

# Create and set the text variable for Qs
how_long = StringVar()
how_long.set("How long do you drive average?")

# Create and place the label for the answer
how_long_label = ttk.Label(right_frame, textvariable=how_long)
how_long_label.grid(row=4, column=1)

# Create int var to get integer info
int_how_long = IntVar()

# Create an entry and place on th screen
int_how_long_entry = ttk.Entry(right_frame, textvariable=int_how_long)
int_how_long_entry.grid(row=5, column=1)

# Create and set the text variable
disposable = StringVar()
disposable.set("How many do you use disposable cups in a day?")

disposable_label = ttk.Label(right_frame, textvariable=disposable)
disposable_label.grid(row=6, column=1)

# Create int var which receive only integer numbers as a code
int_how_much = IntVar()

how_much_entry = ttk.Entry(right_frame, textvariable=int_how_much)
how_much_entry.grid(row=7, column=1)

# Create a submit_button to store and move next page
submit_button = ttk.Button(root, text="Submit", command=next_page)
submit_button.grid(row=1, column=1)

# Run the main window loop
root.mainloop()
