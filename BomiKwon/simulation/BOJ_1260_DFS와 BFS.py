from collections import deque
n,m,v=map(int,input().split())

#탐색을 위한 그래프 만들기 - 양방향으로
array={}
max_v=0
for _ in range(m):
  a,b=map(int,input().split())
  if a not in array.keys():
    array[a]=[b]
  elif a in array.keys():
    array[a].append(b)
  if b not in array.keys():
    array[b]=[a]
  elif b in array.keys():
    array[b].append(a)
node=[]
for _ in range(max(list(array.keys()))+1):
  node.append([])
key_list=list(array.keys())
val_list=list(array.values())
for i in range(len(array)):
  node[key_list[i]]=val_list[i]

# 간선 작은 순
for i in node:
  i.sort()
# print(node)

# DFS
stack=[]
result_d=[]
def dfs(graph,start):
  stack.append(start)
  visited_d[start]=True
  v=stack.pop()
  result_d.append(v)
  for i in graph[v]:
    if not visited_d[i]:
      dfs(node,i)
      visited_d[i]=True

# BFS
result_b=[]
def bfs(graph,start):
  queue=deque([start])
  visited_b[start]=True
  while(queue):
    v=queue.popleft()
    result_b.append(v)
    for i in graph[v]:
      if not visited_b[i]:
        queue.append(i)
        visited_b[i]=True
  
# 탐색
visited_b=[0]*(len(node)+1)
visited_d=[0]*(len(node)+1)
dfs(node,v)
bfs(node,v)

#출력
for i in result_d:
  print(i,end=" ")
print()
for i in result_b:
  print(i,end=" ")