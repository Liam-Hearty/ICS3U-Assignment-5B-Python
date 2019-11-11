#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program adds only positive numbers.


def main():
    # This program adds only positive numbers.

    answer = 0

    # input, process & output in loop
    try:
        number_of_sides = int(input("How many sides does your shape have: "))
        if number_of_sides <= 2:
            print("A shape can not have less than 3 sides.")
            exit()
        for loop_counter in range(number_of_sides):
            chosen_number = int(input("Enter a side length: "))
            # Process
            loop_counter += 1
            if chosen_number < 0:
                print("That number was 0 or less, try program again.")
                exit()
            else:
                # Output
                answer = answer + chosen_number
                continue
        print("{0}".format(answer))
    except(ValueError):
        print("Please input a whole number.")


if __name__ == "__main__":
    main()
