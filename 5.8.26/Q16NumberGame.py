# make a number game
from random import randint
print("Welcome to the Number Game")
rndm_num = randint(1,100)
lives = 10
while True:
    n = int(input("Guess a num between 1 and 100: "))
    if n > rndm_num:
        print("Your guess is higher than my number")
        lives -= 1
    elif n < rndm_num:
        print("Your guess is lower than my number")
        lives -= 1
    else:
        print(f"You were right the number was {rndm_num}")
        print(f"You got the answer in {lives} chances and your score was {(10 - lives) * 10}")
        break
    if lives == 0:
        print(f"You ran out of lives. The correct answer was {rndm_num}")
        break