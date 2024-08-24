import random
import math
# Taking inputs
lower = int(input("Enter the Lower bound:- "))
# Taking inputs
upper = int(input("Enter the Upper bound:- "))
# Generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
# Initializing the number of guess.
count = 0

# for calculation of minimum number of 
#guess depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number:- "))

    # condition testing 
    if x == guess:
        print("Congratulations you did it in ",
              count, "try")
        #once guessed, loop will break
        break
    elif x < guess:
        print("You guessed too small")
    elif x < guess:
        print("You Guessed too high")
    # guessing more than required guesses, 
    # shows this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next Time!")
