import random

print("\n ############# ################ #################### ################ #############\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B2 \n Date: 07/10/2022 \n Experiment 9\n")

print("\n\t \t\t------------------------------------------------")

print("\t \t \tThis program solves the 'Monkey Banana' Problem.", end=" ")

print("\n\t \t \t------------------------------------------------")

print(" (Note: The Start location \n and the subsequent positions \n of all possible movable objects \n are randomized)")

start_poss = ["Door", "Window", "Table", "Under The Bananas"]
table_poss = ["Under The Bananas", "Not Under The Bananas"]

check=bool(False)

Mr_Monke = random.choice(start_poss)
start_table = random.choice(table_poss)

def Table(Mr_Monke, path, check, start_table):
    if start_table == "Under The Bananas":
            Mr_Monke == "Table"
            path.append("Table")
            print("\n\t The Monkey moves towards the Table...")
            print("\t ...and sees the bananas hanging above the table prompting the monkey to climb on top of the table.")
            print("\n\t After climbing on the table and seeing that there is nothing stopping it from taking them, the monkey happily takes the bananas.")
            check = bool(True)
    elif start_table == "Not Under The Bananas":
            Mr_Monke == "Table"
            path.append("Table")
            print("\n\t The Monkey moves towards the Table...")
            print("\t ...and sees the bananas hanging above the table prompting the monkey to climb on top of the table.")
            print("\n\t After climbing on the table and seeing that there is nothing stopping it from taking them, the monkey happily takes the bananas.")
            check = bool(True)

while check == False:
    path = []
    count_of_path = len(path)

    if Mr_Monke == "Table":
        print("\n\t The Monkey, luckily, finds itself near The Table.")
        Table(Mr_Monke, path, check, start_table)
        break

    elif Mr_Monke == "Door":
        path.append("The Door")
        print("\n\t The Monkey finds itself near The Door.")
        Table(Mr_Monke, path, check, start_table)
        break

    elif Mr_Monke == "Window":
        path.append("Window")
        print("\n\t The Monkey finds itself near The Window.")
        Table(Mr_Monke, path, check, start_table)
        break
            
    elif Mr_Monke == "Under The Bananas":
        path.append("Under The Bananas")
        print("\n\t The Monkey, by some strangely fantastic stroke of luck, finds itself under the bananas, already on top the table.")
        print("\n\t Seeing that there is nothing between itself and the bananas, the monkey simply reaches up and victoriously takes the bananas")
        check = bool(True)
        break

print("\n\t The path the monkey took to reach the bananas is: ", path)
print("\n\t And so, the monkey successfully gets the bananas :)", end="\n\n")
