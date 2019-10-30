def best_invitation(first, second):
    topics = {}
    for i in range(0, len(first)):
        if first[i] in topics:
            topics[first[i]] += 1
        else:
            topics[first[i]] = 1
        if second[i] in topics:
            topics[second[i]] += 1
        else:
            topics[second[i]] = 1
    
    res = 0
    for val in topics.values():
        if res < val:
            res = val
    return res

# Example 0
# first = ['fishing', 'gardening', 'swimming', 'fishing']
# second = ['hunting', 'fishing', 'fishing', 'biting']

# Example 1
# first = ['variety', 'diversity', 'loquacity', 'countesy']
# second = ['talking', 'speaking', 'discussion', 'meeting']

# Example 2
first = ['snakes', 'programing', 'cobra', 'monty']
second = ['python', 'python', 'anaconda', 'python']

print(best_invitation(first, second))
