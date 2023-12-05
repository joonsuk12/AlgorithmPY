import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,R,Q=map(int,input().split())
tree=dict()
for i in range(1, N+1):
    tree[i]=[]
#1부터 N번 인접리스트 정보 저장.
adjList=[[] for i in range(N+1)]
visited=[False for i in range(N+1)]

Qlist=[]
counts=1
#그래프를 그리고 R에서부터 재귀로 주변 이동 노드를 순회 하면서 트리에 값을 저장?

#그래놓고 나중에 정점개수를 세면서 바닥까지 내려가면 될 듯

for i in range(N-1):
    U,V=map(int,input().split())
    adjList[U].append(V)
    adjList[V].append(U)

for i in range(Q):
    temp=int(input())
    Qlist.append(temp)
def dfs(father):
    global tree,visited

    if len(adjList[father])>0:
        for j in range(len(adjList[father])):
            toNode=adjList[father][j]
            if visited[toNode]: continue
            tree[father].append(toNode)
            visited[toNode] = True
            dfs(toNode)

    return

visited[R]=True
dfs(R)

def countNode(father):
    global counts
    #트리 현재의 아래로 내려갈 수 있으면 셈
    if len(tree[father])>0:
        for j in range(len(tree[father])):
            counts+=1
            countNode(tree[father][j])
    return


for i in Qlist:
    counts=1
    countNode(i)
    print(counts)