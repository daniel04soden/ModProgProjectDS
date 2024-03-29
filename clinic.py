# Author: Daniel Soden
# Purpose: Python Clinic Booking Project

# Import Statements

from reusable import get_non_empty_string, validate_name, validate_number, delete_line

# Named constants

OPENING_HOUR = 9
CLOSING_HOUR = 5

# Lists for storing values

booked_names = []
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
    booked_names.append(name)
    contact_number = validate_number("Enter your Phone number:  ")

    # Date of appointment input for the user

    # Input validation such as time validation and date validation to be added

    appointment_date = get_non_empty_string(
        "Enter the preferred date of your appointment:  "
    )
    appointment_time = get_non_empty_string(
        f"Enter the time you would like your appointment on {appointment_date}:  "
    )
    booked_dates.append(appointment_date)
    booked_times.append(appointment_time)

    store_patient_data(name, contact_number, appointment_date, appointment_time)
    print(
        f"Appointment for {name} booked at {appointment_time} on the date {appointment_date}"
    )


def cancel_appointment() -> None:
    print(
        "Before we can cancel your appointment we will need to identify you in our system"
    )
    name = validate_name("Enter your Name:  ")
    date = get_non_empty_string("Enter the date of your booking:  ")
    with open("patient_data.txt", "r+") as patient_info:
        i = 0
        for values in patient_info:
            values = values.split(",")
            i += 1
            if values[0] == name and values[2] == date:
                delete_line("patient_data.txt", i)
                print(
                    f"Sucessfully cancelled appointment for {name}\n on the date {date}"
                )

            else:
                print(f"{name} cannot be found at date {date}")


def view_appointments() -> None:
    while True:
        choice = get_non_empty_string(
            "Would you like to view appointments by name or by date?(N/d)  "
        ).lower()

        if choice == "d":
            date = get_non_empty_string("Enter your date of booking:  ")
            with open("patient_data.txt") as patient_info:
                for values in patient_info:
                    values = values.split(",")
                    if values[2] == date:
                        date_index = booked_dates.index(date)
                        print(f"{date} booked for {booked_names[date_index]}")
                    else:
                        pass

            break

        elif choice == "n":
            name = validate_name("Enter your Name:  ")
            with open("patient_data.txt") as patient_info:
                for values in patient_info:
                    values = values.split(",")
                    if values[0] == name:
                        name_index = booked_names.index(name)
                        print(f"{name} is booked in for {booked_dates[name_index]}")
                    else:
                        pass
            break

    else:
        print("Please choose Name or date as a method of viewing.")


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
            cancel_appointment()

        elif menu_choice == "c":
            view_appointments()

        elif menu_choice == "d":
            running = False

        else:
            print("Please select a relevant option")
            pass


if __name__ == "__main__":
    main()
