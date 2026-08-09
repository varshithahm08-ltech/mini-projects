import random

number = random.randint(1, 20)

print("🎮 Number Guessing Game")
print("Guess a number between 1 and 20")
print("You have 3 attempts.")

for attempt in range(3):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations! You won!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("😢 Game over!")
    print("The correct number was:", number)