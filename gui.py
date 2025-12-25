from tkinter import * 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
import main as m

class SignalCorrelationApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Correlation Visualization"
        self.root.geometry = "1000x800"
        self.fig = Figure(figsize=(5,5))


        self.first_plot = self.fig.add_subplot(131)
        self.second_plot = self.fig.add_subplot(132)
        self.custom_plot = self.fig.add_subplot(133)

        self.first_plot.plot(m.t, m.two_sec_correlation)
        self.second_plot.plot(m.t, m.thirty_sec_correlation)


        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(expand=True ,anchor=CENTER)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.label = Label(text="Enter shift value to be correlated with the original audio file.", width=100, fg="black", bg="white").pack(expand=True, anchor=CENTER)
        self.input = Entry(fg="black", bg="white", width=100)
        self.btn = Button(text="Correlate",
                    fg="white",
                    bg="grey",
                    command=self.correlateShift)

        self.input.pack()
        self.btn.pack()

    def correlateShift(self):
        self.custom_plot.clear()
        shift_val = int(self.input.get())
        print(f"Shift value: {shift_val}")
        correlated_data = m.correlateUserInput(shift_val)
        print("correlation retrived")
        self.custom_plot.plot(m.t, correlated_data)
        self.canvas.draw()
        self.toolbar.update()

if __name__ == "__main__":
    root = Tk()
    SignalCorrelationApp(root)
    root.mainloop()
