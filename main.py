import librosa
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def audio_fn(t): 
    indices = (t * sr).astype(int)
    return np.where(
            (indices >= 0) & (indices < len(y)),  # Condition: Is index valid? (Using & operator since numpy elements only accept bitwise operator as valid AND operator)
            y[np.clip(indices, 0, len(y) - 1)],   # True: Safe lookup (clipped to avoid crash)
            0                                     # False: Return 0
        )
    
# Audio Reading

file_path = "./audios/cat_audio.wav"
y, sr = librosa.load(file_path, sr = None, mono = True)
t = np.linspace(0, len(y) / sr , len(y))

def changeAudioFileGUI(gui_path):
    global file_path, y, sr, t
    file_path = gui_path
    y, sr = librosa.load(file_path, sr = None, mono = True)
    t = np.linspace(0, len(y) / sr , len(y))


def correlateUserInput(user_shift):
    if isinstance(user_shift, (int, float)):
        customShift = audio_fn(t - user_shift)
        correlation = signal.correlate(audio_fn(t), customShift , mode="same", method="fft")
        return correlation
    else:
        print("Error: invalid input, could not correlate")

def getFixedDelays():
    two_second_delay = signal.correlate(audio_fn(t) ,audio_fn(t - 2), mode="same", method="fft")
    thirty_second_delay = signal.correlate(audio_fn(t) ,audio_fn(t - 30), mode="same", method="fft")

    return two_second_delay, thirty_second_delay

two_sec_correlation , thirty_sec_correlation = getFixedDelays()


if __name__ == "__main__":
    # Original Audio Time Signal Representation 

    plt.figure(1, figsize=(12, 8))
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Time representation of cat audio .wav file")
    plt.plot(t, y)
    plt.show()

    # Time Shifting

    # Subplot of 3 horiztonal plots shows a comparision between the orignal representation of the audio file
    # As well as 2 other deplayed reprsentations, i.e, 2 sec. delay and 30 sec. delay, respectively.

    plt.figure(2, figsize=(12, 8))

    originalAudio = audio_fn(t - 0)

    plt.subplot(1,3,1)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Original Audio File (t + 0)")
    plt.plot(t, originalAudio)

    twoSecDelay = audio_fn(t - 2)

    plt.subplot(1,3,2)
    plt.xlabel("Time (s)")
    plt.xlim(0, len(y) / sr)
    plt.ylabel("Amplitude")
    plt.title("Audio File Delayed by 2 sec. (t - 2)")
    plt.plot(t, twoSecDelay)

    thirtySecondDelay = audio_fn(t - 30)

    plt.subplot(1,3,3)
    plt.xlabel("Time (s)")
    plt.xlim(0, len(y) / sr)
    plt.ylabel("Amplitude")
    plt.title("Audio File Delayed by 30 sec. (t - 30)")
    plt.plot(t, thirtySecondDelay)
    plt.show()


    # Correlation 

    # Important ! : I use the library 'scipy' as an alternative for numpy .
    # Reason :      numpy preforms correlation in the time domain which takes a long time & my computer doesn't produce a result.
    # Solution :    I imported a similar library to 'numpy', i.e, 'scipy' because scipy uses fourier transform before preforming correlation, hence a faster result.  


    # Correlation between the Orignal Signal and the Delayed Signal by 2 sec.

    plt.figure(3, figsize=(16, 10))

    plt.subplot(1,2,1)
    plt.xlim(0, len(y) / sr)
    plt.ylabel("Correlation")
    plt.xlabel("Time (s)")
    plt.title("Correlation between the Original Audio Signal and the 2 sec. Delay")
    plt.plot(t, two_sec_correlation)

    # Correlation between the Orignal Signal and the Delayed Signal by 30 sec.

    plt.subplot(1,2,2)
    plt.xlim(0, len(y) / sr)
    plt.ylabel("Correlation")
    plt.xlabel("Time (s)")
    plt.title("Correlation between the Original Audio Signal and the 30 sec. Delay")
    plt.plot(t, thirty_sec_correlation)

    plt.show()