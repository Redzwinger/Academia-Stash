print(" \n############# ################ #################### ################\n")
print(" Name: Achintya Kamath \n Roll Number: R030 \n MBA Tech Artificial Intelligence \n Batch: B2 \n Date: 11/10/2022 \n Experiment 10 - Disk Scheduling")

def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)

def findMin(diff):
 
    index = -1
    minimum = 999999999
 
    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index

def SSTFDS(head, request):

    if (len(request) == 0):
            return

    l = len(request)
    diff = [0] * l

    for i in range(l):
        diff[i] = [0, 0]
   
    seek_count = 0
    seek_sequence = [0] * (l + 1)
         
    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)
             
        diff[index][1] = True

        seek_count += diff[index][0]

        head = request[index]
    seek_sequence[len(seek_sequence) - 1] = head
                                                         
    print("\n The Seek Sequence is: ", seek_sequence)

    print(" Total number of seek operations = ", seek_count)

print(f"\n\tThis program showcases the SSTF Disk Scheduling Algorithm.", end="\n\t")

print(" ", end="\n")

initial_pos = int(input(" Please enter the initial position / head of the disc arm: "))

requests = list(map(int, input(' Please enter the request sequence: ').strip().split()))

print(" \n", SSTFDS(initial_pos,requests))

