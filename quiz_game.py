print("Welcome to my Formula One quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, lets play! :)")
score = 0

answer = input("What driver number is Max Verstappen? ")
if answer.lower() == "33":
    print('Correct! Well done!')
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("What colour are soft tyres? ")
if answer.lower() == "red":
    print('Correct! Well done!')
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("Who won the 2019 World Championship? ")
if answer.lower() == "lewis hamilton":
    print('Correct! Well done!')
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("A red flag means the race is stopped. True or false? ")
if answer.lower() == "true":
    print('Correct! Well done!')
    score += 1
else:
    print("Sorry, wrong answer")

answer = input("Who does Lando Norris drive for? ")
if answer.lower() == "mclaren":
    print('Correct! Well done!')
    score += 1
else:
    print("Sorry, wrong answer")

print("You got " + str(score) + " questions correct")
print(str((score / 5) * 100) + "%")
