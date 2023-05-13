import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import IPython

global pi
pi = np.pi
rows = int(4)
columns = int(2)

fs = 1000 #Frequency

t = np.arange(1000) / fs
#print(t)

signal_a = np.sin(2*np.pi*100*t) 

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.plot(t, signal_a, color='xkcd:red pink')
    plt.xlabel("Time --->")
    plt.ylabel("Amplitude --->")
    plt.title("Sine Signal with Frequency 100 Hz")

f2 = abs(np.fft.fft(signal_a))
#print(f2.shape, end="\n\n")

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.stem(f2[0:600])
    plt.xlabel("Magnitude --->")
    plt.ylabel("Frequency --->")
    plt.title("PSD of Sine Signal")

signal_b =np.sin(2*np.pi*20*t)

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.plot(t, signal_b, color="xkcd:jade")
    plt.xlabel("Time --->")
    plt.ylabel("Amplitude --->")
    plt.title("Sine Signal with Frequency 20 Hz")

with plt.xkcd():
    plt.figure(figsize=(12,4))

signal_c = signal_a + signal_b

'''
print(signal_c, end="\n")
print(t.shape, end="\n")
print(t, end="\n")
'''

with plt.xkcd():
    plt.plot(t[0:300], signal_c[0:300], color="xkcd:pinky red")
    plt.xlabel("Time --->")
    plt.ylabel("Amplitude --->")
    plt.title("Addition of 2 Sine Signal (300)")

with plt.xkcd():
    plt.plot(t[0:500], signal_c[0:500], color="xkcd:deep violet")
    plt.xlabel("Time --->")
    plt.ylabel("Amplitude --->")
    plt.title("Addition of 2 Sine Signal (500)")

f3 = abs(np.fft.fft(signal_c))

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.stem(f3[0:300])
    plt.xlabel("Magnitude --->")
    plt.ylabel("Frequency --->")
    plt.title("PSD of Addition of 2 Sine Signals")

#Filtering the low and high frequency components using low and high pass filter systems

fc = 30 #cut off frequency
w1 = fc / (fs / 2)
b,a = signal.butter(5,w1,"low")
output = signal.filtfilt(b,a,signal_c)

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.plot(t, output, color="xkcd:pinkish red")
    plt.xlabel("Time --->")
    plt.ylabel("Amplitude --->")
    plt.title("Signal with Low Frequency Component Filtered Out")

fs = abs(np.fft.fft(output))

with plt.xkcd():
    plt.figure(figsize=(12,4))
    plt.stem(f2[0:500])
    plt.xlabel("Magnitude --->")
    plt.ylabel("Frequency --->")
    plt.title("PSD of Signal with Low Frequency Component Filtered Out")

fs, data = wavfile.read('D:\Achintya\Visual Studio\Py 3.10.5\Spider-Man.wav')

print("\n FS =", fs)
print("\n Data =\n\n", data)

IPython.display.Audio(data.T, rate = fs)

plt.figure(figsize=(12,4))
plt.plot(data, color="xkcd:pale turquoise")
plt.xlabel("Frequency --->")
plt.ylabel("Magnitude --->")
plt.title("Spider-Man.wav Audio File")

f4 = abs(np.fft.fft(data))
plt.figure(figsize=(12,4))
plt.plot(f4[0:int(len(f4)/2)], color="xkcd:sickly green")
plt.xlabel("Frequency --->")
plt.ylabel("Magnitude --->")
plt.title("PSD of Spider-Man.wav Audio File")

fc = 2000
w = fc/(fs/2)
print("\n",fs)
print("\n",w)
b, a = signal.butter(25,w,'low')
output = signal.filtfilt(b,a,data, padlen = 1)

plt.figure(figsize=(12,4))
plt.plot(output, color="xkcd:yellow orange")

b, a = signal.butter(25,w,'high')
output1 = signal.filtfilt(b,a,data, padlen = 1)

plt.figure(figsize=(12,4))
#plt.plot(output1, color="xkcd:robin's egg blue")

w, h = signal.freqz(b, a)
plt.plot(w, abs(h))
plt.title("Magnitude Response")
plt.xlabel("Frequency --->")
plt.ylabel("Amplitude --->")

plt.show(block=True) 


