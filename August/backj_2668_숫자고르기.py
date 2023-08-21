import sys
from collections import deque
input=sys.stdin.readline
'''
다뽑고 나서 위의 집합과 아래의 집합이 일치하게끔 짜는 최대의 경우를 찾자
100개의 경우에 대한 powerSet은 말이 안되는 수치
완탐 불가.
1 2 3 4 5 6 7
3 1 1 5 5 4 6
그래프의 정점을 순회하면서 양방향인 정점들을 담거나, 자기 자신을 가리키는 정점을 담고
그 개수와 정점을 오름차순으로 정렬해서 출력하라?
->그냥 특정 점에서 가는 곳에서 다시 나를 가리키는지를 확인하면 되나?

반례를 떠올려보자
1 2 3 4 5 6
2 3 1 4 5 6
이러한 반례도 분명히 존재한다.-> 이전 방식은 잘못된 방식인듯.

두번째 생각, 사이클을 그리는 상황이라면? 오오 이건거 같음
인접 리스트라고 생각하고 사이클을 그리는 정점들을 정답에 넣어보는거야

사이클을 찾는 법, 경로를 계속 가지고 가다가 이미 방문한 정점을 방문하려고 하면
->사이클임!

가장 큰 사이클을 그리는 경우를 찾아야 되겠는데용
정점 100개
정점개수만큼 뽑으면 끝내기
'''

#입력
N=int(input())
adjList=[0 for _ in range(N+1)]
is_cycle=[False for _ in range(N+1)]
answer=0
answerlist=list()
for i in range(1,N+1):
    start=i
    end=int(input())
    adjList[start]=end

#함수
#발생할 수 있는 모든 사이클을 찾아야 하지 않나->완탐식 접근
#모든 정점마다의 사이클을 분석한다.
#간선이 1개씩이므로 나에서 출발해서 나에서 돌아오면 사이클임.

def bfs(begin):
    #덱을 만들어서 시작정점을 넣고
    global answer, N,answerlist
    q=deque()
    node=[begin,[]]
    node[1].append(begin)
    q.append(node)
    visited[begin]=True
    #q가 빌 때까지
    while len(q)!=0:
        temp=q.popleft()
        #현재 정점[0]에서 갈 수 있는 정점을 탐색함
        temp[1].append(adjList[temp[0]])
        #다음정점이 출발점이라면,
        if adjList[temp[0]]==begin:
            for j in temp[1]:
                is_cycle[j]=True
        if not visited[adjList[temp[0]]]:
            visited[adjList[temp[0]]]=True
            q.append([adjList[temp[0]],temp[1]])
            continue

#실행
for i in range(1,N+1):
    visited=[False for _ in range(N+1)]
    bfs(i)

for i in is_cycle:
    if i:
        answer+=1
print(answer)
for i in range(1,N+1):
    if is_cycle[i]:
        print(i)
