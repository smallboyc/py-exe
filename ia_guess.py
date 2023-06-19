import random

print("\nFaites deviner un nombre entre 1 et 100 à l'ordinateur !")
print("Indication à la machine : '+' / '-' / '='\n")

numberToGuess = int(input("Choisissez un nombre à faire deviner à l'oridnateur : "))
number = 0
min = 1
max = 100


while (number != numberToGuess):
    number = random.randint(min,max)
    print(f"Nombre choisis : {number}\n")
    choice = ''
    while not choice in ('+','-','='):
        choice = input("Indication : ")
        if (choice == '+'):
            min = number
        elif (choice == '-'):
            max = number
        elif (choice == '=') :
            print(f"\nL'ordinateur a trouvé le nombre !")
            break
        
print("Fin du jeu")
    