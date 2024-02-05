import random
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
random = random.randint(1,20)
continue1 = True
counter = 0
while(continue1):
    counter = counter + 1
    x = int(input())
    if(x == random):
        print(f"Good job, {name}! You guessed my number in {counter} guesses!")
        continue1 = False
    else:
        print("Take a guess")

