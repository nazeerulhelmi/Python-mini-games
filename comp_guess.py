import random

print("Welcome to the game.")
playing = input("Do you want to play? (yes or no) ").lower()
if playing != "yes" :
    print("Bye! Let's play some other time.")
    quit()
print("Okay! Let's the game begins!"
      "\nThis is a guessing game."
      "\nYou are to choose a number of desire."
      "\nNext, you set any number LARGER than what you chose before to be set as the upper limit."
      "\nThen, make I, computer, will guess between 0 and the number you set."
      "\nWe will see how many guesses will it take for me to correctly guess you chosen number.")

user = input("Choose a number: ")
if user.isdigit():
    user = int(user)

else:
    print("Please type a number next time.")
    quit()

high = input("Set the upper limit: ")
if high.isdigit():
    high = int(high)

    if high < user:
        print("Please choose a number larger than", user, "next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

turn = 0
low = 0
while True:
    guess = random.randint(low, high)
    turn += 1
    print("Turn", turn)

    if guess == user:
        print("I got it! Your number is " + str(guess) + ".")
        print("I got it in", turn, "guesses.")
        break
    elif guess > user:
        print("I think my guess,", guess, ", is higher than your chosen number.")
        high = guess - 1
    else:
        print("I think my guess,", guess, ", is lower than your chosen number.")
        low = guess + 1