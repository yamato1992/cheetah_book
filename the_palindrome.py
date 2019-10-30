def find(s):
    length = len(s)
    r = s[::-1]
    for i in range(0, len(s)):
        if r == s:
            return i + length
        s = s[1:]
        r = r[:-1]

# Example 0
# s = 'abab'

# Example 1
# s = 'abacaba'

# Example 2
# s = 'qwerty'

# Example 3
# s = 'abdfhdyrbdbsdfghjkllkjhgfds'

print(find(s))
