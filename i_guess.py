import random

print("Devinez le nombre entre 1 et 100 ! (7 coups max)")

numberToGuess = random.randint(1,100)
number = 0
count = 7

while number != numberToGuess: 
    print(f"{count} coups restants")
    number = int(input("Entrez un nombre : "))
    count-=1
    
    if number < numberToGuess:
        print("C'est plus !")
    elif number > numberToGuess:
        print("C'est moins !")
    else :
        print(f"Bravo vous avez trouvé le nombre à deviner, il s'agissait bien de {numberToGuess} ! (en {7-count} coups.)")
        print("\n")
        break
    
    if count == 0 :
        print("Perdu !")
        print("\n")
        break
   
    print("\n")

print("Fin du jeu")