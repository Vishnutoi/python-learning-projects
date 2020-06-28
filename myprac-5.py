#Number guessing game
#Generate number from 0-100 and ask the user to guess the number
#Many bonus points if you can create a points system!

import random


guess = int(input("enter number between 0 to 4: "))
number = random.randrange(0,4)

count = 0
while guess != number:
    #print("number = %s" %(number))
    print("no you entered wrong number")
    guess = int(input("enter number :"))
    count = count + 1


print("you got it in %s time" %(count))
print("you got it right")