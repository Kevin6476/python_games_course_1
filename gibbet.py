def to_play():
    print("#############################")
    print("Welcome to the hangman game!")
    print("#############################")

    got_the_word_right = False
    went_to_the_gallows = False
    secret_word = "banana".upper()
    letters_unraveled = ["_", "_", "_", "_", "_", "_"]
    total_errors = 3
    errors = 0

    while not got_the_word_right and not went_to_the_gallows:
        print("\n\n", letters_unraveled, sep="")
        print("{} attempts left.".format(total_errors - errors))

        letter_kicked = input("Enter a letter: ").strip().upper()
        if letter_kicked in secret_word:
            index = 0
            for letter in secret_word:
                if letter.lower() == letter_kicked.lower():
                    letters_unraveled[index] = letter
                index += 1
        else:
            errors += 1
            print("You got the letter wrong ...", end="")

        went_to_the_gallows = errors == total_errors
        got_the_word_right = "_" not in letters_unraveled

    if went_to_the_gallows:
        print("Exhausted attempts :´(")
    elif got_the_word_right:
        print("Game finished! Congratulations on discovering the secret word: ")
        print(letters_unraveled)

    print("\n", "End of the game!", sep="")


if __name__ == "__main__":
    to_play()
