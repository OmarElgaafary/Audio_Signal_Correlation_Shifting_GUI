from tkinter import *
import main

# The main tkinter window
window = Tk()

# setting the title and 
window.title('Plotting in Tkinter')

def init():
    main.allPlots()

# setting the dimensions of 
# the main window
window.geometry("500x500")

# button that would displays the plot
plot_button = Button(master = window,
                     height = 2,
                     width = 10,
                    text = "Plot",
                    command=init)
# place the button
# into the window
plot_button.pack()

# run the gui
window.mainloop()