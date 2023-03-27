import sys
n=int(sys.stdin.readline())
member=list(map(int,sys.stdin.readline().split()))
b,c=map(int,sys.stdin.readline().split())
n=0
# 각 교실 마다 
for mem in member:
    # 총감독
  remain=mem-b
  n+=1
  # 부감독
  if remain>0:
    re=remain//c
    n+=re
    if remain != re*c:
      n+=1

print(n)