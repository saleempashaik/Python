import random
dice = random.randint(1,6)
user_input = int(input("Guess a number between 1 and 6:\n"))
if dice==user_input:
    print("You guessed CORRECT. machine also picked  "+str(dice))
else:
    print("Sorry. Machine picked "+str(dice)+" and you picked " +str(user_input))
