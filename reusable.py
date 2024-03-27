# Author: Daniel Soden
# Purpose: Useful functions

# Non-empty string

def get_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0:
            return user_input
        else:
            print("Please enter a valid value.")


# Get a positive integer

def get_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))

            if user_input > 0:
                break
            else:
                print("Please enter a positive value")
        except ValueError:
            print("Please only enter whole numbers")
    return user_input


# Get a number in range

def get_number_range(minimum=1, maximum=100):
    while True:
        try:
            user_num = int(input(F"Give me a number between {minimum} and {maximum}:  "))
            if minimum <= user_num <= maximum:
                break
            else:
                print("You must enter a number in the range provided")
        except ValueError:
            print("Hey! Enter a number silly")
    return user_num


# Get a positive float

def get_positive_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))

            if user_input > 0:
                break
            else:
                print("Please enter a positive value")
        except ValueError:
            print("Please only enter numbers")
    return user_input

# Print a list with its index

def print_list_index(user_list:list):
    
    for i,item in enumerate(user_list):
        
        print(f"Index:{i} Value:{item}")

# Reading any file

def read_file(file_name:str,seperator:str):

    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            line = line.split(seperator)

# Testing of functions

def main():
    number = get_positive_integer("Please enter a number  ")
    print(number)
    my_num = get_number_range()
    print(my_num)
    get_positive_float("Please enter a number:  ")
    read_file("namepass.txt")

if __name__ == "__main__":
    main()

# !
# ?
# //
# * so bright so epic
