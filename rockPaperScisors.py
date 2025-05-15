import random

randomizer = random.randint(0,2)

# IN THE ARRAY
# 0 = Rock
# 1 = Paper
# 2 = Scissors
# Example 1, [0][1]
# Rock vs paper = Loose
# Example 2, [0][0]
# Rock vs Rock = Draw
# Example 3, [0][2]
# Rock vs Scissors = Win

winning = [['D','L','W'],['W','D','L'],['L','W','D']]

print("=================================================")
print("\nWelcome to the Rock, Paper, Scisor game\n\n")
choise = int(input('Choose one (Type 0 for Rock, 1 for Paper OR 2 for Scissors)'))

match winning[choise][randomizer]:
        case "W":
            print("=============================================================")
            print('\nYou win\n')
        case "D":
            print("=============================================================")
            print("\nIt is a Draw\n")
        case "L":
            print("=============================================================")
            print('\nYou loose\n')
        case _:
            print("=============================================================")
            print("ERROR in the input.")