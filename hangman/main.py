import random
from func import *
print("\nLe jeu du pendu !\n")


with open("words.txt","r") as file:
    words_file = file.read().splitlines()
target = random.choice(words_file).upper()
attempts = 11
bool_tab = []
used_letters = []
fill_bool_tab(bool_tab,target)
print_result(bool_tab,target)
print("\n")

while not word_found(bool_tab):
    if (attempts == 0):
        print(f"\nPerdu ! Le mot était : {target}")
        break

    print(f"=> Encore {attempts} tentatives")

    print("Lettres utilisées :")
    for used_letter in used_letters :
        print(used_letter, end=", ")
    letter = (input("\n\nEntrez une lettre : ")).upper()
    used_letters.append(letter)

    if not (letter_found(letter,bool_tab,target)):
        attempts-=1
        draw_hangman(attempts)
    print("\n")
    print_result(bool_tab,target)
    print("\n------------------------------------------------------------\n")
    
    if word_found(bool_tab):
        print("\n\nBravo !! Vous avez trouvé le mot")
        break
    print("\n")

print("\nFin du jeu.")