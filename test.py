import librosa
import numpy as np
import matplotlib.pyplot as plt

def audio_fn(t): 
    indices = (t * sr).astype(int)
    return np.where(
            (indices >= 0) & (indices < len(y)),  # Condition: Is index valid? (Using & operator since numpy elements only accept bitwise operator as valid AND operator)
            y[np.clip(indices, 0, len(y) - 1)],   # True: Safe lookup (clipped to avoid crash)
            0                                     # False: Return 0
        )


y, sr = librosa.load("./audios/guitar_,melody.wav", sr=None, mono=True)
t = np.linspace(0, len(y) / sr, len(y))

plt.plot(t, y)
plt.show()


