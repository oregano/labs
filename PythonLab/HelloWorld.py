def AddUp(*args):
    result = 0
    for a in args:
        result = result + a
    return result


print(AddUp(2, 3, 4))
