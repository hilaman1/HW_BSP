import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
Fs = 100
d = 5  # in seconds
N = Fs * d
t = np.linspace(0, d, num=N, endpoint=False)


f1 = 2
amp1 = 2
sig1 = amp1*np.sin(2 * np.pi * f1 * t)

f2 = 10
amp2 = 4
sig2 = amp2*np.sin(2 * np.pi * f2 * t)
ax.plot(t, sig1)
ax.plot(t, sig2)

ax.legend()
plt.xlabel('$t$ [s]')
plt.ylabel('$\sin (t)$')
ax.set_title("Time domain")
plt.show()

fig2, ax2 = plt.subplots()
fft1 = np.fft.fftshift(np.fft.fft(sig1))
fft2 = np.fft.fftshift(np.fft.fft(sig2))

power1 = np.square(np.abs(fft1)) / N
power2 = np.square(np.abs(fft2)) / N

amp_spec1 = (2 / N) * np.abs(power1)
amp_spec2 = (2 / N) * np.abs(power2)

ax2.stem(np.arange(-N/2, N/2), amp_spec1, use_line_collection=True)
ax2.stem(np.arange(-N/2, N/2),amp_spec2, use_line_collection=True)



ax2.legend()
ax2.set_title("Amplitude spectrum")
ax2.set_xlabel('$f$ [Hz]')
ax2.set_ylabel('Amplitude')
plt.show()
