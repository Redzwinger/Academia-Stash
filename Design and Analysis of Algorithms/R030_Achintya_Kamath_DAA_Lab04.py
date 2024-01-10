'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 04
Date: 13/09/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 04 \n Date: 13/09/2023")

print("\n ############# ################ ####################\n")

def find_max_profit_job_sequence(jobs, total_time):
    jobs.sort(key=lambda x: (-x[2], x[1]))

    is_slot_taken = [False] * total_time
    job_sequence = ['-1'] * total_time
    total_profit = 0

    for job in jobs:
        deadline = min(total_time - 1, job[1] - 1)
        while deadline >= 0:
            if not is_slot_taken[deadline]:
                is_slot_taken[deadline] = True
                job_sequence[deadline] = job[0]
                total_profit += job[2]
                break
            deadline -= 1

    print(" Job Sequence:", job_sequence)
    print(" Total Profits Gained:", total_profit)

# Sample Array
job_info = [['J1', 5, 80], ['J2', 2, 10], ['J3', 1, 20], ['J4', 7, 40], ['J5', 1, 200]]

print(" The following sequence of jobs leads to the maximum profit: ", end="\n\n")
find_max_profit_job_sequence(job_info, 4)

# Charmingly Crafted By Redzwinger #

