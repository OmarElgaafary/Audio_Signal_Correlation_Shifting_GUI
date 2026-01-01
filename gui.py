import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import main as m  

class SignalCorrelationApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Correlation Visualization")
        self.root.geometry("1200x800") 
        

        self.plot_frame = tk.Frame(root)
        self.plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.control_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)


        self.fig = Figure(figsize=(15, 5), dpi=100, constrained_layout=True)
        
        self.first_plot = self.fig.add_subplot(131)
        self.second_plot = self.fig.add_subplot(132)
        self.custom_plot = self.fig.add_subplot(133)

        self.first_plot.plot(m.t, m.two_sec_correlation, color='#1f77b4') 
        self.second_plot.plot(m.t, m.thirty_sec_correlation, color='#ff7f0e') 

        self.setup_plot_style(self.first_plot, "Delay: 2 seconds")
        self.setup_plot_style(self.second_plot, "Delay: 30 seconds")
        self.setup_plot_style(self.custom_plot, "User Defined Delay")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        self.toolbar.update()

        self.import_btn = tk.Button(
            self.control_frame, 
            text="Import WAV File",
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            width=20,
            command=self.importAudio
        )
        self.import_btn.pack(side=tk.TOP, pady=(10, 5))
        

        self.label = tk.Label(
            self.control_frame, 
            text="Enter shift value (integer) to correlate with original audio file:", 
            font=("Arial", 11),
            bg="#f0f0f0"
        )
        self.label.pack(side=tk.TOP, pady=(10, 5))

        self.input = tk.Entry(self.control_frame, font=("Arial", 12), width=15, justify='center')
        self.input.pack(side=tk.TOP, pady=5)
        self.input.bind('<Return>', lambda event: self.correlateShift()) # Allow pressing Enter key

        self.btn = tk.Button(
            self.control_frame, 
            text="Compute Correlation",
            font=("Arial", 10, "bold"),
            fg="white",
            bg="darkblue",
            activebackground="#003d99", 
            activeforeground="white",
            width=20,
            command=self.correlateShift
        )
        self.btn.pack(side=tk.TOP, pady=(5, 15))


    def importAudio(self):
        file_path = filedialog.askopenfilename(
            title="Select WAV file",
            filetypes=(("WAV files", "*.wav"), ("All files", "*.*"))
        )
        
        if file_path:
            m.changeAudioFileGUI(file_path) 
            
            # Refresh the plots with the new data from main.py
            self.update_all_plots()
            self.canvas.draw()
            print(f"Loaded new file: {file_path}")

    def update_all_plots(self):
        self.first_plot.clear()
        self.second_plot.clear()

        first_signal, second_signal = m.getFixedDelays()
        
        self.first_plot.plot(m.t, first_signal, color='#1f77b4')
        self.second_plot.plot(m.t, second_signal, color='#ff7f0e')
        
        self.setup_plot_style(self.first_plot, "Delay: 2 seconds")
        self.setup_plot_style(self.second_plot, "Delay: 30 seconds")
        self.setup_plot_style(self.custom_plot, "User Defined Delay")

    def setup_plot_style(self, ax, title):
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Correlation")
        ax.grid(True, linestyle='--', alpha=0.6)

    def correlateShift(self):
        try:
            val_str = self.input.get()
            if not val_str: return 
            shift_val = int(val_str)
        except ValueError:
            print("Please enter a valid integer")
            return

        print(f"Shift value: {shift_val}")
        
        correlated_data = m.correlateUserInput(shift_val)
        
        self.custom_plot.clear()
        self.custom_plot.plot(m.t, correlated_data, color='green')
        
        self.setup_plot_style(self.custom_plot, f"User Delay: {shift_val}s")
        
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignalCorrelationApp(root)
    root.mainloop()