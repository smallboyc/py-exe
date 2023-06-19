import random

print("\nJeu du pierre-feuille-ciseaux !\n")

#p > c / p < f
#f > p / f < c
#c > f / c < p

choice = ("p","f","c")
target = 3
human_score = 0
computer_score = 0

while human_score != target and computer_score != target:
    human = ''
    computer = random.choice(choice)
    while not human in choice:
        human = input("Choisissez entre 'p' / 'f' / 'c' : ")

    print(f"L'ordinateur a choisi : {computer}")

    if (human == 'p' and computer == 'c') or (human == 'f' and computer == 'p') or (human == 'c' and computer == 'f') :
        print("Vous avez gagné la manche !\n")
        human_score+=1
    elif (human == 'p' and computer == 'f') or (human == 'f' and computer == 'c') or (human == 'c' and computer == 'p') :
        print("Vous avez perdu la manche !\n")
        computer_score+=1
    else :
        print("Egalité !\n")

    print(f"Score / {human_score} : {computer_score}")

if (human_score == target):
        print("\nVictoire !!! ")
elif (computer_score == target):
        print("\nDéfaite !")
    



