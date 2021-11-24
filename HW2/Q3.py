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
ax.stem(np.arange(-N/2,N/2), power_spectrum, use_line_collection=True)

ax.legend()
ax.set_title("Power spectrum")
ax.set_xlabel('$f$ [Hz]')
ax.set_ylabel('Power')
# plt.show()

fig2, ax2 = plt.subplots()
fft2 = fft.copy()
ten_present = int(np.shape(fft2)[0]*0.1)
fft2[(-1)*ten_present:] = 0
fft2[:ten_present] = 0
power_spectrum2 = np.square(np.abs(fft2))/N
ax2.stem(np.arange(-N/2,N/2), power_spectrum2, use_line_collection=True)

ax2.legend()
ax2.set_title("Power spectrum after filtering")
ax2.set_xlabel('$f$ [Hz]')
ax2.set_ylabel('Power')
plt.show()

# we can see that the Power spectrum hasn't change. thus, we didn't need to erase these frequencies.

ifft2 = np.fft.ifft(np.fft.ifft(sig))

wavfile.write('ifft guitar.wav', Fs, (ifft2*2**16).astype(np.int16))

