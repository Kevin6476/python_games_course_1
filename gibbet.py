import random

def to_play():
    display_game_name()

    secret_word = get_secret_word()
    letters_unraveled = ["_" for each_letter in secret_word]
    got_the_word_right = False
    went_to_the_gallows = False
    errors = 0

    while not got_the_word_right and not went_to_the_gallows:
        print("\n\n", letters_unraveled, sep="")
        letter_kicked = input("Enter a letter: ").strip().upper()
        if letter_kicked in secret_word:
            set_found_letter(secret_word, letter_kicked, letters_unraveled)
        else:
            errors += 1
            draw_gallows(errors)

        went_to_the_gallows = errors == 7
        got_the_word_right = "_" not in letters_unraveled

    if went_to_the_gallows:
        report_that_the_player_lost(secret_word)
    elif got_the_word_right:
        inform_that_the_player_won()

    print("\n", "End of the game!", sep="")


def display_game_name():
    print("#############################")
    print("Welcome to the hangman game!")
    print("#############################")


def get_secret_word():
    words = []
    with open("palavras.txt", encoding="UTF-8") as file:
        for line in file:
            words.append(line.strip())
    chosen_word = random.randrange(0, len(words))
    return words[chosen_word].upper()


def set_found_letter(word, letter, unraveled):
    idx = 0
    for current_letter in word:
        if current_letter.lower() == letter.lower():
            unraveled[idx] = letter
        idx += 1


def report_that_the_player_lost(secret_word):
    print("Gosh, you've been hanged!")
    print("the word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def inform_that_the_player_won():
    print("Congratulation, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_gallows(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    to_play()
