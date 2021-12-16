#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 16, 2021
# This program gets the user to enter a year.
# It then tells the user if that year is a leap year.


def main():

    # get user input
    year_string = input("Enter the year: ")

    # error checking
    try:
        year = int(year_string)
    except Exception:
        print("Invalid input, must be an integer.")
        quit()

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


if __name__ == "__main__":
    main()
