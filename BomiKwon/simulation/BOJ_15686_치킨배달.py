# 조합마다 /치킨 집마다/ 집에 대한 최소거리를 구하는 과정이 좀 헷갈렸음
# 다음부턴 한 조건에 대해서 먼저 코드 짜고 반복문에 넣기

import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
array=[]
for _ in range(n):
  array.append(list(map(int,sys.stdin.readline().split())))

# 집의 좌표를 저장
house=[]

# 치킨의 좌표를 저장
chicken=[]
for i in range(n):
  for j in range(n):
    if array[i][j]==1:
      house.append([i,j])
    elif array[i][j]==2:
      chicken.append([i,j])
      
# 도시치킨거리를 저장
all_dist=[]
while(True):
  if m==0:
    break
  # m개씩 조합을 만들어서 살릴 치킨 집 선정
  for chic in list(combinations(chicken,m)):
    # 치킨거리를 저장하는 배열
    chic_dist=[]
    for home in house: 
      mind=1e9
      for i in chic:
        dist=abs(home[0]-i[0])+abs(home[1]-i[1])
        if mind>dist:
          mind=dist
      # 각 집마다 치킨거리를 저장
      chic_dist.append(mind)
    # 각 조합마다 도시치킨 거리를 저장
    all_dist.append(sum(chic_dist))
  m-=1

print(min(all_dist))