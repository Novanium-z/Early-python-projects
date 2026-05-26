import random
print("You have to guess a number from 1 to 50!")
_num = random.randint(1, 50)
for i in range(10, 0, -1):
    print(f"You have {i} guesses left!")
    guess = int(input("Enter your guess: "))
    if guess == _num:
        print(f"Congrats!! {guess} was the number! ")
        break
    elif i == 1:
        print(f"Game over! The number was {_num}!")
        break
    elif _num-5 < guess < _num:
        print(f"{guess} is Wrong! maybe a 'little more' than that!")
    elif guess < _num:
        print(f"{guess} is Wrong! maybe more")
    elif _num < guess < _num+5:
        print(f"{guess} is Wrong! maybe a 'little less' than that!")
    elif guess > _num:
        print(f"{guess} is Wrong! maybe less than that")
