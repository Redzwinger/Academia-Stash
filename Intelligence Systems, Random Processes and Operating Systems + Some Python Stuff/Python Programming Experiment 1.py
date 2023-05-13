'''
Experiment 1
Part A: Develop a simple calculator using operators
Part B: Check Odd, Even and Prime numbers.
Part C: Logic Gates (AND, OR, NOT)
'''


def plus(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    print("\nThis file contains the following programs: ")
    print(" 1. A Simple Calculator.")
    print(" 2. A program to check Odd, Even and Prime numbers.")
    print(" 3. A program that implements some Logic Gates")

    choice = input("\n Please select one of the above (1/2/3): ")

    #Part A

    if choice == '1':
        while True:

            print(
                "\n  This is a simple calculator program that works for two number calculations."
            )
            print("\n\tPlease select an operation:")
            print("\t1.Add.")
            print("\t2.Subtract.")
            print("\t3.Multiply.")
            print("\t4.Divide.")
            print("\t5.Exit To Main Menu.")

            choice = input("\n\tPlease enter (1/2/3/4): ")

            if choice in ('1', '2', '3', '4'):
                a = float(input("\n\tPlease enter the first number: "))
                b = float(input("\tPlease enter the second number: "))

            if choice == '1':
                print("\n\t", a, " + ", b, " = ", plus(a, b))

            elif choice == '2':
                print("\n\t", a, " - ", b, " = ", subtract(a, b))

            elif choice == '3':
                print("\n\t", a, " * ", b, " = ", multiply(a, b))

            elif choice == '4':
                print("\n\t", a, " / ", b, " = ", divide(a, b))

            elif choice == '5':
                print("\n\tExiting simple calculator program...")
                break

            again = input("\n\tWanna do another calculation? (Y/N): ")

            if again == "y" or "Y":
                print(f" ")

            elif again == "n" or "N":
                print("\n\tThank you for using this program!\n")
                break
            else:
                print("\n\t*** Invalid Input! ***")

#Part B

    if choice == '2':
        while True:
            print(
                f"\n  Please Enter any Two numbers to check which one of them is greater: ",
                end="\n\n\t")
            number_1 = int(input("Number 1 = "))
            print(f" ", end="\n\t")
            number_2 = int(input("Number 2 = "))

            if number_1 == number_2:
                print(f"\n\tThe Numbers ", number_1, " and ", number_2,
                      " are equal")
                break

            elif number_1 > number_2:
                print(f"\n\t ", number_1, " is greater than ", number_2)
                break

            elif number_2 > number_1:
                print(f"\n\t ", number_2, " is greater than ", number_1)
                break

#Part C

    if choice == '3':

        print(
            "\n  This is a program that puts to use the Logic Gates AND, OR and NOT."
        )
        print(
            f"\n\tPlease select the Logic Gate that you would like to use first: "
        )
        print(f"\t1. AND")
        print(f"\t2. OR")
        print(f"\t3. NAND")
        print(
            f"\t(Note: The above mentioned Logic Gates are going to be used in the context of one light bulb with 2 switches.\n\tThere are two switches. \n\tBoth control one light bulb.\n\t"
        )

        choice_2 = input("\tYour Selection: ")

        if choice_2 == '1':

            print(f" ", end="\n\t")
            switch_1 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))
            print(f" ", end="\n\t")

            switch_2 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))

            if switch_1 == switch_2 == 1:
                print("\n\tThe Light Bulb Lit Up!")

            else:
                print(
                    f"\n\tThe given input does not satisfy the requirements of an AND Gate. Please Try Again."
                )

        if choice_2 == '2':

            print(f" ", end="\n\t")
            switch_1 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))
            print(f" ", end="\n\t")

            switch_2 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))

            if switch_1 == 1 or switch_2 == 1:
                print("\n\tThe Light Bulb Lit Up!")

            elif switch_1 == switch_2 == 0:
                print(
                    f"\n\tThe given input does not satisfy the requirements of an OR Gate. Please Try Again."
                )

        if choice_2 == '3':

            print(f" ", end="\n\t")
            switch_1 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))
            print(f" ", end="\n\t")

            switch_2 = int(
                input(
                    "Please enter the status of switch 1 ('1' for 'on' and '0' for 'off'): "
                ))

            if switch_1 == switch_2 == 1:
                print(
                    "\n\tThe Light Bulb Didn't Turn On... and thats perfect!")

            else:
                print(
                    f"\n\tThe Light Bulb Lit Up but, the given input does not satisfy the requirements of a NAND Gate. Please Try Again."
                )




