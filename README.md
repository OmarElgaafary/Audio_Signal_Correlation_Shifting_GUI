# Audio Signal Shift Correlation Visualization Tool

A high-performance Python GUI application designed to visualize audio signal cross-correlation. This tool allows users to import audio files, apply user-defined time shifts, and analyze the correlation between the original and shifted signals in real-time.

## 🚀 Features

* **Interactive GUI:** Built with **Tkinter** for a responsive user experience.
* **Custom Audio Support:** Import your own `.wav` files using **Librosa**.
* **High-Performance Logic:** Utilizes **Scipy's** FFT-based convolution for rapid correlation calculation, significantly outperforming standard NumPy methods.
* **Dynamic Visualization:** Real-time plotting of waveforms and correlation graphs using **Matplotlib**.
* **Flexible Controls:** * One-click presets for **2s** and **30s** delays.
    * Input field for custom user-defined time shifts.

## 🛠️ Tech Stack

* **GUI:** `tkinter` (Standard Python Interface)
* **Computation:** `scipy.signal` (FFT-based Cross-Correlation), `numpy` (Array manipulation)
* **Visualization:** `matplotlib.pyplot` (Graphing backend)
* **Audio Processing:** `librosa` (Audio file loading and sampling)

## 🧮 Correlation Logic

The application prioritizes speed and memory efficiency. Instead of standard spatial domain convolution, the **main.py** logic leverages `scipy.signal.correlate` using the **Fast Fourier Transform (FFT)** method. This converts the signal to the frequency domain to compute correlation, which is computationally superior for large audio arrays compared to standard time-domain iterative methods.

**Mathematical Definition:**
Scipy defines the discrete cross-correlation $z$ of two arrays $x$ and $y$ as:

$$z[k] = \sum_{l=0}^{N-1} x_l y^*_{l-k}$$

Where:
* $z[k]$ is the correlation result at lag $k$.
* $x_l$ is the input array.
* $y^*$ denotes the complex conjugate of the shifted array.

## 📸 Preview


![Correlation_Visualization_Preview-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/2cb3759e-994c-489b-b7f3-a9ec12530267)


## 📦 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install numpy scipy matplotlib librosa
    ```

3.  **Run the application:**
    ```bash
    python gui.py
    ```
