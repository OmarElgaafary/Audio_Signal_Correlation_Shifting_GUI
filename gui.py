from tkinter import * 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np


class SignalCorrelationApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Correlation Visualization"
        self.root.geometry = "1000x800"
        self.fig = Figure(figsize=(5,5))
        self.ploty = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)

        self.canvas.get_tk_widget().pack(expand=True ,anchor=CENTER)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.label = Label(text="Enter shift value to be correlated with the original audio file.", width=100, fg="black", bg="white").pack(expand=True, anchor=CENTER)
        self.input = Entry(fg="black", bg="white", width=100)
        self.btn = Button(text="Correlate",
                    fg="white",
                    bg="grey",
                    command=self.rectShift)

        self.input.pack()
        self.btn.pack()

    def rect(self, t):
       return abs(t) < 0.5

    def rectShift(self):
        rShift = self.input.get()
        self.ploty.clear()
        if isinstance(rShift, (int, float)):
            input.delete(0, END)
            print("Error: Input value must be a number.")
            return 

        t = np.arange(-5, 5, 0.1)
        y = self.rect(t + float(rShift))
        self.ploty.plot(t, y)
        self.canvas.draw()
        self.toolbar.update()

if __name__ == "__main__":
    root = Tk()
    SignalCorrelationApp(root)
    root.mainloop()
