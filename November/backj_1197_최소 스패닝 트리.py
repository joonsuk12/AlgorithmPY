import sys

input = sys.stdin.readline

V, E = map(int, input().split())

edgeList = []
answer = 0
# 간선 배열 받기
for i in range(E):
    edgeList.append(list(map(int, input().split())))

# 간선을 가중치를 기준으로 오름차순 정렬하기.
edgeList.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]


# 부모 찾기
def getParent(x):
    # 부모배열이 나면 나를 리턴
    if parent[x] == x:
        return x
    # 부모배열의 값으로 부모를 찾기
    parent[x] = getParent(parent[x])
    return parent[x]

#연결하기
def unionFind(a, b):
    # 각자부모찾기
    a = getParent(a)
    b = getParent(b)
    # 작은 쪽을 부모로 삼기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
#크루스칼
#가중치 작은 간선부터 유니온파인드해서 부모가 다르면 연결하기
for start,end,cost in edgeList:
    #부모가 다르면 간선에 연결하기
    if getParent(start)!=getParent(end):
        unionFind(start,end)
        answer+=cost
print(answer)
