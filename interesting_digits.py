def digits(base):
    res = []
    for i in range(2, base):
        if ((base - 1) % i == 0):
            res.append(i)
    return res

# Example 0
base = 10

# Example 1
# base = 3

# Example 2
# base = 9

# Example 3
# base = 26

# Example 4
base = 30

print(digits(base))
