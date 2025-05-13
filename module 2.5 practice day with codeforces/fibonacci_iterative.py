def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
test=int(input())
for i in range(test):
    print(fibonacci(i),end=" ")