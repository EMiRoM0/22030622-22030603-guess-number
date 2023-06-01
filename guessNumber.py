#gonzalez leos america xochitl utm22030603
#romo calvillo cristobal emilio utm22030622
#This version of the game is for one person, with a fixed range of 1 to 100, with only 10 chances.
#This library guarantees us to get a random number that is in the fixed range.
from random import randint
TRIES = 9 #This is the number of chances that do you have.
secretNumber = randint(1, 100) #This is the range of numbers that we have.
enteredNumber = int(input("Guess the number 1 to 100: "))
while secretNumber != enteredNumber: #If you put the wrong number that is missing in the range, you'll lost chances.
    if TRIES > 0:
        if secretNumber > enteredNumber: #If our number is to low, this will appear like an advice.
            print("Very low")
        else:
            print("Very high") #Or if our number is too high this will appear to analyze and think in more numbers.
        print("You have", TRIES, "tries left.") #While you still trying to introduce numbers, there will be a counter of tries that do you have.
        enteredNumber = int(input("Enter another guess: "))
        TRIES -= 1
    else:
        print("The number was:", secretNumber) #If you fail all the chances, the game will show you the random number.
        break
if TRIES >= 0:
    print("Exactly! You guessed in", 9 - TRIES, "tries.") #If you have entered the correct number, this message will appear and the number of tries.
