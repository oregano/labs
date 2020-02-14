s = 'abcdedfgh'

# slice first 2 characters
print('First 2 characters of {st} are {ch}'.format(st=s, ch=s[0:2]))
print('First 2 characters of {st} are {ch}'.format(st=s, ch=s[:2]))

# slice last 2 characters
print('last 2 characters of {st} are {ch}'.format(st=s, ch=s[-2:]))
print('last 2 characters of {st} are {ch}'.format(st=s, ch=s[-2:]))

# alternate characters
print(s[::2])

# alternate characters(reverse)
print(s[::-2])

# reverse a string
print(s[::-1])