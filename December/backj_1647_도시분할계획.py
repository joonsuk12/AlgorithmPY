import sys

input = sys.stdin.readline

# 그래프

#mst uf 간선을 제일 가중치 작은 거 uf

# 그래프-> 최소신장트리 connect개수가 2개 이하 가중치가 최대인 값 ->답

N, M = map(int,input().split())
edgeList=[]
#초기에 부모는 모두 자기 자신.
parents=[i for i in range(N+1)]
answer=0

#a의 부모를 찾는 함수
def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

#a,b 두개의 부모가 달라 둘을 합치는 함수
def union(a,b):
    if find(a)!=find(b):
        #부모가 다르면 합치고 b의 부모에 a값을 넣는다.
        parents[b]=a
        return True
    else:
        return False

# graph=[[] for i in range(N+1)]
for i in range(M):
    start, end, weight =map(int,input().split())
    edgeList.append([start,end,weight])
#간선리스트 정렬하기
edgeList.sort(key=lambda x:x[2])
final=0
#그래프 형성 안하는 선에서 간선을 하나씩 잡아보자고, 이미 고른 곳만 다시 안고르면댐
for start, end, weight in edgeList:
    #u,f해서 부모가 같으면 넘어가고, 부모가 다르면 간선 연결하고 같은 부모로 취급하기.
    #uni
    if union(start,end):
        answer+=weight
        final=weight

print(answer-final)
