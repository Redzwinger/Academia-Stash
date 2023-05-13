'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B2
Date: 30/09/2022
Experiment 8
'''

import numpy as np
import math
from numpy.random import randn
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ztest

print("\n ############# ################ #################### ################ ############# ########## ##############\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B2 \n Date: 07/10/2022 \n Experiment 9\n")

#Q1
print("\n\tThis program solves hypothesis questions, based on Z-Test, using the 'statsmodels' module for python.")

print("\t-----------------------------------------------------------------------------------------------------")

print("\nQ1. A machine is set to produce metal plates of thickness 1.5 cms with standard deviation of 0.2 cm. \n     A sample of 100 plates produced by the machine gave an average thickness of 1.52 cms. \n     Is the machine fulfilling the purpose?")

print("\n Solving Q1 using Z-Test...")

alpha = 0.05
null_mean = 1.5

data_1 = np.random.normal(1.52, 0.2, 100)

print("\n ",'Mean = %.2f stdv = %.2f' %(np.mean(data_1), np.std(data_1)), end="\n")

z, p = ztest(data_1, value = null_mean, alternative = 'two-sided')

print("\n ", z, "\n ", '{0:0.2f}'.format(p), end="\n")

print("\n Comparing H0 with H_alpha(0.05)...")

if p<0.05:
    print("\n H0 > H_alpha(0.05) \n  Therefore, H0 is rejected.", end="\n\n")
else:
    print("\n H0 < H_alpha(0.05) \n  Therefore, H0 is accepted.", end="\n\n")

print(" --------------------------------------------------------\n OoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoO\n --------------------------------------------------------")

#Q2
print("\n#Q2. In a random sample of size 500, the mean is found to be 20. \n     In independent sample of 400, the mean is 15. \n     Could the sample have been drawn from the same population with SD 4?")

print("\n Solving Q2. using Z-Test...")

alpha_1 = 0.05
null_mean_1 = 1.5

sam1 = np.random.normal(20, 4, 500)
sam2 = np.random.normal(15, 4, 400)

print("\n ",'Mean of first sample = %.2f stdv = %.2f' %(np.mean(sam1), np.std(sam1)), end="\n")

print("\n ",'Mean of second sample = %.2f stdv = %.2f' %(np.mean(sam2), np.std(sam2)), end="\n")

z1, p1 = ztest(sam1, sam2, value = null_mean_1, alternative = 'two-sided')

print("\n ", z1, "\n ", '{0:0.2f}'.format(p1), end="\n")

print("\n Comparing H0 with H_alpha(0.05)...")

if p1<0.05:
    print("\n H0 > H_alpha(0.05) \n  Therefore, H0 is rejected.", end="\n\n")
else:
    print("\n H0 < H_alpha(0.05) \n  Therefore, H0 is accepted.", end="\n\n")

print(" --------------------------------------------------------\n OoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoOOoOoOoO\n --------------------------------------------------------")

#Q3
print("\n#Q3. In 2015 in a big city, on a sample of 1000 drivers, 17% were penalised for rash driving. \n     The following year, on a sample of 1000 drivers, 21% were penalised for rash driving. \n     Is there any a significant difference between the percent of drivers for rash driving ?")

print("\n Solving Q3. using Z-Test...")

success = np.array([170,210])

total_sam_size = np.array([1000,1000])

z2, p2 = proportions_ztest(count = success, nobs = total_sam_size, alternative = "two-sided")

print("\n ", z2, "\n ", '{0:0.10f}'.format(p2), end="\n")

print("\n Comparing H0 with H_alpha(0.05)...")

if p1<0.05:
    print("\n H0 > H_alpha(0.05) \n  Therefore, H0 is rejected.", end="\n\n")
else:
    print("\n H0 < H_alpha(0.05) \n  Therefore, H0 is accepted.", end="\n\n")

#Q4
print("\n#Q4. 15.5% of a random sample of 1600 undergraduates were smokers, \n     where as 20% of a random sample of 900 postgraduates were smokers in a states. \n     Can we conclude that less number of undergraduates are smokers than the postgraduates?")

print("\n Solving Q4. using Z-Test...")

success1 = np.array([248,180])

total_sam_size1 = np.array([1600,900])

z3, p3 = proportions_ztest(count = success1, nobs = total_sam_size1, alternative = "two-sided")

print("\n ", z3, "\n ", '{0:0.10f}'.format(p3), end="\n")

print("\n Comparing H0 with H_alpha(0.05)...")

if p1<0.05:
    print("\n H0 > H_alpha(0.05) \n  Therefore, H0 is rejected.", end="\n\n")
else:
    print("\n H0 < H_alpha(0.05) \n  Therefore, H0 is accepted.", end="\n\n")
