import pyautogui
import time

n = int(input())

print("running")
time.sleep(3)

# পিরামিড আঁকা
# for i in range(1, n + 1):
#     spaces = ' ' * (n - i)
#     stars = '*' * (2 * i - 1)
#     line = spaces + stars
#     pyautogui.typewrite(line)
#     pyautogui.press("enter")
    
for i in range(1,n+1):
    for j in range(i):
        print("#",end="")
    print()