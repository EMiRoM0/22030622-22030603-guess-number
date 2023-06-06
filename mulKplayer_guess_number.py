#gonzalez leos america xochitl utm22030603
#romo calvillo cristobal emilio utm22030622

from getpass import getpass

TRIES = 90

print("This is a two player game, the first player must enter the range of numbers and the second player must try to guess a random number.")

secretNumber = getpass("Enter the secret number: ")
secretNumber = int(secretNumber)
enteredNumber = int(input("Guess the number: "))

while secretNumber != enteredNumber:
    if TRIES > 0:
        if secretNumber > enteredNumber:
            print("Very low")
        else:
            print("Very high")
        print("You have", TRIES, "points left.")
        enteredNumber = int(input("Enter another guess: "))
        TRIES -= 10
    else:
        print("The number was:", secretNumber)
        break

if secretNumber == enteredNumber:
    print("Exactly! Just spend", 100 - TRIES, "of your 100 points")
else:
    print("You didn't get it right, try again. ")
