def to_play():
    print("#############################")
    print("Welcome to the hangman game!")
    print("#############################")

    got_it_right = False
    gibbet = False
    secret_word = "banana"
    letters_unraveled = ["_", "_", "_", "_", "_", "_"]

    while not got_it_right and not gibbet:
        print(letters_unraveled)
        shot = input("Enter a letter: ").strip()
        index = 0
        for letter in secret_word:
            if letter.lower() == shot.lower():
                letters_unraveled[index] = letter
            index += 1

    print("End of the game!")

if __name__ == "__main__":
    to_play()
