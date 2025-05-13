def find_max(*args):
    max=args[0]
    for i in args:
        if i>max:
            max=i
    return max

print(find_max(10, 5, 22, 13))  # Output: 22
