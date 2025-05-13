def split_even_odd(*args):
    even=[]
    odd=[]
    for i in args:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

print(split_even_odd(1, 2, 3, 4, 5))  # Output: ([2, 4], [1, 3, 5])
