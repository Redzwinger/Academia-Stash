'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 03
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 03")

print("\n ############# ################ ####################\n")

def knapsack_max_profit(profit_weight_ratios, profits, weights, max_weight):
    total_profit = 0

    while max_weight > 0 and profit_weight_ratios:
        max_ratio_index = profit_weight_ratios.index(max(profit_weight_ratios))
        max_weight_item = weights[max_ratio_index]
        max_profit_item = profits[max_ratio_index]

        if max_weight_item <= max_weight:
            total_profit += max_profit_item
            max_weight -= max_weight_item

        else:
            fraction = max_weight / max_weight_item
            total_profit += max_profit_item * fraction
            max_weight = 0

        print(f" Profit: {max_profit_item}")
        print(f" Weight: {max_weight_item}")
        print(f" Profit-to-Weight Ratio: {profit_weight_ratios[max_ratio_index]}")
        print(" ----------------------")

        profit_weight_ratios.pop(max_ratio_index)
        profits.pop(max_ratio_index)
        weights.pop(max_ratio_index)

    print(f" Final Profit: {total_profit}", end="\n\n")

max_weight_capacity = 60
profits = [280, 100, 120, 120]
weights = [40, 10, 20, 24]

profit_weight_ratios = [round(profits[i] / weights[i], 2) for i in range(len(weights))]

knapsack_max_profit(profit_weight_ratios, profits, weights, max_weight_capacity)

# Charmingly Crafted By Redzwinger #

