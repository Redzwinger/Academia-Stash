import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.contingency import margins
import os
os.system("")

print("\nHi, this program solves the following question: ")

print("\nThe Joint Probability Function of two discrete random variables X and Y is given by: "
      "\nf(x,y)= ", "\033[4m" + "2x+y" + "\033[0m", "\n          42"
      "\nwhere, x and y can assume all integers such that"
      "\n0 ≤ x ≤ 2, 0 ≤ y ≤ 3 and f(x, y) = 0, otherwise."
      "\n\nWrite a python program to plot the probabilities of Joint PMF."
      "\nFurther obtain:"
      "\ni) Marginal PMF of x and y."
      "\nii) Mean and Variance of x and y."
      "\n-----------------------------------------------------------------------------------"
      "\n\t\t*** Program by Achintya Kamath ***"
      "\n-----------------------------------------------------------------------------------")

print("Answer: \ni)", end=" ")
print("\n\tf(x,y)=0, \n\tcan be represented as: ", end="\n\n")
z=np.zeros([3,3])
print("\t\t" + str(z).replace('\n','\n\t\t'))

x = [0,1,2]
y = [1,2,3]

a=len(x)
b=len(y)

print("\n\tnow, f(x,y)= ", "\033[4m" + "2x+y" + "\033[0m", "\n\t               42")
print("\n\twhere, x and y are 0 ≤ x ≤ 2 and 0 ≤ y ≤ 3 respectively, ",
     "\n\tthis can be represented as: ", end="\n\n")

for x in range(a):
    for y in range(b):
        z[x,y]=(2*x+3*(y+1))/72
print("\t" + str(z).replace('\n','\n\t'), end="\n")

joint_probability_x_y = np.array(z)

x, y =margins(joint_probability_x_y)

print("\n\tTherefore, The Marginal PMF of X is: ")
pmf_x = x
print("\n\t\t" + str(pmf_x).replace('\n','\n\t\t'), end="\n\n")

print("\tAnd, The Marginal PMF of Y is: ")
pmf_y = y
print("\n\t\t" + str(pmf_y.T).replace('\n','\n\t\t'), end="\n")

print("\nii)", end=" ")

a=np.array([0,1,2])
b=pmf_x

a.shape = (a.size, 1)

print("\n\t\t", a.shape)
print("\n\t\t", b.shape)

c=a*b

print("\n\t\t" + str(c).replace('\n','\n\t\t'), end="\n")

mu_x=np.sum(c)
print("\n\tMean of x is: {}".format(mu_x), end=" ")

var_x=np.sum(a*a*b) - (mu_x*mu_x)

print("\n\tVariance of x is {}".format(var_x), end="\n\n")

print("-----------------------------------------------------------------------------------"
      "\n\t\t*** Program by Achintya Kamath ***"
      "\n-----------------------------------------------------------------------------------")




