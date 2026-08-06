secret = 7

while True:
    guess = int(input("Enter number: "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try Again")