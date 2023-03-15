# 삼성sw역량테스트 기출 문제 02 - 연구소
# 0315

from itertools import combinations 
from collections import deque
import copy
n,m=map(int,input().split())
array=[]
for i in range(n):
  array.append(list(map(int,input().split())))
empty=[]
virus=[]
for i in range(n):
  for j in range(m):
    if array[i][j]==0:
      empty.append([i,j])
    if array[i][j]==2:
      virus.append([i,j])
      
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
  cnt=0
  queue=deque()
  # 바이러스이 위치에서 퍼져나간다
  for i in virus:
    queue.append(i)
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
      if arraycopy[nx][ny]==0:
        queue.append([nx,ny])
        arraycopy[nx][ny]=1
    # 탐색 마친 뒤에 빈 공간을 카운트
  for i in range(n):
    for j in range(m):
      if arraycopy[i][j]==0:
        cnt+=1
  return cnt
  
# 벽을 세울 수 있는 경우의 수
install=list(combinations(empty,3))

result=[]
for i in range(len(install)):
  arraycopy=copy.deepcopy(array)
  for wall in install[i]:
    wallx,wally=wall
    arraycopy[wallx][wally]=1
    # 벽이 설치된 경우에 대해 다 탐색을 진행
  result.append(bfs())
print(max(result))
      