import sys
cal = input().split('-')
result = []
for i in cal:
    temp=0
    plus = i.split('+')
    for j in plus:
        temp +=int(j)
    result.append(temp)
first = result[0]
for k in range(1,len(result)):
    first -=result[k]
print(first)
    
        