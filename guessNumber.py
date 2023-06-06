#gonzalez leos america xochitl utm22030603
#romo calvillo cristobal emilio utm22030622
#This version of the game is for one person, with a fixed range of 1 to 100, wi>
#This library guarantees us to get a random number that is in the fixed range.
from random import randint
TRIES = 9 #This is the number of chances that do you have.
secretNumber = randint(1, 100) #This is the range of numbers that we have.
enteredNumber = int(input("Guess the number 1 to 100: "))
while secretNumber != enteredNumber: #If you put the wrong number that is missi>
    if TRIES > 0:
        if secretNumber > enteredNumber: #If our number is to low, this will ap>
            print("Very low")
        else:
            print("Very high") #Or if our number is too high this will appear t>
        print("You have", TRIES, "tries left.") #While you still trying to intr>
        enteredNumber = int(input("Enter another guess: "))
        TRIES -= 1
    else:
        print("The number was:", secretNumber) #If you fail all the chances, th>
        break
