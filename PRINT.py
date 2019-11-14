#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: November 2019
# This program ask for string and prints it


def main():
    # This program ask for string and prints it
    user_number_str = input("Howmany times you want to repeat the string: \
(integer) ")
    try:
        user_string = input("Enter a string: ")
        user_number = int(user_number_str)
        if user_number > 0:
            print(((user_string+"")*user_number, "{}".
                  format(user_number)),
                  "Return time is:{}".format(user_number))
        else:
            print("I dont know")
    except Exception:
        print("sorry invalid integer")


if __name__ == "__main__":
    main()
