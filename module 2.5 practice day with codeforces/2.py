def sum_of_odds(x, y):
    total = 0
    start = min(x, y) + 1
    end = max(x, y)
    
    for i in range(start, end):
        if i % 2 != 0:
            total += i
    return total

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(sum_of_odds(x, y))
