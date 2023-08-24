import sys
from collections import deque
input=sys.stdin.readline

'''
0: 공기없는 빈공간
1: 치즈
2: 공기 있는 빈공간

1초마다 한번의 동작
1.공기를 0,0 인덱스에서 뿌려주고 bfs
2. 내부의 치즈들을 보면서 2의 기준에서 1이 2개 이상이면 녹여버리고 bfs
3. 남은 치즈의 개수를 센다
'''
#선언
dr=[-1,1,0,0]
dc=[0,0,-1,1]

#입
N,M=map(int,input().split())
cheeseMap=[list(map(int,input().split())) for i in range(N)]
#함
def spreadAir():
    visited=[[False for i in range(M)]for j in range(N)]
    #시작 정점을 큐에 넣어줌
    que=deque()
    que.append([0,0])
    visited[0][0]=True
    while len(que)!=0:
        #하나를 빼서,
        temp=que.popleft()
        #4방향 탐색
        for i in range(4):
            nr=temp[0]+dr[i]
            nc=temp[1]+dc[i]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                #0이면 공기를 뿌려 2로 보내고 큐에 넣음
                visited[nr][nc]=True
                if cheeseMap[nr][nc]==0:
                    cheeseMap[nr][nc]=2
                    que.append([nr,nc])
                #2면 아무것도 안하고 큐에 넣고
                elif cheeseMap[nr][nc]==2:
                    que.append([nr,nc])
                #1이면 치즈니까 못감
                else: continue
    return
#치즈가 녹을 수 있는지 파악하기
def meltCheckCheese(r, c):
    countAir=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<N and 0<=nc<M:
            if cheeseMap[nr][nc]==2:
                countAir+=1
        if countAir>=2:
            return True
    return False

#산소가 뿌려진 다음 치즈를 녹이는 과정, 녹일거를 지정하고 나중에 한번에 지워야함
def meltAll():
    meltList=[]
    visited = [[False for i in range(M)] for j in range(N)]
    # 시작 정점을 큐에 넣어줌
    que = deque()
    que.append([0, 0])
    visited[0][0] = True
    while len(que) != 0:
        # 하나를 빼서,
        temp = que.popleft()
        # 4방향 탐색
        for i in range(4):
            nr = temp[0] + dr[i]
            nc = temp[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                # 1이면 치즈니까 녹일지를 판단함
                if cheeseMap[nr][nc] == 1:
                    if meltCheckCheese(nr,nc):
                        meltList.append([nr,nc])
                que.append([nr, nc])

    return meltList
def countCheese():
    visited = [[False for i in range(M)] for j in range(N)]
    # 시작 정점을 큐에 넣어줌
    cheeseCount=0
    que = deque()
    que.append([0, 0])
    visited[0][0] = True
    while len(que) != 0:
        # 하나를 빼서,
        temp = que.popleft()
        # 4방향 탐색
        for i in range(4):
            nr = temp[0] + dr[i]
            nc = temp[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc]=True
                # 1이면 치즈니까 세고 큐에 넣음
                if cheeseMap[nr][nc] == 1:
                    cheeseCount+=1
                que.append([nr, nc])

    return cheeseCount


#실
ansTime=0
cheeseMap[0][0]=2

for i in range(500):
    ansTime += 1
    spreadAir()
    delList=meltAll()
    for i in delList:
        cheeseMap[i[0]][i[1]]=0
    # for i in cheeseMap:
    #     print(i)
    # print()
    if countCheese()==0:
        break
print(ansTime)

#외부의 공기와 접촉해야지!