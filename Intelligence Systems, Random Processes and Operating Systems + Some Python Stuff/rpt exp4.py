from os import name
from tkinter import N
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10*np.pi,1024)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel("Time --->")
plt.ylabel("Magnitude --->")
plt.title("Sine Signal")
plt.show()

y.shape
print("Y shape =", y.shape)
r = np.correlate(y,y,mode='full')

r.shape
print("R shape =", r.shape)

2*len(y)-1
m = np.linspace(-2*np.pi, 2*np.pi, 2*len(y)-1)

print("M=", m)
print("R=", r)

plt.plot(m,r)
plt.xlabel("Time Lag " + '$\tau$' + "--->")
plt.ylabel("Magnitude --->")
plt.title("Auto Correlation : Sine Signal")
plt.show()

n =np.random.normal(-1,1,len(x))

yn = y+n

plt.plot(x,yn)
plt.xlabel("Time --->")
plt.ylabel("Magnitude --->")
plt.title("Noisy Sine Signal")
plt.show()

rn = np.correlate(y,yn,mode='full')
m = np.linspace(-2*np.pi, 2*np.pi, 2*len(y)-1)
plt.plot(m,rn)
plt.xlabel("Time Lag " + '$\tau$' + "--->")
plt.ylabel("Magnitude --->")
plt.title("Cross Correlation : Sine Signal")
plt.show()

nn = np.correlate(n,n,mode="full")
yy = np.correlate(y,y,mode="full")

np.sqrt(nn[1024]*yy[1024])

(nn[1024]*yy[1024])/2
np.max(rn)

