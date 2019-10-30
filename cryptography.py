def encrypt(numbers):
    numbers.sort()
    numbers[0] += 1
    res = 1
    for num in numbers:
        res *= num
    return res

# Example 1
# numbers = [1, 2, 3]

# Exanmple 2
# numbers = [1, 3, 2, 1, 1, 3]

# Example 3
# numbers = [1000, 999, 998, 997, 996, 995]

# Example 4
numbers = [1, 1, 1, 1]

print(encrypt(numbers))