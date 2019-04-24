import random
count = 0
print("your name")
name= input()
print("chances:")
chance= input()
chance = int(chance)
number=  random.randint(1,200)
print("Guess the number between 1 to 20, name")

while count < chance:
    print("Take a guess:")
    guess= input()
    guess=int(guess)

    count =count+1

    if guess < number:
        print("low")
    if guess > number:
        print("high")
    if guess== number:
        break
if guess==number:
    print("you guessed the number in", count, "time")
if guess != number:
    print("wrong")
    

