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
  
| Task No | Planned Action                           | Planned Outcome                                                                          | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------|------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                    | To have a clear idea of the hardware and software requirements for the proposed solution | 10 min        | Sep 22                 | A         |
| 2       | Meet with client                         | Recieve Client's aproval                                                                 | 5 min         | Sep 23                 | A         |
| 3       | Design the menu                          | Have enough options to satisfy the client                                                | 20 min        | Sep 27                 | B         |
| 4       | Create flow diagrams                     | Make them easy to understand                                                             | 1hr           | Sep 30                 | B         |
| 5       | Create system diagram                    | Also make them easy to understand                                                        | 10 min        | Sep 30                 | B         |
| 6       | Code the menu                            | Make it functional and simple to use for the client                                      | 20 min        | Oct 1                  | C         |
| 7       | Code the login system                    | Gain the client's trust in how the program is password and username protected            | 30 min        | Oct 1                  | C         |
| 8       | Code all main functions                  | Make sure to stick to success criteria and simple to use                                 | 10 hrs        | Oct 3                  | C         |
| 9       | Make the program more visually appealing | Make the client want to use it and enjoy the visuals                                     | 20 min        | Oct 3                  | C         |
| 10      | Record Demonstration Video               | To have a video demonstrating how to use the crypto wallet                               | 20 min        | Oct 4                  | B         |

# citation

[1] Binance Academy. “Dogecoinとは？.” Binance Academy, Binance Academy, 9 Oct. 2020, academy.binance.com/ja/articles/what-is-dogecoin. Accessed 1 Oct. 2022.
  
[2] “Cryptocurrency Dogecoin (DOGE): What It Is, History, Uses.” Investopedia, 2022, www.investopedia.com/terms/d/dogecoin.asp. Accessed 1 Oct. 2022.
  
[3] “PyCharm：JetBrainsによるプロ開発者向けPython IDE.” Jetbrains.com, JetBrains, 2022, www.jetbrains.com/ja-jp/pycharm/. Accessed 2 Oct. 2022.
  
[4] Rhita Koubbi. “A 2020 Guide to Python 2 vs Python 3.” Career Karma, 14 July 2020, careerkarma.com/blog/python-2-vs-python-3/. Accessed 2 Oct. 2022.
  
[5]“What Is a .CSV File and What Does It Mean for My Ecommerce Business?” BigCommerce, 2022, www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/. Accessed 2 Oct. 2022.


‌

‌
‌
