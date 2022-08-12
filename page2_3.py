import tkinter as tk

class CalulateCO2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CO2 Tracker")
        self.geometry("400x600")

        # define IntVar() variables A and B
        self.A = tk.IntVar()
        self.B = tk.IntVar()

        # assign methods to notify on IntVar() variables
        self.A.trace_add("write", self.calculate_sum)
        self.B.trace_add("write", self.calculate_sum)

        self.create_widgets()

    def create_widgets(self):
        self.A_label = tk.Label(self, text="How long do you drive average? ")
        self.B_label = tk.Label(self, text="How many do you use disposable cups in a day? ")

        self.A_entry = tk.Entry(self, textvariable=self.A)
        self.B_entry = tk.Entry(self, textvariable=self.B)

        self.sum_label = tk.Label(self, text="Total: ")
        self.result_label = tk.Label(self, text=self.A.get() + self.B.get())

        self.A_label.grid(row=0, column=0, padx=5, pady=5)
        self.A_entry.grid(row=1, column=0, padx=5, pady=5)
        self.B_label.grid(row=2, column=0, padx=5, pady=5)
        self.B_entry.grid(row=3, column=0, padx=5, pady=5)
        self.sum_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_label.grid(row=4, column=1, padx=5, pady=5)

        #clickable button
        self.button= tk.Button(self, text="Submit")
        self.button.grid(row=5, column=1, columnspan=2)

    def calculate_sum(self, *args):
        try:
            num_a = self.A.get()
            num_aa = num_a * 2.68
        except:
            num_aa = 0

        try:
            num_b = self.B.get()
            num_bb = num_b * 0.06
        except:
            num_bb = 0

        self.result_label['text'] = num_aa + num_bb

if __name__ == "__main__":
    app = CalulateCO2()
    app.mainloop()