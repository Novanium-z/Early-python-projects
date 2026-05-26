import random
print("Let's roll some dice!")
while True:
    choice = input("Press 'Enter' to roll or 'q' to exit: ")
    if choice == '':
        num = random.randint(1, 6)
        print(f"You rolled {num}!")
    elif choice == 'q':
        break
    else:
        print("Invalid Input!")
print("Thanks for playing!")
