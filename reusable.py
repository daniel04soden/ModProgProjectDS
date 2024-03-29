# Author: Daniel Soden
# Purpose: Useful functions

# Any needed import statements

# Non empty string


def get_non_empty_string(prompt: str) -> str:
    """
    This function takes a string from a user but ensures
    it is not empty

    :param: prompt: flexible prompt to be used by developer (str)

    :returns: user_input(str): returns string inputted by the user
    """
    while True:
        user_input = input(prompt)
        if len(user_input) > 0:
            break
        else:
            print("Please enter a valid value.")

    return user_input


# Get a positive integer


def get_positive_integer(prompt: str) -> int:
    """
    This function takes an integer from the user and ensures it is
    positive, an integer and has a length greater than 0

    :param: prompt: flexible prompt to be used by developer (str)

    :returns: user_input(int): returns the integer inputted by the user
    """

    while True:
        try:
            user_input = int(input(prompt))

            if user_input > 0 and len(str(user_input)) > 0:
                break
            else:
                print("Please enter a positive value")
        except ValueError:
            print("Please only enter whole numbers")
    return user_input


# Get a number in range


def get_number_range(minimum=1, maximum=100) -> int:
    """
    This function takes 2 integers from the user and uses these
    numbers to create a range and ensures the user doesn't go out
    of this range

    :param: minimum: minimum value for the range (int)
            maximum: maximum value for the range (int)

    :returns: None, just stores an integer
    """

    while True:
        try:
            user_num = int(
                input(f"Give me a number between {minimum} and {maximum}:  ")
            )
            if minimum <= user_num <= maximum:
                break
            else:
                print("You must enter a number in the range provided")
        except ValueError:
            print("Hey! Enter a number silly")
    return user_num


# Get a positive float


def get_positive_float(prompt) -> float:
    """
    This function takes a float from the user and ensures it is
    positive and has a length greater than 0

    :param: prompt: flexible prompt to be used by developer (str)

    :returns: user_input(float): returns the float inputted by the user
    """

    while True:
        try:
            user_input = float(input(prompt))

            if user_input > 0 and len(str(user_input)) > 0:
                break
            else:
                print("Please enter a positive value")
        except ValueError:
            print("Please only enter numbers")
    return user_input


# Print a list with its index


def print_list_index(user_list: list) -> None:
    """
    This function takes a list from a user
    and iterates through this list and assigns an index to each
    iterative value

    :param: user_list: list providedby the user to iterate over

    returns: None, just prints index and value
    """
    for i, item in enumerate(user_list):
        print(f"Index:{i} Value:{item}")


# Ensuring number length is valid
def validate_number(prompt: str) -> str:
    """This function takes the length the user wants the string to be and
        prompts the user to enter their Irish Phone number

    :param: prompt: prompt provided for code reusability

    returns: resulting_variable
    """
    phone_length = 10
    resulting_variable = input(prompt)
    while not len(resulting_variable) == phone_length:
        print("Invalid input Please try again")
        resulting_variable = input(prompt)
    else:
        return resulting_variable


# Full Name Validation


def validate_name(prompt: str) -> str:
    """This function takes the length the user wants the string to be and
    a prompt in order to restrict the user input

    :param: prompt: prompt provided for code reusability

    returns: resulting_variable
    """
    user_limit = 20
    resulting_variable = input(prompt)
    while not 1 <= len(resulting_variable) <= user_limit:
        print("Invalid input Please try again")
        resulting_variable = input(prompt)
    else:
        return resulting_variable


# Deleting lines from a file


def delete_line(filename: str, line_number: int):
    """This function reads the file given by the user and
    deletes a specified line by rewriting a new file
    without that line

    :param:
            filename: string referencing the name of the file
            line_number: number to focus on the line user is Deleting

    :returns: None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()

    if line_number <= len(lines):
        del lines[line_number - 1]

        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Not found in file")


# Testing of functions


def main():
    number = get_positive_integer("Please enter a number  ")
    print(number)
    my_num = get_number_range()
    print(my_num)
    get_positive_float("Please enter a number:  ")


if __name__ == "__main__":
    main()
