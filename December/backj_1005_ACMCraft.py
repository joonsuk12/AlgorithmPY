import sys
from collections import deque

input=sys.stdin.readline

#위상 정렬이 뭔데
T=int(input())
answer=[]

#테케 동안
for i in range(T):
    N,K=map(int,input().split())
    DList=[0]+list(map(int,input().split()))
    dp=[0 for j in range(N+1)]
    depthDict=dict()
    #그래프
    adjList=[[] for j in range(N+1)]
    #인엣지 리스트
    inedge=[0 for j in range(N+1)]

    for j in range(K):
        #역방향으로 그래프 간선을 받는다.
        start,end=map(int,input().split())
        #단방향임
        adjList[start].append(end)
        inedge[end]+=1
    #특정 건물
    goal=int(input())

    #BFS
    que=deque()
    #inedge가 0인 애들 부터 큐에 넣는다.
    for j in range(1,N+1):
        if inedge[j]==0:
            dp[j]=DList[j]
            que.append(j)
    #큐가 빌때까지
    while que:
        #큐에서 가장 앞의 값을 빼고
        temp=que.popleft()
        for k in adjList[temp]:
            #얘로 갈 수 있는 애들을 보면서,
            #지금까지의 나의 최대+얘 자체 건설시간이랑 최대를 계속 비교해 저장한다.
            dp[int(k)]=max(dp[int(k)], dp[temp]+DList[int(k)])
            #비교해줬으면 가야할 정점에 대해서 inedge값을 1 줄여준다.
            if inedge[int(k)]>0:
                inedge[int(k)]-=1
            #inedge가 0이 된 애들은 큐에 넣어준다.
            if inedge[int(k)]==0:
                que.append(int(k))
    answer.append(dp[goal])
for i in answer:
    print(i)
