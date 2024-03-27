# Author: Daniel Soden
# Purpose: Python Clinic Booking Project

# Import Statements

from reusable import *

# Named constants

OPENING_HOUR = 9
CLOSING_HOUR = 5

# Lists for storing values

booked_dates = []
booked_times = []

# Clinic Specific Functions

# Main Output


def main():
    running = True

    while running:
        print(
            "a)Schedule an Appointment\n"
            "b)Cancel an Appointment\n"
            "c)View Appointments\n"
            "d)Exit"
        )
        menu_choice = get_non_empty_string(">>>")

        if menu_choice == "a":
            pass

        elif menu_choice == "b":
            pass

        elif menu_choice == "c":
            pass

        elif menu_choice == "d":
            running = False

        else:
            pass


if __name__ == "__main__":
    main()
