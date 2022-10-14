def login(user:str, password:str)->bool:
    '''
    Function for simple user login
    needs db.csv
    :param user:
    :param password:
    :return:
    '''
    with open("db.csv", "r") as file:
        database = file.readlines()
    output = False
    for line in database: # every user
        # get rid of \n
        clear_line = line.strip()
        separated_line = clear_line.split(",")
        if user == separated_line[0] and password == separated_line[1]:
            output = True

    return output
