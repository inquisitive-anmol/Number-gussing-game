# Number gussing game
import random as r 
import math


lower = int(input("Set the lower limit :"))


upper = int(input("Set the upper limit :"))

# Generating random number between
# upper and lower limit
x = r.randint(lower, upper)

print("\n\tYou've only", round(math.log(upper - lower + 1 , 2))," chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum no. of guesses 
# depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    try:

        guess = int(input("Guess a number! : "))
    except:
        print("Please enter a guessed integer")


    # Testing conditions

    if guess == x:
        print("Congratulations!! , You guessed it in", count, "try")

        # Once guessed , the loop will break
        break

    elif guess > x:
        print("You guessed too high!")

    elif guess < x:
        print("You guessed too small!")


#  If the guesses are more than limit
if count > math.log(upper - lower + 1, 2):
    print("\n The number is " ,x)
    print("\t Better luck Next Time!!")
