# by Xander Eagle
# November 6, 2019
# this program displays the Birthday Paradox showing the percent of people that have the sme birthday based on the
# amount of simulations

import random


def are_duplicates(nums):
    """finds the duplicates
        :return: true if there is a duplicate
        false if no duplicate
        """
    for x in nums:
        for y in nums[x + 1:]:
            if y == x:
                return True
    return False


def run_it():
    """
        ask the user to input the number of simulations
        :return: the number of simulations
        """
    return int(input("How many times do you want to run the simulation?"))


def main():
    """
        tracks the variables and finds 23 random numbers out of 365
        :return: the amount of duplicate birthdays along with the percentage
        """
    track_variables = 0
    num_times = run_it()
    for nums in range(num_times):
        birthdays = []
        for x in range(23):
            number = random.randint(1, 365)
            birthdays.append(number)
        if are_duplicates(birthdays):
            track_variables += 1
    percent_total = track_variables / num_times * 100
    print("There were duplicate birthdays", track_variables, "times. That means two people had the same birthday",
          percent_total, "percent of the time.")


main()
