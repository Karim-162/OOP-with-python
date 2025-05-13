def count_odd(*args):
    count=0
    for i in args:
        if i%2!=0:
            count+=1
    return count



print(count_odd(1, 2, 5, 6, 9))  # Output: 3
