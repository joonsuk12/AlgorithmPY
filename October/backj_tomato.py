import sys
input=sys.stdin.readline
from collections import deque


dr=[-1,1,0,0,0,0]
dc=[0,0,-1,1,0,0]
dh=[0,0,0,0,-1,1]

C,R,H=map(int,input().split())
rest_count=0
board=[]
for h in range(H):
    temp_board=[]
    for r in range(R):
        temp_list=list(map(int,input().split()))
        temp_board.append(temp_list)
    board.append(temp_board)

for h in range(H):
    for r in range(R):
        for c in range(C):
            if board[h][r][c]==0:
                rest_count+=1

#상하좌우위아래를 전부 탐색하자
#bfs로!
#한번에 1인애들 다 큐에 담아서 처리해야되는거 알지?
def bfs():
    global rest_count

    depth=0
    que=deque()
    #큐에 시작점 다 넣고
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if board[h][r][c]==1:
                    que.append([h,r,c,0])
    #큐가 빌 때까지
    while len(que)!=0:
        #하나씩 빼서 갈 수 있는 방향 확인하고, 안익은 토마토(0)면 익혀(1) 아니면 멈춤
        temp=que.popleft()
        for i in range(6):
            nh=temp[0]+dh[i]
            nr=temp[1]+dr[i]
            nc=temp[2]+dc[i]
            #넘는지 여부 확인
            if 0<=nh<H and 0<=nr<R and 0<=nc<C:
                if board[nh][nr][nc]==0:
                    board[nh][nr][nc]=1
                    depth=max(depth,temp[3]+1)
                    que.append([nh,nr,nc,temp[3]+1])
                    rest_count-=1
    if rest_count==0:
        return depth
    return -1

print(bfs())



