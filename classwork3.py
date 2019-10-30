def add_numbers(nums):
    total = 0
    for x in nums:
        total = x + total
    return total


print(add_numbers([9, 5, 11, 6, 1, 15]), "is the total sum of the list")
