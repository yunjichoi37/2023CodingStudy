n = input()
if "0" not in n:
    print(-1)
else:
    sum =0
    for i in range(len(n)):
        sum += int(n[i])
        
    if sum % 3 != 0 :
        print(-1)
        
    else:
        sorting_num = sorted(n, reverse=True)
        answer = "".join(sorting_num)
        print(answer)