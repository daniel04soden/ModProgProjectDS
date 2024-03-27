# Author: Daniel Soden
# Purpose: Python Clinic Booking Project

# Import Statements

from reusable import get_non_empty_string, validate_name, validate_number

# Named constants

OPENING_HOUR = 9
CLOSING_HOUR = 5

# Lists for storing values

booked_dates = []
booked_times = []

# Clinic Specific Functions


def store_patient_data(
    name: str, contact_number: str, appointment_date: str, appointment_time: str
):
    with open("patient_data.txt", "a") as patient_info:
        print(
            f"{name},{contact_number},{appointment_date},{appointment_time}",
            file=patient_info,
        )


def schedule_appointment() -> None:
    # Name and Number input for the user
    name = validate_name("Enter your Name:  ")
    contact_number = validate_number("Enter your Phone number:  ")

    # Date of appointment input for the user

    # Input validation such as time validation and date validation to be added

    appointment_date = get_non_empty_string(
        "Enter the preferred date of your appointment:  "
    )
    appointment_time = get_non_empty_string(
        f"Enter the time you would like your appointment on {appointment_date}"
    )
    booked_dates.append(appointment_date)
    booked_times.append(appointment_time)

    store_patient_data(name, contact_number, appointment_date, appointment_time)
    print(
        f"Appointment for {name} booked at {appointment_time} on the date {appointment_date}"
    )


def cancel_appointment():
    pass


def view_appointments():
    pass


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
            schedule_appointment()

        elif menu_choice == "b":
            pass

        elif menu_choice == "c":
            pass

        elif menu_choice == "d":
            running = False

        else:
            print("Please select a relevant option")
            pass


if __name__ == "__main__":
    main()
