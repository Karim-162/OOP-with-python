def positive_numbers(*args):
    pos=[]
    for i in args:
        if i>0:
            pos.append(i)
    return pos

print(positive_numbers(-2, 0, 5, -3, 7))  # Output: [5, 7]
