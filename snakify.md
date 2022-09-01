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
