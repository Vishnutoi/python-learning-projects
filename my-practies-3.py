import random


user_input = input("Please enter HEADS or TAILS :")


ran = random.randint(0,1)

print(ran)
if ran == 0 and user_input == "tails":
    print("tails is the outcome and you WON")
elif ran == 0 and user_input == "heads":
    print("tails is teh outcome and your LOST")
elif ran == 1 and user_input == "tails":
    print("Heads is teh outcome and you LOST")
else:
    print("heads is the outcome and you WON")


