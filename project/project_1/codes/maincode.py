from my_library import validate_int_input, end_code, colors, current_doge_value, Open_msg, doge_info,menu,validate_float_input,validate_date_input,with_dep_op,price
from simple_login import login

# login system
print(f'{colors[4]}please login to your account')
pass_wrong_count = 0
username = input("enter username: ")
password = input("Please enter your password: ")
right_pw = login(password=password, user=username)
max_attempts=3
while pass_wrong_count < max_attempts-1 and right_pw == False:
    pass_wrong_count += 1
    print(f"{colors[1]}Incorrect username or password.Attempts left {max_attempts - pass_wrong_count}. Please try again.{end_code}")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    right_pw = login(password=password, user=username)

if pass_wrong_count == 3 or right_pw == False:
    print(f"{colors[1]}Too many incorrect attempts. Exiting program.{end_code}")
    exit()

print(f"{colors[6]}Welcome back! {Open_msg}".center(50))
print("access granted!".center(50))

# 1 basic information
def basic_info() :
    print(f"{colors[5]} {doge_info}")
    mon_con = float(input('enter amount of USD you would like to convert: '))
    convert_usd = mon_con / current_doge_value
    print(f'{mon_con} USD equals to roughly to {convert_usd} Doge coins')


# 2 current wallet balance
def wall_bal():
    balance = 0
    with open("wallet.csv") as file:
        wallet = file.readlines()
        i = 0
        for line in wallet:
            if i > 0:
                data = line.split(",")
                balance = data[2]
            i += 1
    current = f'{colors[5]} You currently have {colors[4]}{balance}{colors[5]} doge coins in your wallet!'
    print(current)

    second_conv = input("'yes' if you would like to convert your balance to USD: ")
    if second_conv.lower() == "yes":
        sec_con = float(balance) * current_doge_value
        print(f'Your current Doge coins value to {colors[4]}{sec_con}{colors[5]} USD!')
    else:
        return menu

# past transactions
def past_trans():
    print('here are the lastest transactions: ')
    with open("wallet.csv", "r") as file:
        wallet = file.readlines()
        i = 0
        for line in wallet:
            if i > 0:
                data = line.split(",")
                print(f"{colors[5]}{data[0]}: {data[1].rjust(10)}")
            i += 1

# withdraw, record, enter
def with_dep():
    print(colors[5] + """
    1. Withdraw a transaction
    2. Record a transaction
    3. Done
    """)
    choice = validate_int_input("enter your option: ")
    if choice == 1:
        print("Here are the current transactions:   ")
        with open("wallet.csv", "r") as file:
            wallet = file.readlines()
            i = 0
            for line in wallet:
                if i > 0:
                    data = line.split(",")
                    print(f"({i}) {data[0]}: {data[1]}")
                i += 1
        delete_no = validate_int_input("enter number of transaction: ")
        with open("wallet.csv", "r") as file:
            data = file.readlines()
        with open("wallet.csv", "w") as file:
            for i, line in enumerate(data):
                if i != delete_no:
                    file.write(line)
        print(f"{colors[2]}Transaction withdrawn!")
    if choice == 2:
        with open("wallet.csv", "a") as file:
            print(f'{with_dep_op} ')
            sec_choice = validate_int_input("enter your option: ")
            if sec_choice == 1:
                date = validate_date_input("enter the date of the transaction(YYYY-MM-DD): ")
                def price():
                    bal = (0)
                    with open("wallet.csv") as file:
                        wallet = file.readlines()
                        i = 0
                        for line in wallet:
                            if i > 0:
                                data = line.split(",")
                                bal = data[2]
                            i += 1
                        print(bal)
                    print(f'You currently have {colors[4]}{bal}{colors[5]} doge coins')
                price()
                amount = validate_float_input("enter the amount of doge entered you would like to add: ")
                new_am = validate_float_input("Enter the new amount you would now have (please make sure it's correct!): ")
                file.write(f"{date},+{amount},{new_am},Deposit")
                print(f'{colors[6]}Transaction Recorded! Restart the program before checking the updated balance')
                return with_dep_op
            if sec_choice == 2:
                date = validate_date_input("enter the date of the transaction(YYYY-MM-DD): ")
                price()
