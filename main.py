# Jaden Russell
# 11/16/2022
# SDEV 300

"""This program loads the user specified file data and displays the
statistics of the user specified variable from the file """
import statistics
import pandas as pd
import matplotlib.pyplot as plt


def show_stats(col_var):
    """Prints the statistical data of the specified column variable"""
    print("The statistics for this column are:")
    print(f"Count: {len(col_var)}")
    print(f"Mean: {col_var.mean()}")
    print(f"Standard Deviation: {statistics.stdev(col_var)}")
    print(f"Max: {col_var.max()}")
    print(f"Min: {col_var.min()}")

    plt.figure(figsize=(7, 3))
    plt.hist(col_var, bins='auto')
    plt.show()


def h_analysis():
    """Creates a menu to choose the column for housing analysis"""
    pop_data = pd.read_csv("Housing.csv")
    print("You have entered housing data.")
    column = ' '

    while column not in 'f':
        print("Select the column you want analyze:")
        print("a. House Age\nb. Bedrooms\nc. Year Built\nd. Rooms\ne. Utility Costs")
        print("f. Exit Column")
        column = input()
        if column == 'a':
            show_stats(pop_data["AGE"])
        elif column == 'b':
            show_stats(pop_data["BEDROOMS"])
        elif column == 'c':
            show_stats(pop_data["BUILT"])
        elif column == 'd':
            show_stats(pop_data["ROOMS"])
        elif column == 'e':
            show_stats(pop_data["UTILITY"])
        elif column == 'f':
            print("Exiting...")
        else:
            print("The value you entered was invalid, please re-enter.")


def p_analysis():
    """Creates a menu to choose the column for population analysis"""
    pop_data = pd.read_csv("PopChange.csv")
    print("You have entered population data.")
    column = ' '

    while column not in 'd':
        print("Select the column you want analyze:")
        print("a. Pop Apr 1\nb. Pop Jul 1\nc. Change Pop\nd. Exit Column")
        column = input()
        if column == 'a':
            show_stats(pop_data["Pop Apr 1"])
        elif column == 'b':
            show_stats(pop_data["Pop Jul 1"])
        elif column == 'c':
            show_stats(pop_data["Change Pop"])
        elif column == 'd':
            print("Exiting...")
        else:
            print("The value you entered was invalid, please re-enter.")


def main():
    """Defines the code of the program in main"""
    print(f"{'Welcome to the Python Data Analysis Program':*^100}")
    choice = 0

    while choice != 3:
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")
        try:
            choice = int(input())
        except ValueError:
            print("The value you entered is invalid, please re-enter.")

        if choice == 1:
            p_analysis()
        elif choice == 2:
            h_analysis()
        elif choice < 1 or choice > 3:
            print("The value you entered is invalid, please re-enter.")

    print(f"{'Thank you for using the Python Data Analysis Program':*^100}")


main()
