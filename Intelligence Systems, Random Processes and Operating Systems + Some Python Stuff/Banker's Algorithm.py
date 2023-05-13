#Program for Banker's Algorithm
import numpy as np

print("\n This program showcases the Banker's Algorithm for the following example,\n")

def check(i):
    for j in range(no_r):
        if(needed[i][j]>available[j]):
            return 0
    return 1


no_p = 5
no_r = 3

Sequence = np.zeros((no_p,),dtype=int)
visited = np.zeros((no_p,),dtype=int)

allocated = []

allocated = np.array([[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]])
maximum = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]])

needed = maximum - allocated
available = np.array([3,3,2])

available_for_display = [3,3,2]

count = 0
while( count < no_p ):
    temp=0
    for i in range( no_p ):
        if( visited[i] == 0 ):
            if(check(i)):
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(no_r):
                    available[j] += allocated[i][j] 
    if(temp == 0):
        break

print('{} {} {} {}'.format('\n |Processes|', '\t|Allocated|',
      ' \t|Maximum|', ' \t|Available|'))

for p in range(len(allocated)):
    print("\n     P",p+1, f"   \t ",allocated[p], f"\t",maximum[p],
          f"\t",available_for_display)

if(count < no_p):
    print('\n\tThe System is Unsafe\n')
else:
    print("\n\tThe System is Safe,")
    print("\tand hence, the Safe Sequence of processes is: ",Sequence+1, ", ")
    print("\twith the Available Resource being:",available, end="\n\n")

