def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
total=sum(1,2,3)
print(total)