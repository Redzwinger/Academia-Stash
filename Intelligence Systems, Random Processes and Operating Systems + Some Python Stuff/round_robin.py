#Program for Round Robin

import numpy as np
import numbers
import os
os.system("")

print("\n\tThis is a program for Round Robin\n")

numba_o_processes = int(input(" Please enter the number of processes: "))
print(" ")

time_burst = []

for b in range(1, numba_o_processes + 1):
    a_thing = int(input(f" Please enter the Burst Time for Process {b} : "))
    time_burst.append(a_thing)

print(f" ")

quantum = int(input(" Please enter the time quantum: "))
print(" ")

#Calculating Waiting Time for Each Process.

waiting_time = []
rem_bt = [0] * numba_o_processes

for i in range(numba_o_processes): 
	rem_bt[i] = time_burst [i]
time = 0

while(1):
		done = True
		for i in range(numba_o_processes):
			if (rem_bt[i] > 0) :
				done = False

				if (rem_bt[i] > quantum) :
					time += quantum
					rem_bt[i] -= quantum
				else:
					time = time + rem_bt[i]

					waiting_time.append(time - time_burst[i])
					rem_bt[i] = 0

		if (done == True):
			break

#Calculating the Turn Around Time.

turn_ar_time = []
yet_another_thing = int()

for e in range(numba_o_processes):
    turn_ar_time.append(time_burst[e] + waiting_time[e])

#Calculting Average Waiting Time.

waiting_time = [0] * numba_o_processes
total_waiting_time = 0

for w in range(numba_o_processes):
	total_waiting_time += waiting_time [w]

#Calculting Average Turn Around Time.

turn_ar_time = [0] * numba_o_processes
total_turn_ar_time = 0

for a in range(numba_o_processes):
	total_turn_ar_time += turn_ar_time [a]

#End Print

print('{} {} {} {}'.format('\n |Processes|', '|Burst Time|',
      ' |Waiting Time|', ' |Turn Around Time|'))

for p in range(len(time_burst)):
    print("\n     P",p+1, f"    \t",time_burst[p], f"\t\t",waiting_time[p],
          f"\t\t",turn_ar_time[p])

print(f"\n\n The Average Waiting Time is {total_waiting_time}")
print(f"\n The Turn Around Time is {total_turn_ar_time}", end="\n")

print(f"\n\tThank You For using this program!\n\n\t", 
      "\033[3m" + "Program by Achintya Kamath" + "\x1B[0m", end="\n\n\n")

