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

def IP_Network(givenIP):
    RawStuf = givenIP.split('.') # Decimal Separated IP
    
    A = [int(RawStuf[0])]
    B = [int(RawStuf[1])]
    C = [int(RawStuf[2])]
    D = [int(RawStuf[3])]
    
    binA, binB = ("{:08b}".format(int(A[0]))), ("{:08b}".format(int(B[0])))
    binC, binD = ("{:08b}".format(int(C[0]))), ("{:08b}".format(int(D[0])))
    
    print("\n Binary Conversion: ", binA, binB, binC, binD)
    
    NetClass = classy(A[0])
    subnet_mask = subby(NetClass)
    hosty(givenIP, subnet_mask)

def classy(firs_oct):
    if (firs_oct == 0):
        print("\n Invalid IP")

    elif (0<firs_oct<127):
        print("\n Network Class: A")
        return 'A'
    
    elif (127<firs_oct<191):
        print("\n Network Class: B")
        return 'B'
    
    elif (191<firs_oct<223):
        print("\n Network Class: C")
        return 'C'
    
    elif (223<firs_oct<239):
        print("\n Network Class: D (Multicast)")
        return 'D'
    
    elif (239<firs_oct):
        print("\n Network Class: E (Experimental)")
        return 'E'
        
def subby(NetClass):
    if NetClass == 'A':
        print("\n Subnet Mask: 255.0.0.0")
        return '255.0.0.0'
    
    elif NetClass == 'B':
        print("\n Subnet Mask: 255.255.0.0")
        return '255.255.0.0'
    
    elif NetClass == 'C':
        print("\n Subnet Mask: 255.255.255.0")
        return '255.255.255.0'
    
    else:
        print("\n Subnet Mask: N/A")
        return 'N/A'

def hosty(given_ip, subnet_mask):
    if subnet_mask == 'N/A':
        print("\n Usable Host IP Range: N/A \n")
        
    else:    
        subnet_octets = subnet_mask.split('.')
        given_octets = given_ip.split('.')
    
        start_range = []
        end_range = []
    
        for i in range(4):
            if subnet_octets[i] == '255':
                start_range.append(given_octets[i])
                end_range.append(given_octets[i])
            else:
                break
            
        if len(start_range) == 1:
            start_range.append('0')
            start_range.append('0')
            start_range.append('1')
            end_range.append('255')
            end_range.append('255')
            end_range.append('254')
                
        if len(start_range) == 2:
            start_range.append('0')
            start_range.append('1')
            end_range.append('255')
            end_range.append('254')
                
        if len(start_range) == 3:
            start_range.append('1')
            end_range.append('254')
    
        start_ip = ".".join(start_range)
        end_ip = ".".join(end_range)
    
        print('\n Usable Host IP Range: ' f'{start_ip} - {end_ip}', end="\n\n")
        
gib_the_IP = str(input(" Enter an IP adresss: "))
IP_Network(gib_the_IP)

# Comprehensively Crafted By Redzwinger #

