print("#############################")
print("Welcome to the Guessing game!")
print("#############################")

secret_num = 42
total_attempts = 3

for attempt in range(1, total_attempts + 1):
    print(f"\n\nAttempt {attempt} of {total_attempts}")

    shot = int(input("Enter your number: "))
    print("Your kick was", shot)

    kick_was_bigger = shot > secret_num
    kick_was_smaller = shot < secret_num

    if kick_was_bigger:
        print("You missed! Your kick was bigger than the secret number")
    elif kick_was_smaller:
        print("You missed! Your guess was less than the secret number")
    else:
        print("You're right!")
        break

print("End of the game!")
