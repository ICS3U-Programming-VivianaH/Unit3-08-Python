#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: April, 2025
# This program asks the user to enter a year
# and then tells the user if it is a "leap" year.


def main():
    # Ask the user a year
    year_str = input("Enter a year: ")

    try:
        # TryCatch input to an integer
        year = int(year_str)

        # Check if it's a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Leap year")  # It's a leap year
        else:
            print("Not a leap year")  # Not a leap year
    except:
        # The input wasn't a number
        print(year_str, "is not an integer")


if __name__ == "__main__":
    main()
