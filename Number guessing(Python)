import random

Tries=0

while True:
    Number=random.randint(0,100)
    opt=int(input("Enter an appropriate option:\n1)Take a guess.\n2)Exit.\n"))
    if opt==2:
        print("Thank you.\n")
        break
    elif opt==1:
        Done=False
        while not Done:
            guess=int(input("Enter a whole number between 0 and 100.\n"))
            Tries+=1
            if guess==Number:
                print("WOW! you guessed perfectly!.\n")
                print("You took ",Tries," tries.\n")
                Done=True
            elif guess<Number:
                print("Your guess is lower than expected number.\n")
            else:
                print("Your guess is higher than expected number.\n")
    else:
        print("Invalid input.\n")
