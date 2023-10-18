import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int, input().split())
board=[]
start=[0,0]
dr=[-1,1,0,0]
dc=[0,0,-1,1]
visited=[[False for c in range(C)] for r in range(R)]
for r in range(R):
    temp_list=list(input().rstrip())
    #시작점 위치는 알아야 할듯?
    temp_list=list(map(int,temp_list))
    for c in range(C):
        if temp_list[c]==2:
            start=[r,c]
    board.append(temp_list)

#시작점에서 3,4,5중 하나를 제일 먼저 도달할 수 있는 거리?
#BFS
def BFS(st):
    q=deque()
    visited[st[0]][st[1]]=True
    q.append(st+[0])
    while len(q)>0:
        #큐에서 하나 빼서
        temp=q.popleft()
        #다른 곳으로 갈 수 있으면 가고 큐에 담기
        for i in range(4):
            nr=temp[0]+dr[i]
            nc=temp[1]+dc[i]
            weight=temp[2]+1
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and board[nr][nc]!=1:
                if board[nr][nc] > 2:
                    return weight
                visited[nr][nc]=True
                q.append([nr,nc,weight])

    #다 돌았는데 반환이 안댓네?->-1반환
    return -1

answer=BFS(start)

if answer==-1:
    print("NIE")
else:
    print("TAK")
    print(answer)
