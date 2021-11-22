import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


fig, ax = plt.subplots()
Fs = 100
d = 5  # in seconds
N = Fs * d
t = np.linspace(0, d, num=N, endpoint=False)


f1 = 2
sig1 = np.sin(2 * np.pi * f1 * t)
ax.plot(t, sig1)

f2 = 10
sig2 = np.sin(2 * np.pi * f2 * t)
ax.plot(t, sig2)

ax.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
ax.set_title("signals & fft")
#plt.show()

fig2, ax2 = plt.subplots()
fft1 = np.fft.fftshift(np.fft.fft(sig1))
fft2 = np.fft.fftshift(np.fft.fft(sig2))
# ax2.plot(t, fft1)
# ax2.plot(t, fft2)

power_spectrum1 = np.square(np.abs(fft1))/N
power_spectrum2 = np.square(np.abs(fft2))/N

amp_spectrum1 = (2/N)*np.abs(power_spectrum1)
amp_spectrum2 = (2/N)*np.abs(power_spectrum2)

phase_spec1 = np.arctan(np.imag(fft1),np.real(fft1))
phase_spec2 = np.arctan(np.imag(fft2),np.real(fft2))

ax2.stem(np.arange(-N/2,N/2), power_spectrum1)
ax2.stem(np.arange(-N/2,N/2), power_spectrum2)

ax2.legend()
ax2.set_title("fft of signals")
ax2.set_xlabel('$f$ [Hz]')
ax2.set_ylabel('Amplitude')
plt.show()
