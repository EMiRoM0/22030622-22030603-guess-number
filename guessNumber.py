#gonzalez leos america xochitl utm22030603
#romo calvillo cristobal emilio utm22030622

from random import randint #Library to be able to use a random number 

TRIES = 90  #Variable to add points to the game 

print("Guess the random number by entering the range ")   
print("\n")
print("Enter game range:")              #Enter the variables for the range 
minimum = int(input("Minimum: "))
maximum = int(input("Maximum: "))
print("\n")
secretNumber = randint(minimum, maximum)    #a number is chosen when roasting
enteredNumber = int(input("Guess the number: "))    #enter a number

while secretNumber != enteredNumber:   
    if TRIES > 0:
        if secretNumber > enteredNumber:
            print("Very low")      #very low 
        else:
            print("Very high")              # you go very high
        print("You have", TRIES, "points left.")
        print("\n")
        enteredNumber = int(input("Enter another guess: "))
        TRIES -= 10
    else:
        print("\n")
        print("The number was:", secretNumber)    #reveals the secret number 
        break

if secretNumber == enteredNumber:     #end of the game
    print("\n")
    print("Exactly! Just spend", 100 - TRIES, "of your 100 points")   #if you got it right 
else:
    print("\n")
    print("You didn't get it right, try again. ")  #if you didn't get it right 

