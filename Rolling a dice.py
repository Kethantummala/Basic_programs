import random

while True:
    opt=int(input("Enter the option to perform the action:\n1)Roll the dice!\n2)Exit\n"))
    if opt==2:
        print("\nThank you.")
        break
    elif opt==1:
        print("\nDice rolled,Result:\t",random.randint(1,6),"\n")
    else:
        print("\nInvalid option selection.")

input()
