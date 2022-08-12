from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Create a window
root =Tk()
root.title("CO2 Tracker")
root.geometry("600x500")

Label(root, text="WELCOMEMMEMEMEM", pady=10, padx= 100).grid(row=0, column=3)

Frame1 = Frame(root, bg='grey', borderwidth=4, relief = SUNKEN)
Frame2 = Frame(root, bg='grey', borderwidth=4, relief = SUNKEN)
Frame3 = Frame(root, bg='grey', borderwidth=4, relief = SUNKEN)

head = Label(Frame1, text="title")
footer = Label(Frame3, text="footer")

head.grid(row=1, column=2)
footer.grid(row=10, column=2)

root.mainloop()
