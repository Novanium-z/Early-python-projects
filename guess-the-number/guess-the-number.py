import random
import json
import os
if not os.path.exists("users.json"):
    with open("users.json", "wt") as fh:
        json.dump({}, fh)
while True:
    with open("users.json", "rt") as dh:
        user_data = json.load(dh)
    for user in user_data:
        games = user_data[user]["games played"]
        wins = user_data[user]["Wins"]
        if games > 0:
            user_data[user]["Win Percentage"] = (wins / games) * 100
        else:
            user_data[user]["Win Percentage"] = 0
    with open("users.json", "wt") as fh:
        json.dump(user_data, fh, indent=4)
    users = user_data
    print("Welcome to the number guessing game!")
    is_user = input("Enter your username (or q to quit): ")
    if is_user in users:
        print(
            f"Welcome! {is_user} Choose an action:\n1: View your statistics\n2: Play the game")
        doing = str(input("Enter your choice "))
        if doing == '1':
            print(f"Here are your stats!\n{user_data[is_user]}")
        elif doing == '2':
            print("You have to guess a number from 1 to 50!")
            user_data[is_user]["games played"] += 1
            with open("users.json", "wt") as gh:
                json.dump(user_data, gh, indent=4)
            _num = random.randint(1, 50)
            for i in range(10, 0, -1):
                try:
                    print(f"You have {i} guesses left!")
                    guess = int(input("Enter your guess: "))
                    if guess < 0 or guess > 50:
                        raise ValueError()
                    if guess == _num:
                        print(f"Congrats!! {guess} was the number! ")
                        with open("score.txt", "at") as fh:
                            fh.write(
                                f"{is_user} guessed the number in {11-i} tries!"+'\n')
                        user_data[is_user]["Wins"] += 1
                        if user_data[is_user]["Best score"] > 11-i:
                            user_data[is_user]["Best score"] = 11-i
                        with open("users.json", "wt") as sh:
                            json.dump(user_data, sh, indent=4)
                        break
                    elif i == 1:
                        print(f"Game over! The number was {_num}!")
                        break
                    elif _num-5 < guess < _num:
                        print(
                            f"{guess} is Wrong! maybe a 'little more' than that!")
                    elif guess < _num:
                        print(f"{guess} is Wrong! maybe more")
                    elif _num < guess < _num+5:
                        print(
                            f"{guess} is Wrong! maybe a 'little less' than that!")
                    elif guess > _num:
                        print(f"{guess} is Wrong! maybe less than that")
                except ValueError:
                    print("Invalid Input!")
                    continue
        else:
            print("Invalid Input!")
    elif is_user == 'q':
        break
    else:
        print("Username doesn't exist Press:\nEnter to create your own\nq to quit")
        to_do = input("Enter your choice: ")
        if to_do == '':
            new_user = input("Enter your desired username: ")
            if new_user in users:
                print("Username already exists!")
            else:
                users[new_user] = {
                    "games played": 0, "Wins": 0, "Best score": 50000, "Win Percentage": 0
                }
                with open("users.json", "wt") as fh:
                    json.dump(users, fh, indent=4)
        elif to_do == 'q':
            break
print("Thanks for playing!")
