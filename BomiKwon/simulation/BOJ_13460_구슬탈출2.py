# 삼성sw역량테스트 기출 문제 01 - 구슬탈출2
# 0314

from collections import deque
n,m=map(int,input().split())
array=[]
for _ in range(n):
  array.append(list(input()))
# [빨간구슬x][빨간구슬y][파란구슬x][파란구슬y] 방문여부
visited=[[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
  for j in range(m):
    if array[i][j]=='R':
      redx,redy=i,j
    if array[i][j]=='B':
      bluex,bluey=i,j

# 다음 위치가 벽이 아니고, 지금이 구멍이 아니면 해당 방향에 따라 계속 움직인다
def move(x,y,dx,dy,c):
  while array[x+dx][y+dy]!='#' and array[x][y]!='O':
    x+=dx
    y+=dy
    c+=1
  return x,y,c

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
  queue=deque()
  queue.append((redx,redy,bluex,bluey,0))
  while queue:
    rx,ry,bx,by,tc=queue.popleft()
    # 10회 이상인 경우 실패로 처리
    if tc>=10:
      break
    for i in range(4):    
      # 각각 구슬에 대해, 각 방향에 대해 move함수 처리
      nRx,nRy,rc=move(rx,ry,dx[i],dy[i],0)
      nBx,nBy,bc=move(bx,by,dx[i],dy[i],0)
      # 파란 구슬이 구멍에 온 경우 무시
      if array[nBx][nBy]=='O':
        continue
      # 빨간 구슬이 구멍에 온 경우 전체 움직인 횟수를 출력
      if array[nRx][nRy]=='O':
        print(tc+1)
        return
      # 파란 구슬과 빨간 구슬의 위치가 같으면 더 움직인 구슬을 전 위치로 옮긴다
      if nRx==nBx and nRy==nBy:
        if rc>bc:
          nRx=nRx-dx[i]
          nRy=nRy-dy[i]
        else:
          nBx=nBx-dx[i]
          nBy=nBy-dy[i]
      # 방문 여부를 확인한 뒤 큐애 넣어주기
      if visited[nRx][nRy][nBx][nBy]==False:
        visited[nRx][nRy][nBx][nBy]=True
        queue.append((nRx,nRy,nBx,nBy,tc+1))
        # print((nRx,nRy,nBx,nBy,tc))
  print(-1)
        
bfs()
          
            


