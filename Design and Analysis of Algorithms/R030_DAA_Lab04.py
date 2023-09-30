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

# Function for Job Sequencing
def Job_Sequencing(job_stuff, t):
    
    n = len(job_stuff)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if job_stuff[j][2] < job_stuff[j + 1][2]:
                
                job_stuff[j], job_stuff[j + 1] = job_stuff[j + 1], job_stuff[j]

    result = [False] * t
    job_num = ['-1'] * t
    profits_gained = int()
    
    for i in range(len(job_stuff)):
        for j in range(min(t - 1, job_stuff[i][1] - 1), -1, -1):
            
            if result[j] is False:
                
                result[j] = True
                job_num[j] = job_stuff[i][0]
                profits_gained += job_stuff[i][2]
                break
            
    print("Job: ", job_num)
    print("Profits: ", profits_gained)
    
# Sample Array
JobSeq= [['J1',2,60], ['J2',1,100], ['J3',3,20], ['J3',2,40], ['J4',1,20]]

print("The following sequece of jobs leads to the maximum profit: ")
Job_Sequencing(JobSeq,3)