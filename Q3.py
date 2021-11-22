from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

Fs, sig = wavfile.read('guitartune.wav')
d = 15  # in seconds
N = Fs * d
t = np.linspace(0, d, num=N, endpoint=False)

fig, ax = plt.subplots()
fft = np.fft.fftshift(np.fft.fft(sig))
power_spectrum = np.square(np.abs(fft))/N
amp_spectrum = (2/N)*np.abs(power_spectrum)
phase_spec = np.arctan(np.imag(fft),np.real(fft))
ax.stem(np.arange(-N/2,N/2), power_spectrum)

ax.legend()
ax.set_title("Power spectrum")
ax.set_xlabel('$f$ [Hz]')
ax.set_ylabel('Amplitude')
plt.show()