account_name = 'Joe'
account_balance = 100
account_password = 'soup'

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')

    action = input("What do you want to do? ").lower()[0]

    if action == 'q':
        break

    user_password = input('Please enter your password: ')
    if user_password != account_password:
        print('Incorrect Password')
        continue

    if action == 'b':
        print('Your balance is: $', account_balance)
    elif action == 'd':
        amount = float(input('How much do you want to deposit?: '))
        account_balance += amount
        print('Your balance is: $', account_balance)
    elif action == 'w':
        amount = float(input('How much do you want to withdraw?: '))
        account_balance -= amount
        print('Your balance is: $', account_balance)
    elif action == 's':
        print(f'Account details:\nName: {account_name}\nBalance: {account_balance}')
