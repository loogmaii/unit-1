# Chapter 1 - Input, print and numbers

## Sum of three numbers

Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

```.py
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

Image of the results

<img width="806" alt="Screen Shot 2565-09-01 at 20 58 00" src="https://user-images.githubusercontent.com/111941936/187908669-1c9892ce-6dd5-4b0b-aab9-6b89647a5313.png">

## Hi John

Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.

```.py
print('Hi',input())
```

Image of the results

<img width="795" alt="Screen Shot 2565-09-01 at 21 05 30" src="https://user-images.githubusercontent.com/111941936/187919470-8f3ac8df-53fe-40c4-af90-d7b1a7b166f1.png">

## Square

Write a program that takes a number and print its square.

```.py
a = int(input())
print(a ** 2)
```

Image of the results

<img width="803" alt="Screen Shot 2565-09-01 at 22 19 37" src="https://user-images.githubusercontent.com/111941936/187924090-405abebb-4617-4bd2-9379-238cc7189f69.png">

## Area of right-angled triangle

Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.

```.py
b = int(input())
h = int(input())
print(1/2 * b * h)
```

Image of the results

<img width="799" alt="Screen Shot 2565-09-01 at 22 25 22" src="https://user-images.githubusercontent.com/111941936/187926218-801baef4-5434-4fd1-b213-7ce13611ad8b.png">

## Hello, Harry!

Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. 

```.py
name = input()
print('Hello'+ ', ' + name + '!')
```

Image of the results

<img width="799" alt="Screen Shot 2565-09-01 at 22 37 31" src="https://user-images.githubusercontent.com/111941936/187927945-9477d191-f83f-40f9-81f0-efa6ddc30bba.png">

## Apple sharing

N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

```.py
n = int(input())
k = int(input())
print(k // n)
print(k % n)
```
Image of the results

<img width="800" alt="Screen Shot 2565-09-01 at 22 48 15" src="https://user-images.githubusercontent.com/111941936/187930481-dbdaa989-e9d3-4662-8e7b-604b5b0e174e.png">

## Previous and next

Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

```.py
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')
```

Image of the results

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

Image of the results

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

Image of the results

<img width="798" alt="Screen Shot 2565-09-04 at 21 23 25" src="https://user-images.githubusercontent.com/111941936/188313333-3fda4422-3def-47d9-860e-a88dd7a02eed.png">

# Chapter 2 - Integer and float numbers

## Last digit of integer

Given an integer number, print its last digit.

```py
a = int(input())
print(a % 10)
```

Image of the results

<img width="794" alt="Screen Shot 2565-09-04 at 21 53 35" src="https://user-images.githubusercontent.com/111941936/188314518-ea0b9e91-f567-4579-a07d-3a7d30a12418.png">

## Two digits

Given a two-digit number, print its digits separately.

```py
a = int(input())
print(a//10, a%10)
```

Image of the results

<img width="787" alt="Screen Shot 2565-09-04 at 21 56 38" src="https://user-images.githubusercontent.com/111941936/188314676-4538148b-7e85-4eb0-a79c-84446402770d.png">

## Swap digits

Given a two-digit number, swap its digits as shown in the tests below.

```py
a = int(input())
tens = a // 10
units = a % 10
print(units * 10 + tens)
```

Image of the results

<img width="791" alt="Screen Shot 2565-09-04 at 22 02 06" src="https://user-images.githubusercontent.com/111941936/188314887-0a1f8821-db64-4dc3-8fc8-2ff0d15ad675.png">

## Last two digits

Given an integer number, print its last two digits.

```py
a = int(input())
print(a % 100)
```

Image of the results

<img width="790" alt="Screen Shot 2565-09-04 at 22 08 15" src="https://user-images.githubusercontent.com/111941936/188315162-174b6ae3-c53c-49c7-962b-fb0709d8b703.png">

## Tens digit

Given an integer. Print its tens digit.

```py
a = int(input())
print(a // 10 % 10) 
```

Image of the results

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

Image of the results

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

Image of the results

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

Image of the results

<img width="782" alt="Screen Shot 2565-09-05 at 10 07 04 1" src="https://user-images.githubusercontent.com/111941936/188341689-785a345d-33b5-4b1f-8ba0-0cbe1c360cd6.png">

## Cyclic rotation

Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below.

```py
a = int(input())
print(a % 100 * 100 + a // 100)
```

Image of the results

<img width="784" alt="Screen Shot 2565-09-05 at 11 11 40" src="https://user-images.githubusercontent.com/111941936/188346663-1aec7379-21b7-4ebb-a359-5d33a9ec3717.png">

## Fractional part

Given a positive real number, print its fractional part.

```py
a = float(input())
print(a - int(a))
```

Image of the results

<img width="796" alt="Screen Shot 2565-09-05 at 11 19 18" src="https://user-images.githubusercontent.com/111941936/188348439-10d8fa2f-1daa-4aff-b741-2e407b804c6b.png">

## First digit after decimal point

Given a positive real number, print its first digit to the right of the decimal point.

```py
a = float(input())
b = a * 10
print(int(b) % 10)
```
Image of the results

<img width="781" alt="Screen Shot 2565-09-05 at 11 25 34" src="https://user-images.githubusercontent.com/111941936/188349053-25b61876-ed3f-4de6-af7a-c5f8a724b298.png">

## Car route

A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

```py
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
```

Image of the results

<img width="789" alt="Screen Shot 2565-09-06 at 19 29 21" src="https://user-images.githubusercontent.com/111941936/188613136-f6e96caf-6dd7-4254-bb0c-8d66ba96cab6.png">

## Day of week

Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday.

```py
k = int(input())
print((k + 3) % 7)
```

Image of the results

<img width="778" alt="Screen Shot 2565-09-07 at 20 08 52" src="https://user-images.githubusercontent.com/111941936/188864205-d33243df-60d1-4bc4-a29f-5aef23877d7f.png">
