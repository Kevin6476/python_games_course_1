import random
import unicodedata


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
        if got_the_lyrics_right(secret_word, letter_kicked):
            set_found_letter(secret_word, letter_kicked, letters_unraveled)
        else:
            errors += 1
            draw_gallows(errors)

        went_to_the_gallows = errors == 7
        got_the_word_right = "_" not in letters_unraveled

    if went_to_the_gallows:
        report_that_the_player_lost(secret_word)
    elif got_the_word_right:
        inform_that_the_player_won(secret_word)


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
    word_unaccented = unaccented(word)
    for current_letter in word_unaccented:
        if current_letter.lower() == letter.lower():
            unraveled[idx] = word[idx]
        idx += 1


def unaccented(word):
    return ''.join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")


def got_the_lyrics_right(secret_word, letter):
    secret_word_unaccented = unaccented(secret_word)
    return letter in secret_word_unaccented


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


def inform_that_the_player_won(secret_word):
    print("Congratulation, you won!")
    print("the word was {}".format(secret_word))
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
