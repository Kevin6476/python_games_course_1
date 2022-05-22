print("#############################")
print("Welcome to the Guessing game!")
print("#############################")

secret_num = 42

shot = int(input("Enter your number: "))
print("You typed ", shot)

hit_kick = shot == secret_num
kick_was_bigger = shot > secret_num
kick_was_smaller = shot < secret_num

if hit_kick:
    print("You're right!")
elif kick_was_bigger:
    print("You missed! Your kick was bigger than the secret number")
elif kick_was_smaller:
    print("You missed! Your guess was less than the secret number")

print("End of the game!")
