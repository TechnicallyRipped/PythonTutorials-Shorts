

import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read("x.wav")
print(f'{rate=}')
print(f'{data=}')

plt.specgram(data, Fs=rate)
plt.show()
