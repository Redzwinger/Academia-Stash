# -*- coding:latin1 -*-
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B2
Date: 07/10/2022
Experiment 9
'''

import numpy as np
import scipy.stats as stats

print("\n ############# ################ #################### ################ ############# ################ #################### ################ ############# ################ #################### ################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B2 \n Date: 07/10/2022 \n Experiment 9\n")

print("\n\t \t \t----------------------------------------------------------------------------------------------------------------")

print("\t \t \tThis program solves hypothesis questions, based on T-Test and F-Test, using the 'scipy.stats' module for python.", end=" ")

print("\n\t \t \t----------------------------------------------------------------------------------------------------------------")

#Q1

print("\n\n §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§ÆÆ§ §ÆÆ§ÆÆ§ÆÆ§")

print("\n\n Q1. A sample of size 13 gave an estimated population variance of 3.0, while another sample of size 15 gave an estimate of 2.5. Could both samples be from populations with the same variance?")

print("\n Solution:")

def f_test(thing, thing2, vari_thing, vari_thing2):

    f = vari_thing/vari_thing2

    print("\n\tF-Statistic =", vari_thing, "/", vari_thing2, "=", f, end=" ")

    p_value = 1-stats.f.cdf(f, thing-1, thing2-1)

    print("\n\tP-Value of F-Statistic =", p_value)

    if f > 0.025:
        print("\n\tTherefore, Ho is accepted.")
    else:
        print("\n\tTherefore, Ho is rejected.")

thing = 13
vari_thing = 3.0
thing2 = 15
vari_thing2 = 2.5

f_test(thing, thing2, vari_thing, vari_thing2)

#Q2

print("\n\n ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß¬¬ß ß¬¬ß¬¬ß¬¬ß")

print("\n\n Q2. The nicotine contents in two random samples of tobacco are given below: \n\n Sample 1: 21   24   25   26   27\n Sample 2: 22   27   28   30   31   36\n\n Can you say that the two samples have same variance?")

print("\n Solution:")

def f_test2(sam1, sam2):

    sam1 = np.array(sam1)
    sam2 = np.array(sam2)

    vari_sam1 = np.var(sam1, ddof=1)
    vari_sam2 = np.var(sam2, ddof=1)

    degof_sam1 = sam1.size-1
    degof_sam2 = sam2.size-1
    
    f1 = vari_sam1/vari_sam2

    print("\n\tF-Statistic =", vari_sam1, "/", vari_sam2, "=", f1, end=" ")

    p_value = 1-stats.f.cdf(f1, degof_sam1, degof_sam2)

    print("\n\tP-Value of F-Statistic =", p_value)

    if f1 > 0.025:
        print("\n\tTherefore, Ho is accepted.")
    else:
        print("\n\tTherefore, Ho is rejected.")

sam1 = [21, 24, 25, 26, 27]
sam2 = [22, 27, 28, 30, 31, 36]

f_test2(sam1, sam2)

#Q3

print("\n\n ¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢££¢ ¢££¢££¢££¢££¢ ¢££¢££¢££¢")

print("\n\n Q3. Two different types of drugs A and B were tried on certain patients for increasing weight. \n     Five persons were given drug A and 7 persons were given drug B. \n     The increase in weight (in kg) is given below: \n\n Drug A:   3.6   5.5   5.9   4.1   1.4 \n Drug B:   4.5   3.6   5.5   6.8   2.7   3.6   5.0 \n\n Do the two drugs differ significantly with regard to their effect in increasing weight?")

print("\n Solution:")

drug_a = np.array([3.6, 5.5, 5.9, 4.1, 1.4])
drug_b = np.array([4.5, 3.6, 5.5, 6.8,  2.7, 3.6, 5.0])

t, p = stats.ttest_ind(a = drug_a, b = drug_b, equal_var = True)

print("\n\tT-Statistic =", t, end=" ")

print("\n\tP-Value of T-Statistic =", p)

if t >= p:
    print("\n\tTherefore, Ho is accepted.")
else:
    print("\n\tTherefore, Ho is rejected.")

#Q4

print("\n\n ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶¤¤¶ ¶¤¤¶¤¤¶¤¤¶")

print("\n\n Q4. The annual rainfall at a certain place is normally distributed with mean 30. \n     If the rainfall during the past 8 years are: \n\n 31.1, 30.7, 24.3, 28.1, 27.9, 32.2, 25.4 and 29.1 \n\n Can we conclude that average rainfall during the past 8 years is less than the normal rainfall?")

print("\n Solution:")

annual_rainfall_mean = 30

eight_years_of_rain = np.array([31.1, 30.7, 24.3, 28.1, 27.9, 32.2, 25.4, 29.1])

t1, p7 = stats.ttest_1samp(a = eight_years_of_rain, popmean = annual_rainfall_mean)

print("\n\tT-Statistic =", t1, end=" ")

print("\n\tP-Value of T-Statistic =", p7)

if t1 < p7:
    print("\n\tTherefore, Ho is accepted.", end="\n\n")
else:
    print("\n\tTherefore, Ho is rejected.")





