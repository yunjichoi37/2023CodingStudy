# 방향 설정 잘 할 것, 방향과 d를 매치하는 부분에서 유의할 것
# 무조건 dfs가 아닌 좌표를 활용하는 문제가 있음을 기억하기.

import sys
# input 대신  sys.stdin.readline()
n,m=map(int,sys.stdin.readline().split())
r,c,d=map(int,sys.stdin.readline().split())
array=[]
for _ in range(n):
  array.append(list(map(int,sys.stdin.readline().split())))

# 북 남 동 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 처음 위치
cnt=1
array[r][c]=-1
while True:
  # 후진 했을 때 벽이면 종료
  if array[r][c]==1:
    break
  flag=0
  # 4가지 방향 탐색
  for _ in range(4):
    d-=1
    if d==-1:
      d=3
    nr=r+dx[d]
    nc=c+dy[d]
    # 빈칸을 발견하면
    if array[nr][nc]==0:
      r=nr
      c=nc
      array[r][c]=-1  
      flag=1
      cnt+=1
      break
  # 빈 칸이 없을시, 후진
  if flag==0:
    r+=dx[d-2]
    c+=dy[d-2]

print(cnt)