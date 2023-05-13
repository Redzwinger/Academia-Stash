'''
Contest Link - https://www.codechef.com/MPF12PP001
Ended:09/08/2022
'''

'''
Problem 1 - https://www.codechef.com/MPF12AP001/problems/TYRES
Solved:09/02/2022
'''

'''
#code start

T=int(input()) #number of testcases

for c in range(T):
    num_o_tyre=int(input()) #number of tyres
    
    print("YES" if num_o_tyre%4!=0 and num_o_tyre%2==0 else "NO")
'''

'''
Problem 2 - https://www.codechef.com/MPF12AP001/problems/PRB01
Solved:09/02/2022
'''

'''
#code start

for i in range(int(input())): #number of testcases
    n=int(input()) #inputs
    if n>1:
        for i in range(2,n):
            if n%i == 0: #checking for primality
                print("no")
                break
        else:
            print("yes")
    else:
        print("no")
'''

'''
Problem 3 - https://www.codechef.com/MPF12AP001/problems/LOOP
Solved:09/02/2022
'''

'''
#code start

num_o_test = int(input()) #number of test cases

for i in range(num_o_test):
    A,B,M=map(int,input().split()) #inputs for integers A, B and M
    
    x,y=min(A,B),max(A,B) #Finding maximum and minimum of A and B
    
    x1=M-y+x #difference between M and the maximum
    y1=y-x #difference between M and the minimum
    
    print(min(x1,y1)) #minimum of the two values
'''

'''
Problem 4 - https://www.codechef.com/MPF12AP001/problems/DPOLY
Solved:09/02/2022
'''

'''
#start code

numba_o_ele=int(input()) #number of elements/inputs

for i in range(numba_o_ele):
    ele=int(input()) #the actual inputs
    store=list(map(int,input().split())) #storing in a list for later
    check=0
    
    for j in range(ele): #checking if element is zero
        
        if store[ele-j-1]==0: #if zero increment the input
            check+=1
        else:
            break #if not zero break out of the loop
       
    print(ele-check-1) #difference between the length of the list and the count variable
'''

'''
Problem 5 - https://www.codechef.com/MPF12AP001/problems/CHN15A
Solved:09/02/2022
'''

'''
#start code

T=int(input()) #number of testcases

for i in range(0,T):
    (N,K)=input().split() #required integers, N for minions and K for transmogrifier
    
    intrinsic_val=input().split() 
    
    list=[]
    
    for m in intrinsic_val:
        list.append((int(m))+int(K)) #putting the intrinsic values in a list
        
    num_of_wolverine_esque_gru=0
    
    for j in list: #checking if it is divisible by 7
        if j%7==0: 
            num_of_wolverine_esque_gru=num_of_wolverine_esque_gru+1
    print(num_of_wolverine_esque_gru)
'''