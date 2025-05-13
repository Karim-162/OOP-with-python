def average(*args):
    size=len(args)
    total=sum(args)
    avg=total/size
    return avg

print(average(10, 20, 30))  # Output: 20.0
