import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from scipy.integrate import simps

# Q1
Fs = 100
amplitude = 1
duration = 1  # in seconds
N = Fs * duration
t = np.linspace(0, duration, num=N, endpoint=False)

# create the sig
frequency = 5
sig = amplitude * signal.sawtooth(2 * np.pi * frequency * t)
plt.plot(t, sig)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


def sawtooth_harmonics(number_of_harmonics):
    n = number_of_harmonics
    fig, ax = plt.subplots()
    ax.plot(t, sig)
    sum = 0

    # it's an odd function, fft has only sin
    def b(n):
        return (2.0 / duration) * simps(sig * np.sin(2.0 * np.pi * n * t / duration), t)

    for i in range(1, n + 1):
        sum += b(i) * (np.sin(2.0 * np.pi * i * t / duration))
        ax.plot(t, sum)
        ax.set_xlabel('$t$ [s]')
        ax.set_ylabel('$A$ [s]')
    ax.legend()
    ax.set_title("Sawtooth sig & harmonics")
    plt.show()

# sawtooth_harmonics(100)
# we need 100 harmonics to represent this wave well
