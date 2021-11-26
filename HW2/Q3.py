from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal



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

# applying some filters

# Butterworth filter
b, a = signal.butter(N=5, Wn=200, fs=Fs)
output = signal.filtfilt(b, a, sig)
wavfile.write('Butterworth.wav', Fs, (output*2**16).astype(np.int16))

# Bessel filter
b2, a2 = signal.bessel(N=5, Wn=0.5, analog=True)
output = signal.filtfilt(b2, a2, sig)
wavfile.write('Bessel.wav', Fs, (output*2**16).astype(np.int16))

# Flattop filter
window = signal.flattop(20)
b3 = np.ones(window.__len__()) * (1/window.__len__())
output = signal.filtfilt(b3, a2, sig)
wavfile.write('Flattop.wav', Fs, (output*2**16).astype(np.int16))
# w, h = scipy.signal.freqz(b, fs=2*np.pi*Fs)
# angles = np.unwrap(np.angle(h))
#
# fig1, ax1 = plt.subplots()
# ax1.plot(w, 20 * np.log10(np.abs(h)), 'b')
# ax1.set_xlabel('Frequency [Hz]')
# ax1.set_ylabel('Amplitude [dB]', color='b')
# ax1.set_title('Butterworth frequency and phase response in semi-log scale')
# ax1.grid(axis='both', which='both')
# ax1.axvline(200, color='red', lw=1)  # cut-off frequency
# ax1.set_xscale("log")
#
# fig3, ax3 = plt.subplots()
# ax3.plot(w, angles, 'g')
# ax3.set_ylabel('Angle [rad]', color='g')

