# Chapter 1 - Input, print and numbers

## Sum of three numbers

Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

```.py
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

<img width="806" alt="Screen Shot 2565-09-01 at 20 58 00" src="https://user-images.githubusercontent.com/111941936/187908669-1c9892ce-6dd5-4b0b-aab9-6b89647a5313.png">

## Hi John

Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.

```.py
print('Hi',input())
```

<img width="795" alt="Screen Shot 2565-09-01 at 21 05 30" src="https://user-images.githubusercontent.com/111941936/187919470-8f3ac8df-53fe-40c4-af90-d7b1a7b166f1.png">

## Square

Write a program that takes a number and print its square.

```.py
a = int(input())
print(a ** 2)
```

<img width="803" alt="Screen Shot 2565-09-01 at 22 19 37" src="https://user-images.githubusercontent.com/111941936/187924090-405abebb-4617-4bd2-9379-238cc7189f69.png">

## Area of right-angled triangle

Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.

```.py
b = int(input())
h = int(input())
print(1/2 * b * h)
```

<img width="799" alt="Screen Shot 2565-09-01 at 22 25 22" src="https://user-images.githubusercontent.com/111941936/187926218-801baef4-5434-4fd1-b213-7ce13611ad8b.png">

## Hello, Harry!

Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. 

```.py
name = input()
print('Hello'+ ', ' + name + '!')
```

<img width="799" alt="Screen Shot 2565-09-01 at 22 37 31" src="https://user-images.githubusercontent.com/111941936/187927945-9477d191-f83f-40f9-81f0-efa6ddc30bba.png">

## Apple sharing

N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

```.py
n = int(input())
k = int(input())
print(k // n)
print(k % n)
```

<img width="800" alt="Screen Shot 2565-09-01 at 22 48 15" src="https://user-images.githubusercontent.com/111941936/187930481-dbdaa989-e9d3-4662-8e7b-604b5b0e174e.png">

## Previous and next

Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

```.py
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')
```

<img width="997" alt="Screen Shot 2565-09-03 at 00 01 24" src="https://user-images.githubusercontent.com/111941936/188178227-5653d593-2584-40c7-9ab5-acaf92ba3348.png">

## Two timestamps

A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

```py
hrs_1 = int(input())
mins_1 = int(input())
secs_1 = int(input())
hrs_2 = int(input())
mins_2 = int(input())
secs_2 = int(input())
print(hrs_2 * 3600 + mins_2 * 60 + secs_2
- hrs_1 * 3600 - mins_1 * 60 - secs_1)
```

<img width="807" alt="Screen Shot 2565-09-04 at 21 13 45" src="https://user-images.githubusercontent.com/111941936/188312881-984257ec-dc1b-4e6c-83af-a2a19e07b2b4.png">

## School desks

A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

```py
a = int(input())
b = int(input())
c = int(input())
print(a//2 + b//2 + c//2 + a%2 + b%2 + c%2)
```

<img width="798" alt="Screen Shot 2565-09-04 at 21 23 25" src="https://user-images.githubusercontent.com/111941936/188313333-3fda4422-3def-47d9-860e-a88dd7a02eed.png">

# Chapter 2 - Integer and float numbers

## Last digit of integer

Given an integer number, print its last digit.

```py
a = int(input())
print(a % 10)
```

<img width="794" alt="Screen Shot 2565-09-04 at 21 53 35" src="https://user-images.githubusercontent.com/111941936/188314518-ea0b9e91-f567-4579-a07d-3a7d30a12418.png">

## Two digits

Given a two-digit number, print its digits separately.

```py
a = int(input())
print(a//10, a%10)
```

<img width="787" alt="Screen Shot 2565-09-04 at 21 56 38" src="https://user-images.githubusercontent.com/111941936/188314676-4538148b-7e85-4eb0-a79c-84446402770d.png">

## Swap digits

Given a two-digit number, swap its digits as shown in the tests below.

```py
a = int(input())
tens = a // 10
units = a % 10
print(units * 10 + tens)
```

<img width="791" alt="Screen Shot 2565-09-04 at 22 02 06" src="https://user-images.githubusercontent.com/111941936/188314887-0a1f8821-db64-4dc3-8fc8-2ff0d15ad675.png">

## Last two digits

Given an integer number, print its last two digits.

```py
a = int(input())
print(a % 100)
```

<img width="790" alt="Screen Shot 2565-09-04 at 22 08 15" src="https://user-images.githubusercontent.com/111941936/188315162-174b6ae3-c53c-49c7-962b-fb0709d8b703.png">

## Tens digit

Given an integer. Print its tens digit.

```py
a = int(input())
print(a // 10 % 10) 
```

<img width="788" alt="Screen Shot 2565-09-04 at 22 19 17" src="https://user-images.githubusercontent.com/111941936/188315663-260b4f7f-90b7-4562-b513-a87b7e0d4916.png">

## Sum of digits

Given a three-digit number. Find the sum of its digits.

```py
a = int(input())
hundreds = (a // 100)
tens = (a // 10 % 10)
units = (a % 10)
print(hundreds + tens + units)
```

<img width="800" alt="Screen Shot 2565-09-05 at 09 47 24" src="https://user-images.githubusercontent.com/111941936/188340523-b7661aa1-ad23-4c87-8f81-6307c1fc9abc.png">

## Reverse three digits

Given a three-digit integer number, print its digits in a reversed order.

```py
a = int(input())
units = a % 10
tens = a % 100 // 10
hundreds = a // 100
print(units * 100 + tens * 10 + hundreds)
```

<img width="789" alt="Screen Shot 2565-09-05 at 09 52 08" src="https://user-images.githubusercontent.com/111941936/188340791-9bea5426-82d2-4919-9b81-c12521d2f14a.png">

## Merge two numbers

Given two two-digit numbers, merge their digits as shown in the tests below.

```py
a = int(input())
b = int(input())
tens_a = a // 10
units_a = a % 10
tens_b = b // 10
units_b = b % 10
print(tens_a * 1000 + tens_b * 100 + units_a * 10 + units_b)
```

<img width="782" alt="Screen Shot 2565-09-05 at 10 07 04 1" src="https://user-images.githubusercontent.com/111941936/188341689-785a345d-33b5-4b1f-8ba0-0cbe1c360cd6.png">

## Cyclic rotation

Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below.

```py
a = int(input())
print(a % 100 * 100 + a // 100)
```

<img width="784" alt="Screen Shot 2565-09-05 at 11 11 40" src="https://user-images.githubusercontent.com/111941936/188346663-1aec7379-21b7-4ebb-a359-5d33a9ec3717.png">

## Fractional part

Given a positive real number, print its fractional part.

```py
a = float(input())
print(a - int(a))
```

<img width="796" alt="Screen Shot 2565-09-05 at 11 19 18" src="https://user-images.githubusercontent.com/111941936/188348439-10d8fa2f-1daa-4aff-b741-2e407b804c6b.png">

## First digit after decimal point

Given a positive real number, print its first digit to the right of the decimal point.

```py
a = float(input())
b = a * 10
print(int(b) % 10)
```

<img width="781" alt="Screen Shot 2565-09-05 at 11 25 34" src="https://user-images.githubusercontent.com/111941936/188349053-25b61876-ed3f-4de6-af7a-c5f8a724b298.png">

## Car route

A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

```py
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
```

<img width="789" alt="Screen Shot 2565-09-06 at 19 29 21" src="https://user-images.githubusercontent.com/111941936/188613136-f6e96caf-6dd7-4254-bb0c-8d66ba96cab6.png">

## Day of week

Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday.

```py
k = int(input())
print((k + 3) % 7)
```

<img width="778" alt="Screen Shot 2565-09-07 at 20 08 52" src="https://user-images.githubusercontent.com/111941936/188864205-d33243df-60d1-4bc4-a29f-5aef23877d7f.png">

## Digital clock

Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?

```py
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)
```

<img width="802" alt="Screen Shot 2565-09-15 at 09 59 48" src="https://user-images.githubusercontent.com/111941936/190288799-ef51c224-ad58-4689-9dfe-a3824dd13e8e.png">

## Total cost

A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

```py
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)
```

<img width="793" alt="Screen Shot 2565-09-15 at 10 01 12" src="https://user-images.githubusercontent.com/111941936/190288957-0c9ec27f-692e-4064-8b86-cea2df40509f.png">

## Century

Given a year as a positive integer, print its century. Mind that the 20th century began on 1901 and ended on 2000.

```py
a = int(input())
print((a - 1) // 100 + 1)
```

<img width="794" alt="Screen Shot 2565-09-15 at 10 05 04" src="https://user-images.githubusercontent.com/111941936/190289348-403fdca7-cac2-4c8a-912d-378ca3ec74ec.png">

## Snail

A snail goes up A feet during the day and falls B feet at night. How long does it take him to go up H feet?
Given three integer numbers H, A and B (A > B), the program should output a number of days.

```py 
from math import ceil

h = int(input())
a = int(input())
b = int(input())
print(ceil((h - a) / (a - b)) + 1)
```

<img width="792" alt="Screen Shot 2565-09-15 at 10 06 29" src="https://user-images.githubusercontent.com/111941936/190289517-d09e2d0f-bbf1-4952-a9aa-a4107a32ec41.png">

## Clock face - 1

H hours, M minutes and S seconds are passed since the midnight (0 ??? H < 12, 0 ??? M < 60, 0 ??? S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.

```py
h = int(input())
m = int(input())
s = int(input())
print( h * 30 + m * 30 / 60 + s * 30 / 3600)
```

<img width="787" alt="Screen Shot 2565-09-15 at 10 08 08" src="https://user-images.githubusercontent.com/111941936/190289684-d68aa20a-1684-4f03-b121-0afb9a12d602.png">

## Clock face - 2

Hour hand turned by ?? degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

```py
a = float(input())
print(a % 30 * 12)
```

<img width="792" alt="Screen Shot 2565-09-15 at 10 09 29" src="https://user-images.githubusercontent.com/111941936/190289920-afa640a5-262c-4112-80e3-cafc27c18a9d.png">

# Chapter 3 - Conditions: if, then, else

## Is positive

Given an integer, print "YES" if it's positive and print "NO" otherwise.

```py
a = int(input())
if a > 0:
    print('YES')
else:
    print('NO')
```

<img width="805" alt="Screen Shot 2565-09-15 at 10 14 43" src="https://user-images.githubusercontent.com/111941936/190290445-5ebcb8e0-32df-469b-ba6d-c31bbcb8f218.png">

## Is odd

Given an integer, print "YES" if it's odd and print "NO" otherwise.

```py
a = int(input())
if a % 2 != 0:
    print('YES')
else:
    print('NO')
```

<img width="791" alt="Screen Shot 2565-09-15 at 10 17 47" src="https://user-images.githubusercontent.com/111941936/190290745-880c6389-e46d-4416-88a4-0722cbb5d84a.png">

## Is even

Given an integer, print "YES" if it's even and print "NO" otherwise.

```py
a = int(input())
if a % 2 == 0:
    print('YES')
else:
    print('NO')
```

<img width="799" alt="Screen Shot 2565-09-15 at 10 19 39" src="https://user-images.githubusercontent.com/111941936/190290954-389a7fbe-f7c1-4f75-815c-d3d959fcb4ab.png">

## Ends on seven

```py
a = int(input())
if a % 10 == 7:
    print('YES')
else:
    print('NO')
```

<img width="800" alt="Screen Shot 2565-09-15 at 10 23 54" src="https://user-images.githubusercontent.com/111941936/190291462-c5f0dfaf-8c27-4a95-98d5-3519a1ef9a3d.png">

## Minimum of two numbers

Given two integers, print the smaller value.

```py
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)
```

<img width="807" alt="Screen Shot 2565-09-15 at 10 26 32" src="https://user-images.githubusercontent.com/111941936/190291819-d5ffe6f6-ba1b-46ad-8bf5-133c36bf2fae.png">

## Are both odd

```py
a = int(input())
b = int(input())
if a % 2 == 1 and b % 2 == 1:
    print('YES')
else:
    print('NO')
```

<img width="802" alt="Screen Shot 2565-09-15 at 17 23 45" src="https://user-images.githubusercontent.com/111941936/190353941-9ef29543-4e77-4c5c-b897-992c1bcf0d7c.png">

## At least one odd

Given two integers, print "YES" if at least one of them is odd and print "NO" otherwise.

```py
a = int(input())
b = int(input())
if a % 2 == 1 or b % 2 == 1:
    print('YES')
else:
    print('NO')
```

<img width="783" alt="Screen Shot 2565-09-15 at 17 25 58" src="https://user-images.githubusercontent.com/111941936/190354361-9b362082-257e-4472-93b3-1b67787ed742.png">

## Exactly one odd

Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise.

```py
a = int(input())
b = int(input())
if a % 2 == 1 and b % 2 == 0 or a % 2 == 0 and b % 2 == 1:
    print('YES')
else:
    print('NO')
```

<img width="778" alt="Screen Shot 2565-09-15 at 17 28 53" src="https://user-images.githubusercontent.com/111941936/190354982-3999e739-b4d5-4f6c-9213-cec8adbe83c8.png">

## Sign function

For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.

```py
a = int(input())
if a > 0:
    print(1)
elif a == 0:
    print(0)
else:
    print(-1)
```

<img width="801" alt="Screen Shot 2565-09-15 at 17 34 08" src="https://user-images.githubusercontent.com/111941936/190356235-647ebd51-200c-4077-9336-dfdc5126445a.png">

## Numbers in ascending order

Given three different integers, print YES if they're given in ascending order, print NO otherwise.

```py
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print('YES')
else:
    print('NO')
```

<img width="796" alt="Screen Shot 2565-09-15 at 17 37 25" src="https://user-images.githubusercontent.com/111941936/190356979-0123437d-0f23-48d5-9aff-c2a9853d0355.png">

## Is three digit

Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.

```py
a = int(input())
if a >= 100 and a < 1000:
    print('YES')
else:
    print('NO')
```

<img width="798" alt="Screen Shot 2565-09-15 at 17 41 29" src="https://user-images.githubusercontent.com/111941936/190357846-fce6bc71-a92a-482b-b887-c173176d916c.png">

## Minimum of three numbers

Given three integers, print the smallest value.

```py
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
```

<img width="798" alt="Screen Shot 2565-09-15 at 17 45 44" src="https://user-images.githubusercontent.com/111941936/190358787-4e7b7fc3-51cb-42b3-a720-50a0a16df199.png">

## Equal numbers

Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

```py
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('3')
elif a == b or a == c or b == c:
    print('2')
else:
    print('0')
```

<img width="792" alt="Screen Shot 2565-09-15 at 17 50 31" src="https://user-images.githubusercontent.com/111941936/190359856-9d60f966-c4ff-4700-baa2-617d692d9134.png">

## Rook move

Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')
```

<img width="787" alt="Screen Shot 2565-09-16 at 01 51 08" src="https://user-images.githubusercontent.com/111941936/190462407-e2d23065-e000-43b3-b160-97db933872f5.png">

## Chess board - black square

Given a square of a chessboard. Print BLACK if it's black and print WHITE otherwise.
The program receives two numbers from 1 to 8 each - the column and the row number of the square.

```py
col = int(input())
row = int(input())
if row % 2 == col % 2:
    print('BLACK')
else:
    print('WHITE')
```

<img width="793" alt="Screen Shot 2565-09-16 at 02 23 16" src="https://user-images.githubusercontent.com/111941936/190470315-5a705053-0854-4775-a44e-afff3a7ff82f.png">

## Chess board - same color

Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 + b1 + a2 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')
```

<img width="804" alt="Screen Shot 2565-09-16 at 02 36 36" src="https://user-images.githubusercontent.com/111941936/190472786-72f8cf5f-2727-4929-8623-61fb77c9c32c.png">

## Distance to closest point

Given the coordinates of the three points A, B, and C on a line. Print a distance from the point A to closest point to it.

```py 
a = int(input())
b = int(input())
c = int(input())

a_to_b = abs(a - b)
a_to_c = abs(a - c)

if a_to_b < a_to_c:
    print(a_to_b)
else:
    print(a_to_c)
```

<img width="794" alt="Screen Shot 2565-09-16 at 21 58 03" src="https://user-images.githubusercontent.com/111941936/190644262-421dfc69-8c40-4602-9af9-c637cedfa04e.png">

## Digits in ascending order

Given a three-digit integer, print YES if its digits go in ascending order, print NO otherwise.

```py
n = int(input())
a = n % 10
b = n % 100 // 10
c = n // 100
if c < b < a:
    print('YES')
else:
    print('NO')
```

<img width="802" alt="Screen Shot 2565-09-16 at 22 07 08" src="https://user-images.githubusercontent.com/111941936/190645889-6a9bf6fd-dfd9-407f-b61c-70def3512679.png">

## Four-digit palindrome

A palindrome is a number which reads the same when read forward as it it does when read backward. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

```py
n = int(input())
a = n // 100
b = (n // 10 % 10) + (n % 10 * 10)
if a == b:
    print('YES')
else:
    print('NO')
```

<img width="802" alt="Screen Shot 2565-09-18 at 16 30 47" src="https://user-images.githubusercontent.com/111941936/190890954-e2a66c46-7b79-4030-ab99-aea92c2396fb.png">

## King move

Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(a1 - a2) <= 1 and abs(b1 - b2) <= 1 :
    print('YES')
else:
    print('NO')
```

<img width="799" alt="Screen Shot 2565-09-18 at 16 37 13" src="https://user-images.githubusercontent.com/111941936/190891124-f660cd70-9a6d-45bb-bdf3-fb3a82d9888d.png">

## Bishop moves

In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(a1 - a2) == abs(b1 - b2):
    print('YES')
else:
    print('NO')
```

<img width="791" alt="Screen Shot 2565-09-18 at 16 41 19" src="https://user-images.githubusercontent.com/111941936/190891274-b05d3672-708a-4c46-8119-6541d8eb1e66.png">

## Queen move

Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(a1 - a2) == abs(b1 - b2) or a1 == a2 or b1 == b2:
    print('YES')
else:
    print('NO')
```

<img width="803" alt="Screen Shot 2565-09-18 at 16 48 35" src="https://user-images.githubusercontent.com/111941936/190891648-b06edf86-f952-404f-9fc3-de87756a5ba9.png">

## Index of outlier

Given three integers: two are equal to each other and the third one is different. Print the index number of this different one - 1, 2 or 3.

```py
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print('3')
elif a == c:
    print('2')
else:
    print('1')
```

<img width="803" alt="Screen Shot 2565-09-18 at 16 53 33" src="https://user-images.githubusercontent.com/111941936/190891798-39ac362b-21a1-4f94-830c-0f596a7934af.png">

## Knight move

Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
da = abs(a1 - a2)
db = abs(b1 - b2)
if da == 1 and db == 2 or da == 2 and db == 1:
    print('YES')
else:
    print('NO')
```

<img width="795" alt="Screen Shot 2565-09-18 at 22 14 33" src="https://user-images.githubusercontent.com/111941936/190903962-0a0213d8-ba11-4459-a951-80f220ef542a.png">

## Chocolate bar

Chocolate bar has the form of a rectangle divided into n??m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.

```py
n = int(input())
m = int(input())
k = int(input())
if k <= n * m and (k % n == 0 or k % m == 0):
    print('YES')
else:
    print('NO')
```

<img width="791" alt="Screen Shot 2565-09-18 at 22 43 49" src="https://user-images.githubusercontent.com/111941936/190906572-e4b2c3da-47a9-4c4e-9a1f-9afdc8fe5872.png">

## Leap year

Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.

```py
y = int(input())
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('LEAP')
else:
    print('COMMON')
```

<img width="794" alt="Screen Shot 2565-09-18 at 22 52 13" src="https://user-images.githubusercontent.com/111941936/190909931-1f5134da-b71d-4fe3-ab13-73ec60f135d1.png">

## Days in month

Given a month - an integer from 1 (January) to 12 (December), print the number of days in it in the year 2017 (or any other non-leap year).

```py
m = int(input())
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("31")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print("30")
else:
    print("28")
```

<img width="804" alt="Screen Shot 2565-09-18 at 22 55 52" src="https://user-images.githubusercontent.com/111941936/190910584-cc3cf7e1-fc5f-4e70-8f4e-b5d39b7aad37.png">

## Next day

Given the month (an integer from 1 to 12) and the day in it (an integer from 1 to 31) in the year 2017 (or in any other common year), print the month and the day of the next day to it. The first test corresponds to March 30 and March 31. The second test corresponds to March 31 and April 1.

```py
month = int(input())
day = int(input())
if day == 31:
    month = month + 1
    day = 1
elif day == 30:
    if month == 4 or month == 6 or month == 9 or month == 11:
        month = month + 1
        day = 1
    else:
        day = day + 1
elif day == 28:
    month = 3
    day = 1
else:
    day = day + 1

if month > 12:
    month = 1
        
print(month)
print(day)
```

<img width="803" alt="Screen Shot 2565-09-18 at 23 14 03" src="https://user-images.githubusercontent.com/111941936/190911482-111f47bf-bb28-4871-be67-9642e3c40804.png">

## Linear equation

Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

```py
a = int(input())
b = int(input())
if a == 0 and b == 0:
    print('many solutions')
elif a == 0 and b != 0 or b % a != 0:
    print('no solution')
else:
    print(b // a)
```

<img width="793" alt="Screen Shot 2565-09-18 at 23 18 05" src="https://user-images.githubusercontent.com/111941936/190911673-7c3fd4df-3ed5-4088-908b-643dfca87478.png">

## Vertices of rectangle

Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).

```py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1
    
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(x4)
print(y4)
```

<img width="792" alt="Screen Shot 2565-09-18 at 23 28 24" src="https://user-images.githubusercontent.com/111941936/190912171-573bc655-d0f9-4541-9464-96db80cac7f5.png">

## Sort three numbers

Given three integers, print them in ascending order.

```py
a = int(input())
b = int(input())
c = int(input())

if a > b:
    a , b = b , a
    
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a)
print(b)
print(c)
```

<img width="797" alt="Screen Shot 2565-09-19 at 00 17 20" src="https://user-images.githubusercontent.com/111941936/190914500-d88d4f7b-e4c3-4cc9-8611-6e5cbceabe40.png">

## White pawn move

A white chess pawn moves up vertically one square at a time. An exception is a pawn on a row #2: it can move either one or two squares up. In addition, a white chess pawn captures diagonally up one square to the left or right. A white chess pawn can never occur on a row #1.

```py
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if abs(a1 - a2) < 2 and b1 > 1 and b1 < b2:
    if b2 - b1 < 2:
        print("YES")
    elif b1 == 2 and b2 - b1 < 3 and a1 == a2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
```

<img width="792" alt="Screen Shot 2565-09-19 at 09 24 48" src="https://user-images.githubusercontent.com/111941936/190934450-2c0c0113-b533-4a0a-ab24-34d3abcaeb81.png">

# Chapter 4 - For loop with range

## Count to N

Given an integer N, print all the numbers from 1 to N.

```py
n = int(input())
for i in range (1, n+1):
    print(i)
```

<img width="801" alt="Screen Shot 2565-09-19 at 16 42 53" src="https://user-images.githubusercontent.com/111941936/190971160-3715049b-9cc5-42c8-b514-83900217e268.png">

## Series - 1

Given two integers A and B (A ??? B). Print all numbers from A to B inclusively.

```py
a = int(input())
b = int(input())
for i in range(a , b + 1):
    print(i)
```

<img width="801" alt="Screen Shot 2565-09-19 at 18 42 48" src="https://user-images.githubusercontent.com/111941936/190991052-25bdf7bb-2a5a-416f-8481-d44e9b35273f.png">

## First N odd, ascending

Given an integer N, print all the odd numbers from 1 to N in ascending order.

```py
N = int(input())
for i in range(N + 1):
    if i % 2 == 1:
        print(i)
```

<img width="796" alt="Screen Shot 2565-09-19 at 18 48 07" src="https://user-images.githubusercontent.com/111941936/190992092-4cf8d425-5742-4e84-a3e9-b4fa759a155f.png">

## Series - 2

Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ??? B.

```py
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
```        

<img width="800" alt="Screen Shot 2565-09-19 at 19 18 41" src="https://user-images.githubusercontent.com/111941936/190996895-5686f493-1694-4258-8c13-96a9707d67d1.png">

## First N even, descending

Given an integer N, print all the even numbers from 0 to N in descending order.

```py
n = int(input())
if n % 2 == 1:
    n -= 1
for i in range(n, -1, -2):
    print(i)
```

<img width="801" alt="Screen Shot 2565-09-19 at 19 30 16" src="https://user-images.githubusercontent.com/111941936/190998916-933d65f0-ae8d-44f1-8ab3-db8dba840adf.png">

## Sum of ten numbers

10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

```py
sum = 0
for i in range(10):
    sum += int(input())
print(sum)
```

<img width="802" alt="Screen Shot 2565-09-19 at 19 39 41" src="https://user-images.githubusercontent.com/111941936/191000281-7921afd0-e272-44cf-96de-21cd93bbea73.png">

## Sum of N numbers

N numbers are given in the input. Read them and print their sum.

```py
sum=0
n = int(input())
for i in range(n):
    a = int(input())
    sum = sum + a
print(sum)
```

<img width="793" alt="Screen Shot 2565-09-28 at 20 43 45" src="https://user-images.githubusercontent.com/111941936/192770601-c9e3a51f-5462-4c5d-87cd-1ebca4ccb88a.png">


## Product of N numbers

N numbers are given in the input. Read them and print their product.

```py
answer = 1
N = int(input())
for i in range(N):
    a = int(input())
    answer = answer * a
print(answer)
```

<img width="801" alt="Screen Shot 2565-09-28 at 20 46 53" src="https://user-images.githubusercontent.com/111941936/192771109-4b4e2730-f03d-4f35-808d-dee6b19c973e.png">

## Sum of cubes

For the given integer N calculate the following sum

```py
n = int(input())
sum = 0
for i in range(n):
    sum = sum + (i + 1) ** 3
print(sum)
```

<img width="801" alt="Screen Shot 2565-09-30 at 21 59 10" src="https://user-images.githubusercontent.com/111941936/193274927-0908ee81-9e5a-4aca-aafe-db72d505de4f.png">

