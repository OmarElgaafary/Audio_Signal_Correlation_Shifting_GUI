## Audio Signal Shift Correlation Visualization Tool   
A Python powered GUI application for visualizing audio signal cross correlation with user defined time shifts. 

# GUI
* The GUI is mainly powered by **Tkinter**, which is part of Python's built-in library for creating graphical user interfaces. All the buttons including the "Compute Correlation" & "Import" buttons are all relient on Tkinter for interactivity. 

* Another library that enables the GUI is **matplotlib**'s backend libraries used for displaying the plots on the GUI, responsible for the visualization of the graphs and navigation tools.

# Correlation Logic 

* All the correlation logic used in the **main.py** is relient on the **scipy** library and mainly the **signal** module used cross-correlation for signals. The scipy library is preferred over the numpy library due to it's efficiency and speed in calculating cross-correlation between two numpy arrays using **Fast Fourier Transform** mode, which is far superior to numpy's correlating methods, due to the fact that scipy's correlating method preforms correlation in the frequecny domain first before converting the signal back to time domain which profoundly decrease time to compute correalation.

## Preview (user-defined delay = 20s):

<img width="1196" height="821" alt="Correlation Visualization" src="https://github.com/user-attachments/assets/874654b6-fcbe-4a00-8770-6eca63a4ef21" />

# Audio Credit:

Guitar Melody : https://www.youtube.com/watch?v=63hdfvqiIV8&list=RD63hdfvqiIV8&start_radio=1

Cat Audio : https://www.youtube.com/watch?v=-dTa8gchZfc
