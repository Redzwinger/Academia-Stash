import numpy as np
import random
import matplotlib.pyplot as plt

gambling_money = 50
gambling_goal = 100

w_or_1 = random.randrange(-1,2,2)
w_or_1

def gamblers_ruin(x,y):
    gambling_money = x
    gambling_goal = y
    gambling_sim = []

    while gambling_money in range(1, gambling_goal):
        w_or_1 = random.randrange(-1,2,2)
        gambling_money = gambling_money + w_or_1
        gambling_sim.append(gambling_money)
    return gambling_sim

gamblers_ruin(50, 100)

plt.figure(figsize=(12,4))
plt.plot(gamblers_ruin(50, 100), color="red")
plt.yticks(np.arange(-20,120,10))
plt.axhline(y=0, color = "yellow")
plt.axhline(y=100, color = "purple")
plt.xlabel("Number of Bets")
plt.ylabel("Money")
plt.title("Gambling Simulations")
plt.show()




