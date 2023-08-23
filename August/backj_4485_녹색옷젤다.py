import sys
import heapq
from heapq import heappush,heappop

input=sys.stdin.readline

'''
가중치가 1이상인 양의 정수인 그래프 문제,
최소비용이동?->그냥 다익스트라다 이말이야
'''

#선언
dr=[-1,1,0,0]
dc=[0,0,-1,1]
#함수부

#0,0에서만 항상 시작하는 다익스트라,
def dijkstra():
    #노드 개수만큼 거리배열 생성
    distance=[[100000000 for j in range(N)]for i in range(N)]
    distance[0][0]=0
    #시작정점의 거리배열을 0으로 만듬
    #우선순위 큐에다가 시작 노드 넣기
    pq=[]
    heappush(pq,[[0,0],0])
    #큐가 빌 때 까지
    while len(pq)!=0:
        temp=heappop(pq)
        #weight가 현재 저장된 거리배열의 값보다 크면 그냥 넘어감
        if temp[1]>distance[temp[0][0]][temp[0][1]]:
            continue
        #방문가능한 정점을 보면서
        for i in range(4):
            nr=temp[0][0]+dr[i]
            nc=temp[0][1]+dc[i]
            #경유지를 거쳐 가는 경로가 해당 정점으로의 코스트보다 작다면 갱신하고
            #큐에 넣기
            if 0<=nr<N and 0<=nc<N:
                nextT=temp[1]+jelmap[nr][nc]
                if nextT<distance[nr][nc]:
                    distance[nr][nc]=nextT
                    heappush(pq,[[nr,nc],nextT])
    return distance[N-1][N-1]+jelmap[0][0]


#실행
N=3
count=1
while N!=0:
    N = int(input())
    if N==0:
        exit(0)
    jelmap=[list(map(int,input().split())) for i in range(N)]
    answer=dijkstra()
    print("Problem "+str(count)+": "+str(answer))

    count+=1