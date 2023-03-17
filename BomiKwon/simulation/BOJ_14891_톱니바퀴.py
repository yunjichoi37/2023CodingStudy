# 삼성sw역량테스트 기출 문제 03 - 톱니바퀴
# 0316-0317

from collections import deque
# 오른쪽에 위치한 바퀴를 체크 -> 연쇄적으로
def right_check(num,dir):
  if num>4:
    return
  if gears[num-1][2]==gears[num][6]:
    return
  if gears[num-1][2]!=gears[num][6]:
    # 오른쪽을 체크하는 경우
    right_check(num+1,-dir)
    # 원래 움직여야하는 경우
    gears[num].rotate(dir)
    
# 왼쪽에 위치한 바퀴를 체크
def left_check(num,dir):
  if num<1:
    return
  if gears[num+1][6]==gears[num][2]:
    return
  if gears[num+1][6]!=gears[num][2]:
    # 왼쪽을 체크하는 경우
    left_check(num-1,-dir)
    # 원래 움직여야 하는 경우
    gears[num].rotate(dir)


gears={}
for i in range(1,5):
  gears[i]=deque(list(map(int,list(input().replace("\n","")))))
k=int(input())

turnlist=[]
for _ in range(k):
  # 돌아갈 톱니 번호, 방향
  turnlist.append(list(map(int,input().split(" "))))

for i in range(k):
  n,d=turnlist[i]
  left_check(n-1,-d)
  right_check(n+1,-d)
  gears[n].rotate(d)

# 점수 출력
cnt=0
for i in range(4):
  cnt+=(2**i)*gears[i+1][0]
print(cnt)