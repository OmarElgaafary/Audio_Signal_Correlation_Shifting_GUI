import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

class SignalCorrelationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Correlation Analyzer")
        self.root.geometry("900x700")

        # --- Signal Parameters ---
        self.fs = 100  # Sampling frequency (Hz)
        self.duration = 60  # Duration in seconds (long enough to show 30s delay)
        self.t = np.linspace(0, self.duration, int(self.fs * self.duration))

        # --- GUI Layout ---
        # 1. Control Panel
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Label(control_frame, text="Enter Delay (seconds):", font=("Arial", 12)).pack(side=tk.LEFT)
        
        self.delay_entry = tk.Entry(control_frame, font=("Arial", 12), width=10)
        self.delay_entry.pack(side=tk.LEFT, padx=5)
        self.delay_entry.insert(0, "5") # Default value

        # Compute Button
        btn_compute = tk.Button(control_frame, text="Compute & Plot", command=self.plot_user_delay, 
                                bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        btn_compute.pack(side=tk.LEFT, padx=10)

        # Preset Buttons (Req: Delay=2s, Delay=30s)
        tk.Label(control_frame, text="|  Presets:", font=("Arial", 11)).pack(side=tk.LEFT, padx=10)
        
        btn_2s = tk.Button(control_frame, text="2 Seconds", command=lambda: self.set_delay_and_plot(2))
        btn_2s.pack(side=tk.LEFT, padx=2)
        
        btn_30s = tk.Button(control_frame, text="30 Seconds", command=lambda: self.set_delay_and_plot(30))
        btn_30s.pack(side=tk.LEFT, padx=2)

        # 2. Matplotlib Figure
        self.fig = plt.Figure(figsize=(8, 6), dpi=100)
        self.ax1 = self.fig.add_subplot(211) # Top: Signals
        self.ax2 = self.fig.add_subplot(212) # Bottom: Correlation
        self.fig.tight_layout(pad=4.0)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Toolbar
        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Initial Plot
        self.plot_user_delay()

    def generate_signal(self, delay_sec):
        """
        Generates a Gaussian pulse signal and its shifted version.
        Original signal is centered at t=5s to ensure it's visible.
        """
        # Original Signal (Gaussian Pulse centered at 5s)
        center_time = 5.0
        sig_orig = np.exp(-0.5 * ((self.t - center_time) ** 2) / (1.0 ** 2))

        # Shifted Signal (Original shifted by delay)
        # We calculate the new center
        shifted_center = center_time + delay_sec
        
        # Create shifted signal using the same time vector
        sig_shifted = np.exp(-0.5 * ((self.t - shifted_center) ** 2) / (1.0 ** 2))

        return sig_orig, sig_shifted

    def set_delay_and_plot(self, delay):
        """Helper to set entry text and plot immediately."""
        self.delay_entry.delete(0, tk.END)
        self.delay_entry.insert(0, str(delay))
        self.plot_user_delay()

    def plot_user_delay(self):
        """Main logic to compute correlation and update plots."""
        try:
            delay = float(self.delay_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric number for delay.")
            return

        # 1. Generate Signals
        sig1, sig2 = self.generate_signal(delay)

        # 2. Compute Correlation
        # 'mode=full' gives the standard cross-correlation
        correlation = np.correlate(sig1, sig2, mode='full')
        
        # 3. Create Lag/Time Axis for Correlation
        # The correlation result length is N + M - 1. We need to map indices to time lags.
        lags = np.arange(-(len(sig1) - 1), len(sig1)) / self.fs

        # --- Visualization ---
        
        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()

        # Plot 1: Time Domain Signals
        self.ax1.plot(self.t, sig1, label='Original Signal', color='blue', linewidth=1.5)
        self.ax1.plot(self.t, sig2, label=f'Shifted Signal (Delay={delay}s)', color='red', linestyle='--')
        self.ax1.set_title("Time Domain: Original vs. Shifted Signal")
        self.ax1.set_xlabel("Time (s)")
        self.ax1.set_ylabel("Amplitude")
        self.ax1.legend(loc="upper right")
        self.ax1.grid(True, alpha=0.3)
        self.ax1.set_xlim(0, self.duration)

        # Plot 2: Cross-Correlation
        # We normalize correlation for better visualization
        self.ax2.plot(lags, correlation, color='purple', linewidth=1.5)
        self.ax2.set_title("Cross-Correlation Function")
        self.ax2.set_xlabel("Lag (Time Delay in s)")
        self.ax2.set_ylabel("Correlation Magnitude")
        self.ax2.grid(True, alpha=0.3)
        
        # Add a marker at the peak
        peak_idx = np.argmax(correlation)
        peak_lag = lags[peak_idx]
        self.ax2.plot(peak_lag, correlation[peak_idx], 'ko') 
        self.ax2.annotate(f'Peak at {peak_lag:.2f}s', 
                          xy=(peak_lag, correlation[peak_idx]), 
                          xytext=(peak_lag, correlation[peak_idx]*1.1),
                          arrowprops=dict(facecolor='black', shrink=0.05))

        # Focus the plot around the relevant lag area (optional, for better view)
        # We ensure 0 and the delay are visible
        view_min = min(0, -delay) - 5
        view_max = max(0, -delay) + 5
        # Note: Cross-correlation of (x, x-delay) peaks at NEGATIVE delay lag if we do corr(x, y)
        # To make it intuitive (peak at +delay), we interpret the lag axis carefully or just look at magnitude.
        # Here, numpy.correlate(a, v) basically slides v over a.
        
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignalCorrelationApp(root)
    root.mainloop()