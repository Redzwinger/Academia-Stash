'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Computer Networks
Lab 05
Date: 22-08-2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Computer Networks \n Lab 05 \n Date: 22/08/2023")

print("\n ############# ################ ####################\n")

import numpy as np

def what_to_do():
    to_do = ["leak","recieve"]
    do = np.random.choice(to_do)
    return do

def leaky(cur_do):
    print(f"Current Action : {cur_do}")
    
    if cur_do == "leak":
        if len(queue) != 0:
            storage_thing = n
            while storage_thing > 0:
                if storage_thing > queue[0]:
                    storage_thing = storage_thing - queue[0]
                    print(f"> Packet of size {queue[0]} has leaked.")
                    queue.pop(0)
                    m = len(queue)
                    if m == 0:
                        break
                else:
                    break
        else:
            print("> The bucket is empty!")
    else:
        sz = sum(queue)
        bit = np.random.randint(100,200)
        if bit + sz <= buck_cap:
            queue.append(bit)
            print(f"> Packet of size {bit} has been accepted.")
        else:
            print(f"> Packet of size {bit} has been rejected.")
    print(f"Bucket => {queue}")

global n,max_capacity, queue
queue = [200,700,500,450,400,200]
n = 1000
buck_cap = 1000
time_int = 10

print(f"Bucket => {queue}")
print("+--------------------------------------+")

for t in range(time_int):
    print(f"|For T = {t}                              |")
    print("+--------------------------------------+")
    selected_action = what_to_do()
    leaky(selected_action)
    print("  ")
    print("+--------------------------------------+")
    
while True:
    v = input("")
    if v == "m":
        break
    else:
        pass