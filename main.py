import random
import art

print(art.logo)

ran = random_number =random.randint(1, 100)

print(ran)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")



def get_difficulty():
    lives = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5

    return lives



def number_guess():
    current_lives = get_difficulty()

    guess =""

    while guess != random_number:
        print(f"You have {current_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            current_lives-=1
            print("Too High")


        else:
            current_lives -= 1
            print("Too Low")



    print(f"You got it! The answer was {guess} .")


number_guess()