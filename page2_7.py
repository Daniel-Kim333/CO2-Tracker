from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create a window
root = Tk()
root.title("CO2 Tracker")
root.geometry("500x500")

# Create the bottom frame to collaborate the Labels in one section("Actions: ")
bottom_frame = ttk.LabelFrame(root, text="Actions: ")
bottom_frame.grid(row=1, column=0, padx=70, pady=10, sticky="NSEW")

# Create the Top frame to display an image and to modify it easily
top_frame = ttk.LabelFrame(root, text="                            Let's check your footprint!                   ")
top_frame.grid(row=0, column=0, padx=70, pady=10, sticky="NSEW")

# Open Image
logo_image = Image.open("environment.png")

# resize the logo image
resized = logo_image.resize((300, 200), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized)
myimage = Label(top_frame, image=new_image)
myimage.grid(row=1, column=0)


# define a function to calculate values the users input and display the result
def calculate():
    q1=int(question1entry.get())
    q2=int(question2entry.get())
    q1amount=q1*2.49
    q2amount=q2*0.06
    total=q1amount+q2amount
    Label(bottom_frame, text=f"You've got {total}kg of CO2 emission today. ").grid(row=4, column=1)

# define next_page to move another window
def next_page():
    root.destroy()
    import page3_5

# Set Labels to display the questions which are text
question1=Label(bottom_frame, text="How long do you drive?")
question2=Label(bottom_frame, text="How many paper cups do you use?")

# Place the labels in specific regions
question1.grid(row=1,column=1)
question2.grid(row=2,column=1)

# This is for the Entry to get the values
question1value=IntVar()
question2value=IntVar()

question1entry=Entry(bottom_frame, textvariable=question1value)
question2entry=Entry(bottom_frame, textvariable=question2value)

# Place the Entry in right position
question1entry.grid(row=1, column=2)
question2entry.grid(row=2, column=2)

# Make a Button to follow the function and place it
Button(bottom_frame, text="Submit", command=calculate).grid(row=3, column=1)

# Create another Button to kill this window and move to next page by using defined function
Button(bottom_frame, text="Next", command=next_page).grid(row=4, column=2)

# Run the main window loop
root.mainloop()

