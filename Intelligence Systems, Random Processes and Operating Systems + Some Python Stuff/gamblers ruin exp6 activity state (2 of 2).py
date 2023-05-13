import numpy as np
import random as rm

states = ["Sleep","Icecream","Run"]

transition_name = [ ["SS", "SR", "SI"], ["RS", "RR", "RI"], ["IS", "IR", "II"] ]

transition_matrix = [ [0.2,0.6,0.2], [0.1,0.6,0.3], [0.2,0.7,0.1] ]

def activity_forcast(days):
    activity_today = "Sleep"
    print("Start State: ", activity_today, end="\n")

    activity_list = [activity_today]
    i = 0
    prob = 1

    while i != days:
        if activity_today == "Sleep":
            change = np.random.choice(transition_name[0], replace = True, p = transition_matrix[0])
            if change == "SS":
                prob = prob * 0.2
                activity_list.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activity_today = "Run"
                activity_list.append("Run")
            else:
                prob = prob * 0.2
                activity_today = "Icecream"
                activity_list.append("Icecream")

        elif activity_today == "Run":
            change = np.random.choice(transition_name[1], replace = True, p = transition_matrix[1])
            if change == "RR":
                prob = prob * 0.5
                activity_list.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activity_today = "Sleep"
                activity_list.append("Sleep")
            else:
                prob = prob * 0.3
                activity_today = "Icecream"
                activity_list.append("Icecream")

        elif activity_today == "Icecream":
            change = np.random.choice(transition_name[2], replace = True, p = transition_matrix[2])
            if change == "II":
                prob = prob * 0.1
                activity_list.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activity_today = "Sleep"
                activity_list.append("Sleep")
            else:
                prob = prob * 0.7
                activity_today = "Run"
                activity_list.append("Run")
        i += 1

    print("Possible States:", str(activity_list))
    print("End State After ", str(days), " days: ", activity_today)
    print("Probability of the possible sequence of states: " + str(prob))

activity_forcast(4)  


