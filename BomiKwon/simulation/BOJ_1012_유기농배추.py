import sys
t=int(sys.stdin.readline())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(start):
  stack=[]
  stack.append(start)
  while stack:
    x,y=stack.pop()
    array[x][y]=0
    visited[x][y]=1
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if [nx,ny] in pos:
        if array[nx][ny]==1:
          stack.append([nx,ny])

# 테케별 탐색을 몇번했는지 담는 배열
result=[]
for _ in range(t):
  m,n,k=map(int,sys.stdin.readline().split())
  array=[[0]*n for _ in range(m)]
  
  # 배추의 위치를 저장하고 있음 - start 후보
  pos=[]
  for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    pos.append([x,y])
    array[x][y]=1

  cnt=0
  visited=[[0]*n for _ in range(m)]
  for i in pos:
    # 방문하지 않은 곳에 대해서 탐색 시작
    if visited[i[0]][i[1]]!=1:
      dfs(i)
      # 탐색이 끝날 때마다 인접한 배추는 다 돈 것
      cnt+=1
  result.append(cnt)

# 정답 출력
for i in result:
  print(i)