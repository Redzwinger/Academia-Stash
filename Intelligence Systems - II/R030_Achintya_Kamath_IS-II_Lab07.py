'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 07
Date: 28/02/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 07 \n Date: 28/02/2024")

print("\n ############# ################ ####################\n")

import random as d20
import numpy as np
import matplotlib.pyplot as plt

# Fitness Function
def FunkyFit(x,y):
    Fit1 = (x - 3.14)**2
    Fit2 = (y - 2.72)**2

    Fit3 = np.sin(3*x + 1.41) + np.sin(4*y - 1.73)

    Thing = Fit1 + Fit2 + Fit3

    return Thing

# Updating Velocity
def update_velo(particle, velo, BestP, BestG):
    minW = 0.5
    SuperMax = 1.0
    cc = 0.1

    Particle_Num = len(particle)
    Velo_new = np.array([0.0 for i in range(Particle_Num)])

    random1 = d20.uniform(0, SuperMax)
    random2 = d20.uniform(0, SuperMax)

    W = d20.uniform(minW, SuperMax)
    C1 = cc
    C2 = cc

    for i in range(Particle_Num):
        Velo_new[i] = W*velo[i] + C1*random1*(np.argmin(BestP[i]) - particle[i]) + C2*random2*(BestG[i] - particle[i])

    return Velo_new

def update_pos(particle, velo):
    new_particle = particle + velo
    return new_particle

def TwoDimensional_PSO(pop, die, minPos, maxPos, gen, fit_crits):
    particles = [[d20.uniform(minPos, maxPos) for j in range(die)] for i in range(pop)]

    BestP_pos = particles
    #p = [i for i in range(pop)]
    BestP_fit = [FunkyFit(p[0], p[1]) for p in particles]

    BestG_index =np.argmin(BestP_fit)
    BestG_pos = BestP_pos[BestG_index]

    velocities = [[0.0 for j in range(die)] for i in range(pop)]

    for t in range(gen):
        if np.average(BestP_fit) <= fit_crits:
            break
        else:
            for n in range(pop):
                velocities[n] = update_velo(particles[n], velocities[n], BestP_pos, BestG_pos)
                particles[n] = update_pos(particles[n], velocities[n])
            
            BestP_fit = [FunkyFit(p[0], p[1]) for p in particles]
            BestG_index = np.argmin(BestP_fit)
            BestG_pos = BestP_pos[BestG_index]

    print(' Global Best Position: ', BestG_pos)
    print(' Best Fitness Value: ', min(BestP_fit))
    print(' Average Particle Fitness Value: ', np.average(BestP_pos))
    print(' Number of Generations: ', t, end="\n\n")    
 
# Contour Plot
x, y = np.array(np.meshgrid(np.linspace(0, 5, 100), np.linspace(0, 5, 100)))

z = FunkyFit(x, y)

minX = x.ravel()[z.argmin()]
minY = y.ravel()[z.argmin()]

plt.figure(figsize=(7,5))

plt.imshow(z, extent=[0, 5, 0, 5], origin = 'lower', cmap = 'viridis', alpha = 0.5)
plt.colorbar()

plt.plot([minX], [minY], marker = 'x', markersize=5, color='white')

contours = plt.contour(x, y, z, 10, colors='black', alpha=0.4)
plt.clabel(contours, inline=True, fontsize=10, fmt = "%.0f")
plt.show()

# Performing 2 Dimensional Particle Swarm Optimization
TwoDimensional_PSO(100, 2, -100, 100, 400, 0.0004)

# Catatonically Crafted by Redzwinger #