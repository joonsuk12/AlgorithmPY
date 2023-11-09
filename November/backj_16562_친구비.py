import sys
from collections import deque
input=sys.stdin.readline

#입력

N,M,k=map(int, input().split())
payN=[0]+list(map(int, input().split()))
friend=[False for i in range(N+1)]
tempCost=0
adjList=[[]for n in range(N+1)]

for m in range(M):
    start,end=map(int,input().split())
    adjList[start].append(end)
    adjList[end].append(start)

def BFS(begin):
    global friend, tempCost
    q=deque()
    #첫번째 넣고 방문처리, 첫번째 애랑 친구비를 temp에 저장
    q.append(begin)
    tempMin=payN[begin]
    friend[begin]=True
    #큐가 빌 때까지
    while len(q)>0:
        #큐에서 하나 빼서
        tempMan=q[0]
        q.popleft()
        manLen=len(adjList[tempMan])
        #갈 수 있는 방향으로 다 가기, 그 친구랑 친구하는 친구비가 더 싸면 최소 친구비 갱신
        for i in range(manLen):
            withFriend=adjList[tempMan][i]
            if friend[withFriend]: continue
            #방문 처리 하고 큐에 넣기
            friend[withFriend]=True
            tempMin=min(tempMin,payN[withFriend])
            q.append(withFriend)
    #다 돌았으면 최소 친구비를 tempCost에 저장하기.
    tempCost+=tempMin

#2. 최소 비용으로 그래프를 모두 칠할 수 있는 가격을 찾는다
for n in range(1,N+1):
    #tempCost가 k를 넘어가면 종료해버리기
    if tempCost>k:
        print("Oh no")
        exit(0)
    #1번 친구부터 쭉 bfs, 이미 친구면 넘어가기
    if friend[n] : continue
    BFS(n)


#3. k와 tempCost를 비교해서 가능 불가 여부를 확인
if tempCost>k:
    print("Oh no")
    exit(0)

print(tempCost)

