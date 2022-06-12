#!/usr/bin/env python3

# Created by: Dahrio-Francois
# Created on: June 2022
# This code calculates the area of a cylinder
# using functions


def calculate_cylinder_volume(radius, height):
    # this calculates the area

    import math

    # process

    volume_of_cylinder = math.pi * radius**2 * height

    # output

    return volume_of_cylinder


def main():
    # this function collects the radius & height

    try:
        # input

        radius_from_user = int(input("Enter in the radius of the cylinder (mm): "))

        height_from_user = int(input("\nEnter in the height of the cylinder (mm): "))

        # call function
        some_var = calculate_cylinder_volume(radius_from_user, height_from_user)

        # process & output

        print(
            "\nThe volume of a cylinder with those two integers are {0:.2f} mm²".format(
                some_var
            )
        )
    except Exception:
        print("\nThat was not a valid integer, please input them correctly.")


if __name__ == "__main__":
    main()
