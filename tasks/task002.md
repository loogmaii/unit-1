# Task 2: EV Calculator

Complete the program for the EV calculator

------ Welcome to EV Calculator-------
                     Options                      
1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data

Data (charging_log.csv):

date,charge,duration

12.9.22,8.878kWh,12:32:36

15.9.22,3.533kWh,5:02:23

17.9.22,6.828kWh,9:41:46

18.9.22,5.425kWh,7:43:35

## code

```py
from my_library import validate_int_input, end_code, colors

welcome_msg = "Welcome to the EV Calculator".center(50, "=")
prompt_msg = "Please enter an option [1-4]: "

print(f"{colors[2]}{welcome_msg}{end_code}")
print("Options".center(50))

with open("charging_log.csv", "r") as file:
    ev_logs = file.readlines()

menu = """
1. Average time per kWh
2. Total kWh
3. Total charge time
4. Show all data
"""
print(menu)
option = validate_int_input(prompt_msg)
while option>4 or option < 1:
    option = validate_int_input(f"{colors[1]}Invalid option. {prompt_msg}{end_code}")

# Option 1: Average time per kWh
if option == 1:
        total_time = 0
        total_kwh = 0.0
        i = 0

        for line in ev_logs:
            if i > 0:
                data = line.split(",")
                #print(data)
                time = data[1]
                time_cleaned = time[:5]
                time_float = float(time_cleaned)
                total_kwh += time_float
                total_kwh = time_float

                temp_time = data[2]
                temp_time = temp_time.split(":")
                temp_time = int(temp_time[0]) * 60 + int(temp_time[1])
                total_time += temp_time

            i += 1

        print(
            f"{colors[5]}Average time per kWh: {int(total_time / total_kwh)} minutes{end_code}")

# option 2: Calculate total energy
if option == 2:
    index = 0
    total_energy = 0
    for log in ev_logs:
        if index > 0:
            values = log.split(",")
            date = values[0]
            energy = values[1]
            time = values[2]
            total_energy += float(energy[0:5])
        index += 1
    print(f"{colors[2]}The total energy charged is {total_energy}kWh")

# option 3: Total charge time
if option == 3:
        total_time = 0
        i = 0
        for line in ev_logs:
            if i > 0:
                data = line.split(",")
                time = data[2]
                time = time.split(":")
                time = int(time[0]) * 60 + int(time[1])
                total_time += time
            i += 1
        print(f"{colors[3]}Total charge time= {total_time} minutes{end_code}")

# option 4: show all data
if option == 4:
    print(f"{colors[2]}4. Showing all data{end_code}")
    index = 0
    for log in ev_logs:
        if index > 0:
            print(f"{colors[6]}No.{index}: {log}", end="") # strip removes the \n at the end of the line
        index += 1
```

## my_library

```py
colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m",
          "\033[0;37m", "\033[0;38m", "\033[0;39m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m",
          "\033[0;44m", "\033[0;45m", "\033[0;46m", "\033[0;47m", "\033[0;48m", "\033[0;49m", "\033[0;50m",
          "\033[0;51m", "\033[0;52m", "\033[0;53m", "\033[0;54m", "\033[0;55m", "\033[0;56m", "\033[0;57m",
          "\033[0;58m", "\033[0;59m", "\033[0;60m", "\033[0;61m", "\033[0;62m", "\033[0;63m", "\033[0;64m",
          "\033[0;65m", "\033[0;66m", "\033[0;67m", "\033[0;68m", "\033[0;69m", "\033[0;70m", "\033[0;71m",
          "\033[0;72m", "\033[0;73m", "\033[0;74m", "\033[0;75m", "\033[0;76m", "\033[0;77m", "\033[0;78m",
          "\033[0;79m", "\033[0;80m", "\033[0;81m", "\033[0;82m", "\033[0;83m", "\033[0;84m", "\033[0;85m",
          "\033[0;86m", "\033[0;87m", "\033[0;88m", "\033[0;89m", "\033[0;90m", "\033[0;91m", "\033[0;92m"]
end_code = "\033[00m"
def validate_int_input(msg:str)->int:
    '''This function validates that the user enters a integer'''
    end_code = "\003[00m"
    red = "\003[0;31m"
    number = input(msg)
    while not number.isdigit():
        number = input(f"Error. {msg}")

    return int(number)
```

## results

<img width="579" alt="Screen Shot 2565-10-10 at 06 22 18" src="https://user-images.githubusercontent.com/111941936/194779995-643ff469-ae1f-4084-8c1a-6219e3a67ba0.png">

fig.1 shows results of "option 1" of the program

<img width="579" alt="Screen Shot 2565-10-10 at 06 22 41" src="https://user-images.githubusercontent.com/111941936/194780014-b1665227-5441-407c-8e04-0e576ae5f0ed.png">

fig.2 shows results of "option 2" of the program

<img width="579" alt="Screen Shot 2565-10-10 at 06 23 03" src="https://user-images.githubusercontent.com/111941936/194780029-55b90f4e-9d8f-453b-a8b3-cbd15ff4af30.png">

fig.3 shows results of "option 3" of the program

<img width="577" alt="Screen Shot 2565-10-10 at 06 24 35" src="https://user-images.githubusercontent.com/111941936/194780109-748fb0f5-2746-4112-b83f-4a899d69f909.png">

fig.4 shows results of "option 4" of the program
