#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: oct 2021
# this program finds the surface area of a cube


def surface_area_cube(user_input_length):
    # this function finds the surface area of a cube

    # process
    cube_sa = 6 * (user_input_length * user_input_length)

    return cube_sa


def main():
    # this function gets user_input_length

    # input
    user_input_length_string = input("Enter the length of the cube (cm): ")

    # process
    try:
        user_input_length = float(user_input_length_string)
        # call function
        surface_area_cube_value = surface_area_cube(user_input_length)
        if user_input_length < 0:
            print("\nPlease enter a positive number.")
        else:
            print(
                "\nThe surface area of the cube would be {} cm²".format(
                    surface_area_cube_value
                )
            )
    except Exception:
        print("\n{} is an invalid input.".format(user_input_length_string))
    print("\nDone")


if __name__ == "__main__":
    main()
