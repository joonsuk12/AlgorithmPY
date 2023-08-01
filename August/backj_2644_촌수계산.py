import sys
from collections import deque
input=sys.stdin.readline
'''
특정 점에서 특정 점으로의 최단거리를 찾으라는 거 아녀?
어차피 가중치는 1이니까 bfs로 충분히 해결할 수 잇는 문제임
'''

#입력부
N=int(input())
man1, man2=map(int,input().split())
E=int(input())

adjList=[[]for i in range(N+1)]
visited=[False for i in range(N+1)]

for i in range(E):
    start, end=map(int,input().split())
    #여기도 양방향바인딩인듯
    adjList[start].append(end)
    adjList[end].append(start)

#함수부
#특정 정점에서 특정 정점으로의 최소가중치,가중치가 1?->bfs문제임
#bfs함수 정의
def bfs(start):
    deq=deque()
    #시작정점을 덱에 넣고 방문처리하고
    #클래스를 사용해서 문제를 풀고싶넹
    deq.append([start,0])
    visited[start]=True
    #큐가 빌 때까지
    while len(deq)!=0:
        #큐에서 하나를 뽑아내서
        temp=deq.popleft()
        #해당 정점을 만나면 해당 정점의 깊이를 반환하면 된다.
        if temp[0]==man2:
            return temp[1]
        #해당 정점에서 갈 수 있는 모든 정점들을 보면서
        for i in adjList[temp[0]]:
            #갈수 있는 정점을 큐에 넣고, 방문처리하기
            if visited[i]: continue
            deq.append([i,temp[1]+1])
            visited[i]=True
    return -1
#실행부
print(bfs(man1))