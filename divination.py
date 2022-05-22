import random

print("#############################")
print("Welcome to the Guessing game!")
print("#############################")

win = False
difficulty = 0
total_attempts = 0
while difficulty < 1 or difficulty > 3:
    print("\nChoose the difficulty in the game:")
    difficulty = int(input("(1) Easy (2) Medium (3) Hard "))

if difficulty == 1:
    total_attempts = 15
elif difficulty == 2:
    total_attempts = 10
else:
    total_attempts = 5

secret_num = random.randrange(1, 101)
for attempt in range(1, total_attempts + 1):
    print("\n\nAttempt {} of {}".format(attempt, total_attempts))

    shot = int(input("Enter an integer between 1 and 100: "))

    if shot < 1 or shot > 100:
        print("You must enter a number between 1 and 100! This round was lost.")
        continue

    kick_was_bigger = shot > secret_num
    kick_was_smaller = shot < secret_num

    if kick_was_bigger:
        print("You missed! Your kick was bigger than the secret number")
    elif kick_was_smaller:
        print("You missed! Your guess was less than the secret number")
    else:
        print("You're right!")
        win = True
        break

if not win:
    print("\nThe secret number was {}".format(secret_num), end="\n\n")
print("End of the game!")
