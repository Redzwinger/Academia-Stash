#Program for FCFS

import numpy as np
import numbers
import os
os.system("")

print("\n\tThis is a program for FCFS\n")

numba_o_processes = int(input(" Please enter the number of processes: "))
print(" ")

time_burst = []

for b in range(1, numba_o_processes + 1):
    a_thing = int(input(f" Please enter the Burst Time for Process {b} : "))
    time_burst.append(a_thing)

#Calculating Waiting Time for Each Process.

waiting_time = [
    0,
]
another_thing = int()

for w in range(len(time_burst) - 1):
    another_thing += time_burst[w]
    waiting_time.append(another_thing)

#Calculting Average Waiting Time.

average_waiting_time = round(np.mean(waiting_time), 2)

#Calculating the Turn Around Time.

turn_ar_time = []
yet_another_thing = int()

for t in range(1, numba_o_processes):
    a_thing = waiting_time[t]
    turn_ar_time.append(a_thing)

turn = turn_ar_time[len(turn_ar_time) - 1] + time_burst[numba_o_processes - 1]
turn_ar_time.append(turn)

#Calculting Average Turn Around Time.

average_turn_ar_time = round(np.mean(turn_ar_time), 2)

#End Print

print('{} {} {} {}'.format('\n |Processes|', '|Burst Time|',
      ' |Waiting Time|', ' |Turn Around Time|'))

for p in range(len(time_burst)):
    print("\n     P",p+1, f"   \t",time_burst[p], f"\t\t",waiting_time[p],
          f"\t\t",turn_ar_time[p])

print(f"\n\n The Average Waiting Time is {average_waiting_time}")
print(f"\n The Turn Around Time is {average_turn_ar_time}", end="\n")

print(f"\n\tThank You For using this program!\n\n\t", 
      "\033[3m" + "Program by Achintya Kamath" + "\x1B[0m", end="\n\n\n")


