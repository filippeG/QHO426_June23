import random #Taking definitions from a package "random" into my scope

secret_n = random.randint(0,20)
print("Welcome to my Guess Game! i AM THINKING OF A NUMBER BETWEEN 1 AND 20 ")

for attempts in range (1,6):
    print(f"Attempt nr {attempts}")
    guess = int(input("Take a guess"))
    if guess == secret_n:
        print("Congrats! You have guessed correctly!")
        break
    elif secret_n < guess:
        print("Too high!")
    else:
        print("Too low!")
if guess != secret_n:
    print(f"Game over! Mynumber was {secret_n}")

