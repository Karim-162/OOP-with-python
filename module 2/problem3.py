def multiply_all(*args):
    count=1
    for i in args:
        count*=i
    return count

print(multiply_all(2, 3, 4))  # Output: 24
