import random

print("Welcome to the game.")
playing = input("Do you want to play? (yes or no) ").lower()
if playing != "yes" :
    print("Bye! Let's play some other time.")
    quit()
print("Okay! Let's the game begins!"
      "\nThis is a guessing game."
      "\nYou are to choose a any number LARGER than 10 to be set as the upper limit."
      "\nThen, make a guess between 0 and the number you chose prior."
      "\nYou are to be given only 5 chances.")

user = input("Set the upper limit: ")
if user.isdigit():
    user = int(user)

    if user < 20:
        print("Please choose a number larger than 20 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

number = random.randint(0,user)
turn = 0
while True:
    turn += 1

    if turn > 5:
        print("\nOh noooo! It's over!"
              "\nYou did not guess it within 5 guesses."
              "\nBetter luck next time.")
        break
    else:
        print("Turn", turn)
        guess = input("Make a guess: ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please insert a number.")
            turn -= 1
            continue

        if guess == number:
            print("You got it!")
            print("You got it in", turn, "guesses.")
            break
        elif guess > user:
            print("Please guess a number between 0 and",user,".")
        elif guess > number:
            print("Your guess is above the number.")
        else:
            print("Your guess is below the number.")



