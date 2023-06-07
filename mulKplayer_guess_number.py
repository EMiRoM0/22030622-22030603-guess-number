#gonzalez leos america xochitl utm22030603
#romo calvillo cristobal emilio utm22030622

from getpass import getpass  #Library to be able to enter a number and not have it visible 

TRIES = 90 #Variable to add points to the game

print("This is a two player game, the first player must enter the range of numbers and the second player must try to guess a random number.")
print("\n")
secretNumber = getpass("Enter the secret number: ")    #enter the secret number 
secretNumber = int(secretNumber)
print("\n")
enteredNumber = int(input("Guess the number: ")) #enter a number

while secretNumber != enteredNumber:
    if TRIES > 0:
        if secretNumber > enteredNumber:
            print("Very low")    #very low 
        else:
            print("Very high")      # you go very high
        print("You have", TRIES, "points left.")
        print("\n")
        enteredNumber = int(input("Enter another guess: "))
        TRIES -= 10
    else:
        print("\n")
        print("The number was:", secretNumber)             #reveals the secret number
        break

if secretNumber == enteredNumber:             #end of the game
    print("\n")
    print("Exactly! Just spend", 100 - TRIES, "of your 100 points")     #if you got it right 
else:
    print("\n")
    print("You didn't get it right, try again. ")       #if you didn't get it right
