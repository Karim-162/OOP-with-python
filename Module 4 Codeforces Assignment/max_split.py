string=input()
balance=0
count=0
result=[]
temp=''
for ch in string:
    temp+=ch
    if ch=='R':
        balance+=1
    else:
        balance-=1
    if balance == 0:
        count+=1
        result.append(temp)
        temp=''
print(count)
for item in result:
    print(item)