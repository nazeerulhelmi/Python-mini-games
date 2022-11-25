print("Welcome to a computer quiz")
playing = input("Do you want to play? ").lower()
if playing != "yes" :
    print("Bye! Let's play some other time")
    quit()
print("Okay! Let's the game begins!"
      "\nThis is a quiz game."
      "\nThe question is an acronym of a computer parts and you are expected to define the acronym."
      "\nBe specific and precise.")
score = 0
question = 0
answer = input("1. What does CPU stand for? ").lower()
question += 1
if answer == "central processing unit":
    print("That is correct!")
    score += 1
else:
    print("Oops, wrong answer. The answer is Central Processing Unit.")

answer = input("2. What does GPU stand for? ").lower()
question += 1
if answer == "graphic processing unit":
    print("That is correct!")
    score += 1
else:
    print("Oops, wrong answer. The answer is Graphic Processing Unit.")

answer = input("3. What does RAM stand for? ").lower()
question += 1
if answer == "random access memory":
    print("That is correct!")
    score += 1
else:
    print("Oops, wrong answer. The answer is Random Access Memory.")

answer = input("4. What does PSU stand for? ").lower()
question += 1
if answer == "power supply unit":
    print("That is correct!")
    score += 1
else:
    print("Oops, wrong answer. The answer is Power Supply Unit.")

answer = input("5. What does SSD stand for? ").lower()
question += 1
if answer == "solid state drive":
    print("That is correct!")
    score += 1
else:
    print("Oops, wrong answer. The answer is Solid State Drive")

print("\nThat is the end of the quiz."
      "\ncounting score..."
      "\ncounting score..."
      "\ncounting score..."
      "\nYou got the score of", score, "out of", question, "questions.")
if score == 5:
    print("That is AWESOME. You answered all correctly!")
elif score >= 3:
    print("You fall short. Nice effort")
elif score >= 1:
    print("Hard luck! Brush up your computer knowledge!")
else:
    print("SERIOUSLY?! SHAME ON YOU!"
          "\nWell, keeps improving okay.")
print("Hope you have fun while playing."
      "\nSee you again. :)")