def check_balance(name):
    print(f"Your current balance is: {details[name]['bal']}")


def withdrawal(name):
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw > details[name]['bal']:
        print("Error! Cannot withdraw more than available balance")
    elif withdraw <= 0:
        print("Invalid Input!")
    else:
        print(f"{withdraw} withdrawn")
        details[name]['bal'] = details[name]['bal']-withdraw


def deposit(name):
    dep = float(input("Enter amount to deposit: "))
    if dep <= 0:
        print("Error! Invalid input")
    else:
        details[name]['bal'] = details[name]['bal']+dep
        print(f"You've deposited {dep}!")


def open_account(name):
    while True:
        name = str(input("Enter your desired username: "))
        if name in details:
            print("Username already exists!")
        else:
            details[name] = {'bal': 0, 'PIN': 'default'}
            while True:
                new_pin = str(input("Enter your desired PIN: "))
                if len(new_pin) == 4 and new_pin.isdigit():
                    details[name]['PIN'] = new_pin
                    break
                else:
                    print("Pin should atleast have 4 numbers!")
            new_bal = float(
                input('Deposit some initial amount for account creation: '))
            if new_bal <= 0:
                print("Invalid amount!")
                details.pop(name)
            else:
                details[name]['bal'] = new_bal
                print(
                    f"{new_bal} deposited! Congratulations {name} Your account has been created!")
                break


def transfer_money(name):
    transfer_to = str(input("Enter recipient name: "))
    if transfer_to not in details:
        print("Account doesn't exist.")
    else:
        amount_to_transfer = float(input("Enter amount to tansfer: "))
        if amount_to_transfer > details[name]['bal']:
            print("Insufficient Balance!")
        elif amount_to_transfer <= 0:
            print("Invalid Input!")
        else:
            details[name]['bal'] -= amount_to_transfer
            details[transfer_to]['bal'] += amount_to_transfer
            print(
                f"Transaction successful!\n{name} Transferred {amount_to_transfer} to {transfer_to}!")


details = {
    "Mark": {'bal': 5000, 'PIN': '5282'},
    "John": {'bal': 10000, 'PIN': '6292'},
    "Nova": {'bal': 1, 'PIN': '0100'}
}

is_name = str(input("Enter your registered name: "))
if is_name not in details:
    print("You do not have an account in our bank!")
    while True:
        open_acc = input(
            "Press 'Enter' to begin account opening process.\nq to quit.")
        if open_acc == '':
            open_account(open_acc)
            break
        elif open_acc == 'q':
            break
        else:
            print("Invalid Input")
else:
    is_pin = str(input('Enter your PIN: '))
    if is_pin == str(details[is_name]['PIN']):
        while True:
            print("Choose the action you want to perform!")
            print("1: check balance")
            print("2: withdraw amount")
            print("3: deposit amount")
            print("4: Transfer money")
            print("5: quit")
            choice = input("Enter choice: ")
            if choice == '1':
                check_balance(is_name)
            elif choice == '2':
                withdrawal(is_name)
            elif choice == '3':
                deposit(is_name)
            elif choice == '4':
                transfer_money(is_name)
            elif choice == '5':
                break
            else:
                print("Invalid input")
    else:
        print("Wrong Pin! Session terminated!")

print("Thanks for banking with us!")
