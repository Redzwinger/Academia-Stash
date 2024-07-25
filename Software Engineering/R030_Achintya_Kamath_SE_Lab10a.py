'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Software Engineering
Lab 10-a
Date: 12/03/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Software Engineering \n Lab 10-a \n Date: 12/03/2024")

print("\n ############# ################ ####################\n")

class Driver(object):
    '''
        This is the main class.
        Eligibility criteria is calculated within
        this same routine.
    '''
    def __init__(self, n, a, p, s):
        self.name = str(n)
        self.age = int(a)
        self.points = int(p)
        self.seasons = int(s)
        self.critsVal = self.stats()
        self.eligible = self.isEligible(self.critsVal)

    def stats(self):
        '''
            This function caluclates the
            criteria points for each
            eligibility met by the driver.
        '''
        crit = int(0) # Number of Criteria Met
        # Primary Condition #
        if (self.age >= 18) and (self.age <= 50):
            # Age Range : [18 -> 50] #
            crit += 5
        # Secondary Criteria #
        if (self.points >= 40) and (self.seasons >= 3):
            crit += 10
        elif (self.points >= 40) or (self.seasons >= 3):
            crit += 7
        return crit

    def isEligible(self, cVal):
        '''
            This function will be responsible for taking
            in the criteria points met,
            and assign the status to it.
        '''
        status = str("NULL") # Defaults to NULL
        if cVal <= 5:
            status = "NOT ELIGIBLE"
        elif cVal < 14:
            status = "SENT TO REVIEW"
        elif cVal == 15:
            status = "ELIGIBLE"
        else:
            status = "NULL"
        return status
'''
# Testing Arena #
n1, a1, p1, s1 = str("Lewis Hamilton"), int(38), int(754), int(14)
d1 = Driver(n1, a1, p1, s1)

n2, a2, p2, s2 = str("Mick Schumacher"), int(27), int(221), int(5)
d2 = Driver(n2, a2, p2, s2)

n3, a3, p3, s3 = str("Achintya Kamath"), int(21), int(0), int(0)
d3 = Driver(n3, a3, p3, s3)

n4, a4, p4, s4 = str("James Bond"), int(42), int(2), int(6)
d4 = Driver(n4, a4, p4, s4)
'''

# To Check if they are eligible? #
'''
print(f"Status of {d1.name} is {d1.eligible}")
print(f"Status of {d2.name} is {d2.eligible}")
print(f"Status of {d3.name} is {d3.eligible}")
print(f"Status of {d4.name} is {d4.eligible}")
'''

# Custom Input #
intro = str("""
This program is made to check for
Super Licence Eligibility.
Please enter the Driver Details below!
""")
eName = str(input("Enter the name of the Driver : ") or "HUMAN")
eAge = int(input("Enter the age of the Driver : ") or 0)
ePoints = int(input("Enter the points earned by Driver : ") or 0)
eSeasons = int(input("Enter seasons attended by the Driver : ") or 1)

# Processing #
dNew = Driver(eName, eAge, ePoints, eSeasons)
print(f"\nThe Licence Status of {dNew.name} is {dNew.eligible}")


