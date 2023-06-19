
def fill_bool_tab(tab, target):
    # i=0
    # while i != len(target):
    #     if target[i] == '-':
    #         tab.append(1)
    #     else:
    #         tab.append(0)
    #     i+=1
    
    for el in target:
        if el == '-':
            tab.append(1)
        else:
            tab.append(0)

def letter_found(letter, tab, target):
    i = 0
    find = False
    for el in target :
        if letter == el:
            tab[i] = 1
            find = True
        i+=1
    return find

def print_result(tab,target):
    i=0
    for el in tab:
        if el == 1:
            print(target[i], end=" ")
        else:
            print("*",  end=" ")
        i+=1

def word_found(tab):
    for el in tab:
        if el != 1:
            return False
    return True


def draw_hangman(attempts):
    with open(f"draw/part_{11-attempts}.txt","r") as file:
        draw_file = file.read()
    print(draw_file)
    print('\n')