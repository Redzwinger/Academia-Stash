'''
Name: Achintya Kamath
Roll Number: R030
Batch: B1
Signals and Image Processing
MBA Tech Artificial Intelligence
'''

# COMPLETED THING ON COLAB
# LINK: https://colab.research.google.com/drive/1_iflEFvoWHbFnwv0tJJ4MDohQ-OmhdLX?usp=sharing


#first thing
import numpy as np
import matplotlib.pyplot as plt
import xkcd

t = np.arange(0,1,0.03)
f = 1

x = np.sin(2*np.pi*f*t)
y = np.cos(2*np.pi*f*t)

plt.subplot(3,3,1)
plt.plot(t,x, color="xkcd:lime green")
plt.subplot(3,3,2)
markerline, stemlines, baseline = plt.stem(t,x, linefmt='green', markerfmt='D', use_line_collection=None)
markerline.set_markerfacecolor('red')

plt.subplot(3,3,3)
plt.plot(t,y, color="xkcd:dark pink")
plt.subplot(3,3,4)
markerline, stemlines, baseline = plt.stem(t,y, linefmt='red', markerfmt='D', use_line_collection=None)
markerline.set_markerfacecolor('yellow')


#second thing
t1 = np.arange(0,10,1)
u = np.where(t1<=5,1,0)

plt.subplot(3,3,5)
plt.plot(t1,u, color="xkcd:turquoise")

plt.subplot(3,3,6)
markerline, stemlines, baseline = plt.stem(t1,u, linefmt='blue', markerfmt='D', use_line_collection=None)
markerline.set_markerfacecolor('green')


#third thing
t2 = np.arange(0,10,1)
r = (np.arange(0,10,1))

plt.subplot(3,3,7)
plt.plot(t2,r, color="xkcd:bright purple")

plt.subplot(3,3,8)
markerline, stemlines, baseline = plt.stem(t2,r, linefmt='violet', markerfmt='D', use_line_collection=None)
markerline.set_markerfacecolor('yellow')


#fourth thing
t3 = np.linspace(0,10,100)
e = np.exp(t3)
plt.subplot(3,3,9)
plt.plot(t3,e, color="xkcd:robin's egg blue")

plt.show()
