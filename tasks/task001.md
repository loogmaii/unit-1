# Task 1

Save your program in a file called task1.md. In a school there are 2400 students and each student uses one locker. Each locker has a unique number from 1 to 2400. The lockers are to be painted in four colors: red, white, yellow and blue, in order of locker numbers, as shown in the following table.link

Task 1: Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400

Task 2: Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.

[HL] Task 3: Create a program that receives a color from the user, validates the input,  and outputs the numbers of the lockers of the color provided. Use at least 10 different functions for Manipulating Strings (Learning Log Item 19)

[HL] Task 4: Given a list of names of students in the format lastname, firstname, create a program that assigns an email address and a locker to each student and saves the results in a file in the format lastname, firstname, email, locker 

## code

```py
# Produce locker numbers
number_lockers = 2400
# generate a sequence
for locker in range(1, number_lockers, 1):
    # create the sequence
    color_code = locker % 4
    if color_code == 0:
        color = "blue"
    if color_code == 1:
        color = "red"
    if color_code == 2:
        color = "white"
    if color_code == 3:
        color = "yellow"
    # more efficient way
    colors = ["blue", "red", "white", "yellow"]
    color = colors[color_code]
    # print the results
    print(f"Locker No {locker} is {color.center(50, '.')} ")
```

## evidence

<img width="579" alt="Screen Shot 2565-10-10 at 05 59 39" src="https://user-images.githubusercontent.com/111941936/194779225-6ad45af2-e191-4c84-a78f-82a0247c9900.png">
