print("Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
print("You have 10 attempts to guess the number")
print("After each guess, I'll tell you if your guess is too high, too low or correct")
print("Let's begin!")
num = int(input("Enter your guess (1-100):"))
if(num < 1 or num > 100 ):
    print("Please enter a number between 1 and 100.")
else:
    import random
    secret_number = random.randint(1, 100)
    attempts = 1
    while attempts <= 10:
        if num < secret_number:
            print("Your guess is too low.")
        elif num > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        if attempts == 10:
            print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
            break
        num = int(input("Enter your guess (1-100):"))
        if(num < 1 or num > 100 ):
            print("Please enter a number between 1 and 100.")
            continue
        attempts += 1
