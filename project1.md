# Crypto Wallet

![image](https://user-images.githubusercontent.com/111941936/195844032-fcd2920b-1679-45a2-bed7-b3b5f84676f0.png)

<sub>Fig1 Shows illustration of doge coin used in Binance Academy [1]<sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

I will to design and make an electronic ledger for a client who is interested in crypto curency trading, specificaly the Dogecoin. The program will organize Ms. Sato's transaction and is constructed using the software pycharm. This crypto wallet will provide efficient and simple-to-understand functions that would help the client achieve a better understanding of the Doge coin and help organize her digtal transactions. 

## Rationale for proposed solution

I have chosen Dogecoin as my crypto currency because despite being a cryptocurrency that originated as online jokes, Dogecoin has grown a loyal user base. It still has a market valuation in the hundreds of millions of dollars till this day. Furthermore, high liquidity makes it simpler for investors to invest in and withdraw from Dogecoin. As its price rises, more celebrities, like Elon Musk, are likely to endorse it, creating an upward price pressure[2].
  
This electronic ledger would be constructed by Python 3 in Pycharm. I decided to use Pycharm because it helps write clean and maintainable code as the IDE helps maintain quality control with PEP8 checks, test assistance, smart refactorings, and numerous inspections [3]. Furthermore, the reason for using Python 3 is that is has clear, existing commands already built into the code, has simple syntax, making it very user-friendly - especially for me to be able to focus my time on designing rather than the coding process. Additionally, Python3 is commonly utilized for data analytics. Data may be gathered and managed securely using Python 3. Last but not least, Python3 is a wonderful fit for finance in dealing with quantitative data because the main objective is to establish a digital wallet for the customer[4].
  
CSV files were used to store data of this wallet: including tthe username and password, as well as the transactions being made. The reason behind using a CSV file is CSV files are plain-text files, making them easier for the website developer to create. Since they're plain text, they're easier to import into a spreadsheet or another storage database, such as in python[5].
  
It will take 3 weeks to make and will be evaluated according to the criteria A, B and C.

## Information about the Doge coin

Dogecoin (DOGE) is a peer-to-peer, open-source cryptocurrency. It was introduced in December 2013 as an alternative cryptocurrency, and its logo is a Shiba Inu dog. The blockchain of Dogecoin has appeal since it uses Litecoin's core technology. Dogecoin, which employs the scrypt algorithm, is notable for its low cost and limitless supply. Dogecoin marketed itself as a "fun" version of Bitcoin with a Shibu Inu dog as its logo. Dogecoin's casual presentation suited the mood of the burgeoning crypto community. Its scrypt technology and unlimited supply were an argument for a faster, more adaptable, and more consumer-friendly version of Bitcoin. Many different types of businesses accept DOGE including Elon Musk's SpaceX and the Dallas Mavericks. Many Dogecoin holders use their DOGE to tip content creators on Reddit and other social media platforms [2]. 


## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger display the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger is protected by password and username.
5. The electronic ledger lets the user convert USD to Doge coin.
6. The electronic ledger will show the latest transactions with dates of the current year.  

# Criteria B: Design

## System Diagram

<img width="1002" alt="Screen Shot 2565-10-23 at 14 42 41" src="https://user-images.githubusercontent.com/111941936/197375896-d73398e5-21c0-43e0-bb35-345a9ef59d35.png">

<sub>Fig.2 shows the system diagram 

The data are stored and recorded in comma separated value files. The first file, wallet.csv, stores the transactions and balance. The second file, db.csv, stores Ms Sato's username and password required to access the digital ledger. A total of 3 python files were used: Crypto wallet.py as the main program file, my_library stores colors, graphics, and input valifdation functions, simple_login is used to store the function of logging into the program.

## Flow Diagrams

## Test Plan

|                             Description                             |                   Type                  |                                                                                 Inputs                                                                                |                                                                                                                                                                                                          Outputs                                                                                                                                                                                                         |
|:-------------------------------------------------------------------:|:---------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| login system                                                        | White box, integration test, functional | 1.Enter username: 2.Enter Password:                                                                                                                                   | The program will continue if the user enters the correct username and password. But if either the username or password But if either the username or password - or both are incorrect the program will print: "Incorrect username or password. Please enter again." More than 3 times,  the program would end if the number of tries exceeds 3.                                                                          |
| login database check                                                | unit test, functional                   | 1.Open file: db.csv 2.Check that each lines contain a value with two elements separated by commas                                                                     | If the username and password entered matches in the correct format, the program will continue                                                                                                                                                                                                                                                                                                                            |
| menu function                                                       | unit test, White box, functional        | 1.enter number of option 1-5 2.or enter invalidate input outside the numbers                                                                                          | The program should go to the choice entered if the number entered falls inside one of the five possible outcomes. If a wrong number is entered, the program should go back to the menu till the input is validated.                                                                                                                                                                                                      |
| date validation                                                     | unit test, functional                   | 1.check if the date input format was correct (YYYY-MM-DD) 2.the date format is correct 3.the date format is incorrect 4.re-enter in the correct format                | The program should move on to the following step if the input is formatted correctly. A message should be returned by the program notifying the user that their input is incorrect and that they should try again if it is in the improper format.                                                                                                                                                                       |
| number validation                                                   | unit test, functional                   | 1.check if the number input format was correct (either int or float) 2.the number format is correct 3.the number format is incorrect 4.re-enter in the correct format | The program should move on to the following step if the input is formatted correctly. A message should be returned by the program notifying the user that their input is incorrect and that they should try again if it is in the improper format.                                                                                                                                                                       |
| test option 1: view basic information and convert yen to doge coins | integration unit test, functional       | 1.Enter option 1 in menu 2.Enter amount of USD wanted to convert to Dogecoin                                                                                          | The program should display the basic information about Dogecoin. The number entered for USD should be converted into Dogecoin Value                                                                                                                                                                                                                                                                                      |
| test option 2: current wallet balance                               | unit test, functional                   | 1.Enter option 2 2.'yes' if they would like to convert to USD                                                                                                         | The program should display the latest value of 'price' from the wallet.csv file. If the user input yes, the program should convert the value to USD                                                                                                                                                                                                                                                                      |
| test option 3: past transactions                                    | unit test, functional                   | 1.Enter option 3                                                                                                                                                      | The program should display the all of the 'date' and 'amount changes' from the wallet.csv                                                                                                                                                                                                                                                                                                                                |
| test option 4: withdraw, record, enter                              | unit test, functional                   | 1.Enter option 4 2.Enter out of option 1-3 3.Enter number of transaction they would like to withdrew 4.Enter date, amount changed, final amount of their transaction  | The program should go to the choice entered if the number entered falls inside one of the three possible outcomes. Print the lastest transaction and then notify the completion of withdrawal after esasing the entered number of transaction from wallet.csv. Ask the user to input the date, amount changed, and the amount they would have then notify the completion of recording after adding it to the wallet.csv. |
| test option 5: exit                                                 | unit test, functional                   | 1.Enter option 5                                                                                                                                                      | The program should display the thank you message and end the program                                                                                                                                                                                                                                                                                                                                                     |
| edit the visuals of the interface                                   | integration, non-functional             | 1.run through the program 2.add colors and graphics                                                                                                                   | The program's printed out part looks more visually appealing                                                                                                                                                                                                                                                                                                                                                             |
| test by others                                                      | integration, functional                 | 1.run the program like they are Ms Sato 2.Had no prior knowledge to how the program is supposed to work                                                               | The program will produce an output if the users correctly understand what to input in each part. The output must match the users' needs.                                                                                                                                                                                                                                                                                 |
| feedback from others                                                | non-functional, usability               | 1.enter the inputs required to receive the outputs they require                                                                                                       | The program will be user friendly and not over complicated                                                                                                                                                                                                                                                                                                                                                               |
| end to end run through                                              | system testing                          | 1. run through the entire program trying all the functions                                                                                                            | The program will run smoothly with no issues                                                                                                                                                                                                                                                                                                                                                                             |

## Record of Tasks
  
| Task No | Planned Action                                                | Planned Outcome                                                                                                            | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | should be aware of the appropriate requirements for hardware and software needed for the proposed solution                 | 10 min        | Sep 22                 | A         |
| 2       | Meet with client                                              | to discuss what the client expects from the digital ledger and come to an agreement of what the functions would look like  | 5 min         | Sep 23                 | A         |
| 3       | Create success criteria                                       | to make sure the functions designed reaches all the requirements that was agreed on with the client earlier                | 20 min        | Sep 24                 | A         |
| 4       | Design the menu                                               | Have enough options to satisfy the client                                                                                  | 20 min        | Sep 27                 | B         |
| 5       | Create flow diagrams                                          | To provide a visual representation of how a function operates and to prepare before coding                                 | 1hr           | Sep 30                 | B         |
| 6       | Create system diagram                                         | Ensure that the client is informed of the wallet's system.                                                                 | 10 min        | Sep 30                 | B         |
| 7       | Code the menu                                                 | To be able to have the client choose which function they would like to use                                                 | 20 min        | Oct 1                  | C         |
| 8       | Test the menu manually with white box method by the developer | Make sure that the functions run smoothly and is easy to understand                                                        | 10 min        | Oct 1                  | B         |
| 8       | Code the login system                                         | Gain the client's trust in how the program is password and username protected                                              | 30 min        | Oct 1                  | C         |
| 9       | Code all main functions                                       | Make sure to stick to success criteria and simple to use                                                                   | 10 hrs        | Oct 3                  | C         |
| 10      | Make the program more visually appealing                      | Make the client want to use it and enjoy the visuals                                                                       | 20 min        | Oct 3                  | C         |
| 11      | Record Demonstration Video                                    | To have a video demonstrating how to use the crypto wallet                                                                 | 20 min        | Oct 4                  | B         |

# Criteria C: Development

## Tools used

Functions
  
For/while loops
  
Input Validation
  
If statements
  
Encryption  
  
## Login systen
  
```py
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
```

Fig.6 showcases the login system for the crypto wallet.The input required is the username and the password, which are both stored in the db.csv file for Ms. Sato. The login system will be displayed first in the program because, from the success criteria, the ledger is password protected in order to gain the client's trust. Therefore, if either the username or password or both are incorect for more than 3 times, the program will come to an end, but if both are correct, the program will continue to the menu page. Once the username and password are correct, the program will insert the username into the welcome message in order to make it more personal for the client. The reason for having a maximum try of 3 is that if there is no limit, anyone could just continue to do it, which is a waste of time and they might possibly get it right. The login function is also imported from the simple_login python file, where it is recommended to open the db.csv file and read the username and password from it. If the input matches, the program will continue. 
  
A while looop was used for the number of tries in order to make it easier to try again with a shorter code (a loop). An if statement was also used for the verification of the login inputs if either one was false and exceeded 3 tries.
                                       
## Current wallet balance
                                       
```py
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
```

Fig. 7 shows the option for the client to check the current wallet balance of their digital ledger. This function opens up the wallet.csv file and splits the comma to access data number 3 'banlance', which in Python is data number 2, and reads the one in the last line since it is the most recent one and prints it out for the client to see. 

After that, the program will ask whether the client would want to convert the Dogecoin value they currently have to USD by using an if statement. If the client types in "yes", the program will multiply the current balance, which is a float since it has decimals, to the current_doge_value from the my_library python file. The program will then print out the final value. If the client inputs anything other than 'yes', the program will return to the menu.
    
## menu

```py
menu = '''
MENU:
1️⃣ view basic information and convert yen to doge coins
2️⃣ check current wallet balance
3️⃣ review this year's past transactions
4️⃣ withdraw or deposit a transaction
5️⃣ exit
'''
  
  while True:
    print(f'{colors[4]}{menu}')
    choice = validate_int_input("enter your choice (number): ")
    if choice == 1:
        basic_info()
    elif choice == 2:
        wall_bal()
    elif choice == 3:
        past_trans()
    elif choice == 4:
        with_dep()
    elif choice == 5:
        print(f"{colors[5]}Thank you for using this platform, Ms Sato! Have an amazing day <3")
        exit()
```

Fig.8 shows the menu for the electronic ledger. The printed out menu was imported from the my_library python file in order to make the main file more organised and have emojis to make it stand out and more visually appealing. 

A while loop was used for the client to enter the number of the function they would like to use, and the validate_int_input was imported from the my_library. py was used to validate if the input was a number between 1 to 5. If not, the program will keep asking to re-enter until the input fits the criteria. From the input, once it's correct, the program would lead the client to one of the 4 functions for each choice, with the last choice being a printed out message before ending the program.                                    
                                       
## record a transaction

```py    
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
```          

Fig.9 shows the option to withdraw a transaction from the fourth option to withdraw or deposit a transaction. In the main function, the user was made to decide between choice 1: to withdraw a transaction, or choice 2: to deposit a transaction. This is currently showing choice 1. After the client had entered '1' in the if statement used, the file wallet.csv was opened and the date and amount changed were read out in separate paragraphs through the use of a for loop. A number was also given to each transaction to make it easier to read for the client. 

Once all the past transactions are printed out with numbers in front, the program then asks the user to enter the number of the transaction they would like to withdraw, which is why a number was added in front of each transaction since it would be easier to read and type out. The validate_int_input from my_linrary.py was used again in order to make sure they entered the correct number. The function then re-opens the wallet.csv file and goes to the line of the number entered by the use of for lin in enumerate data. The line of the transaction was then deleted out of the wallet file. The function finishes by printing out a message to confirm the withdrawal of the transaction.
  
# citation

[1] Binance Academy. “Dogecoinとは？.” Binance Academy, Binance Academy, 9 Oct. 2020, academy.binance.com/ja/articles/what-is-dogecoin. Accessed 1 Oct. 2022.
  
[2] “Cryptocurrency Dogecoin (DOGE): What It Is, History, Uses.” Investopedia, 2022, www.investopedia.com/terms/d/dogecoin.asp. Accessed 1 Oct. 2022.
  
[3] “PyCharm：JetBrainsによるプロ開発者向けPython IDE.” Jetbrains.com, JetBrains, 2022, www.jetbrains.com/ja-jp/pycharm/. Accessed 2 Oct. 2022.
  
[4] Rhita Koubbi. “A 2020 Guide to Python 2 vs Python 3.” Career Karma, 14 July 2020, careerkarma.com/blog/python-2-vs-python-3/. Accessed 2 Oct. 2022.
  
[5]“What Is a .CSV File and What Does It Mean for My Ecommerce Business?” BigCommerce, 2022, www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/. Accessed 2 Oct. 2022.


‌

‌
‌
