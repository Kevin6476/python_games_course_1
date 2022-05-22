import gibbet
import divination

print("#############################")
print("Choose your game!")
print("#############################")

print("(1) Hangman (2) Guessing")
choice = int(input("Choice: "))

if choice == 1:
    gibbet.to_play()
elif choice == 2:
    divination.to_play()
else:
    print("There is no game for this choice")