import random


def are_duplicates(nums):
    for x in nums:
        for y in nums[x + 1:]:
            if y == x:
                return True
    return False


def run_it():
    input(int("How many times do you want to run the simulation?"))

def main():
    birthdays = []
    for x in range(23):
        number = random.randint(1, 365)
        birthdays.append(number)
    print(birthdays)
    print(are_duplicates(birthdays))


main()
