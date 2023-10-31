import sys
from collections import deque

input=sys.stdin.readline

R,C=map(int,input().split())
wolves=0
sheeps=0
board=[]
dr=[-1,1,0,0]
dc=[0,0,-1,1]
visited=[[False for c in range(C)]for r in range(R)]

for i in range(R):
    str=input().rstrip()
    temp_list=[]
    for j in range(len(str)):
        if str[j]=='v':
            wolves+=1
        elif str[j]=='o':
            sheeps+=1
        temp_list.append(str[j])
    board.append(temp_list)

def bfs(sr,sc):
    global wolves, sheeps, visited

    que=deque()
    temp_wolves = 0
    temp_sheeps = 0

    if board[sr][sc] == 'v':
        temp_wolves += 1
    elif board[sr][sc] == 'o':
        temp_sheeps += 1
    que.append([sr,sc])
    visited[sr][sc]=True
    while len(que)!=0:

        temp=que.popleft()

        for i in range(4):
            nr=temp[0]+dr[i]
            nc=temp[1]+dc[i]
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and board[nr][nc]!='#':
                if board[nr][nc]=='v':
                    temp_wolves+=1
                elif board[nr][nc]=='o':
                    temp_sheeps+=1
                que.append([nr,nc])
                visited[nr][nc]=True

    if temp_sheeps> temp_wolves:
        wolves-=temp_wolves
        return
    sheeps-=temp_sheeps
    return

for r in range(R):
    for c in range(C):
        if board[r][c]!='#' and not visited[r][c]:
            bfs(r,c)

print(sheeps, wolves)