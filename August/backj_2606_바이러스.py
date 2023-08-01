import sys
from collections import deque
input=sys.stdin.readline
'''
연결요소 찾기인데,->bfs로 풀면 될듯?
퍼져나간다? ->bfs 느낌으로 풀자
'''

#입력부
N=int(input())
E=int(input())
#1~N번째 까지 쓰고 그 뒤는 사용하지 말자.
adjList=[[] for i in range(N+1)]
visited=[False for i in range(N+1)]

for i in range(E):
    start, end = map(int,input().split())
    #양뱡향 리스트임
    adjList[start].append(end)
    adjList[end].append(start)

#선언부

#그래프를 시작점부터 bfs를 돌려 바이러스가 전파되는 컴퓨터의
#수를 세는 함수
def bfs(start):
    deq=deque()
    tempans=0
    #방문처리 할 때 마다, 카운트를 세자.
    #시작 노드를 넣고
    deq.append(start)
    #방문처리
    visited[start]=True
    #큐가 빌 때 까지
    while len(deq)!=0:
        #큐에서 하나 뽑고
        temp=deq.popleft()

        #갈 수 있는 노드 중에 방문 처리 안된 노드들을 큐에 담고
        for i in adjList[temp]:
            if visited[i]: continue
            #방문처리를 하면서 담아버리기
            deq.append(i)
            visited[i]=True
            tempans+=1

    return tempans
#실행부

print(bfs(1))