from tkinter import *

# Create a window
root = Tk()
root.title("CO2 Tracker")
root.geometry("600x500")

# define a function to calculate values the users input and display the result
def calculate():
    q1=int(question1entry.get())
    q2=int(question2entry.get())
    q1amount=q1*2.49
    q2amount=q2*0.06
    Label(text=f"{q1amount}").grid(row=4, column=1)

# Set Labels to display the questions which are text
action=Label(root, text="Actions: ")
question1=Label(root, text="How long do you drive?")
question2=Label(root, text="How many paper cups do you use?")

# Place the labels in specific regions
action.grid(row=0, column=0)
question1.grid(row=1,column=1)
question2.grid(row=2,column=1)

# This is for the Entry to get the values
question1value=IntVar()
question2value=IntVar()

question1entry=Entry(root, textvariable=question1value)
question2entry=Entry(root, textvariable=question2value)

# Place the Entry in right position
question1entry.grid(row=1, column=2)
question2entry.grid(row=2, column=2)

# Make a Button to follow the function and place it
Button(text="Submit", command=calculate).grid(row=3, column=1)

# Run the main window loop
root.mainloop()
