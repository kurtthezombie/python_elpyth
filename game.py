from os import system
from random import randint

p1:int = 0
p2:int = 0


def inputhand():
    choices = """
    1 Rock
    2 Scissors
    3 Paper
    Your hand(1..3): 
    """
    while True:
        try:
            hand = int(input(choices))
            if (1<=hand<=3):
                break
        except:
            print("Invalid Input!")
            continue
        print("Invalid Input!")
    return hand

def judging(n):
    global p1, p2
    bothand = randint(1,3)
    if n == 1:
        if bothand == 2:
            print("Rock breaks scissors. You WIN!")
            p1 += 1
        elif bothand == 3:
            print("Paper covers rock. You LOSE!")
            p2 +=1
        else:
            print("Rock vs Rock? Tie!")
    elif n == 2:
        if bothand == 3:
            print("Scissors cuts paper. You WIN!")
            p1 += 1 
        elif bothand == 1:
            print("Rock breaks scissors. You LOSE!")
            p2 += 1
        else:
            print("Kinda lesbian but... Tie!")
    else:
        if bothand == 1:
            print("Paper covers rock. You WIN!")
            p1 += 1
        elif bothand == 2:
            print("Scissors cuts paper. You LOSE!")
            p2 += 1
        else:
            print("Y'all schooling? Tie!")
    input("Press any key to continue...")
    

def main():
    system("cls")
    print("Rock, scissors, paper!")
    
    while True:
        judging(inputhand())
        print(p1,p2)
        if p1 == 3:
            print("You win! Congrats!")
            break
        elif p2 == 3:
            print("You lost! Try again next time!")
            break
        else:
            continue
            




if __name__ == "__main__":
    main()