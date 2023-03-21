print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

anwser = input("What does CPU stand for? ")
if anwser.lower() == "central processing unit":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect! ")


anwser = input("What does GPU stand for? ")
if anwser.lower() == "graphics processing unit":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect! ")


anwser = input("What does RAM stand for? ")
if anwser.lower() == "random access memory":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect! ")


anwser = input("What does AWS stand for? ")
if anwser.lower() == "amazon web services":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect! ")


anwser = input("What does API refer to? ")
if anwser.lower() == "application programming interface":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect! ")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) *100) + "%.")