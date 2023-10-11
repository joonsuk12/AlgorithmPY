import sys
from collections import deque

input=sys.stdin.readline

R,C,reps=map(int,input().split())
board= [[0 for col in range(C + 1)]]
for i in range(R):
    temp_list=[0]+list(map(int,input().split()))
    board.append(temp_list)

rR=R
rC=C
sr=1
sc=1
que= deque()

#가급적 함수 안에서 값이 바뀐다고 한다면, 복사해서 사용하도록 하자.

while R>0 and C>0:
    que.clear()
    for c in range(0, C-1):
        que.append(board[sr][sc+c])
    for r in range(0, R-1):
        que.append(board[sr+r][sc+C-1])
    for c in range(C-1,0,-1):
        que.append(board[sr+R-1][sc+c])
    for r in range(R-1,0,-1):
        que.append(board[sr+r][sc])
    temp_reps=reps%len(que)
    for i in range(temp_reps):
        head=que[0]
        que.popleft()
        que.append(head)
    for c in range(0, C-1):
        board[sr][sc+c]=que[0]
        que.popleft()
    for r in range(0, R-1):
        board[sr+r][sc+C-1]=que[0]
        que.popleft()
    for c in range(C-1,0,-1):
        board[sr + R - 1][sc + c]=que[0]
        que.popleft()
    for r in range(R-1,0,-1):
        board[sr + r][sc]=que[0]
        que.popleft()
    R-=2
    C-=2
    sr+=1
    sc+=1

for i in range(1, rR+1):
    for j in range(1, rC+1):
        print(board[i][j],end=' ')
    print()