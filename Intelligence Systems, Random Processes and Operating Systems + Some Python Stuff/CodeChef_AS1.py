'''
Contest Link - https://www.codechef.com/MPF12AP001
Ended:15/02/2022
'''

'''
Problem 1 - https://www.codechef.com/MPF12AP001/problems/CORRSLP
Solved:14/02/2022
'''

'''
#code start
T=int(input()) #number of test cases

for s in range(T):
    N,L,X=map(int,input().split())
    
    #number of slippers, number of left slippers, cost of each pair of slippers.
    
    ttl=int(0)
    ttl_R=N-L
    
    if ttl_R<L: #if the number of Right slippers are more than the Left
        extra=L-ttl_R
        fin_L=L-extra
        ttl=((fin_L+ttl_R)/2)
        print(int(ttl*X))
        
    
    elif ttl_R>L: #if the number of Right slippers are less than the Left
        extra=ttl_R-L
        R=ttl_R-extra
        ttl=((R+L)/2)
        print(int(ttl*X))
        
    else:
        ttl=((ttl_R+L)/2) #if the number of slippers are equal
        print(int(ttl*X))
 '''

'''
Problem 2 - https://www.codechef.com/MPF12AP001/problems/WODPLT043
Solved:14/08/2022
'''

#just no comments for this one :|

'''
#code start
T=int(input()) #number of test cases

for p in range(T):
    N=int(input())

    if(N%2!=0):
        jumps=int((N + 1) / 2) 
        #finding the median since "you" moves first which makes the last plate be the median of the the total
        print(jumps)
'''
