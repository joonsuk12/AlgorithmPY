import sys
input=sys.stdin.readline


answer=0
reps=1
edgeList=[]

#트리를 순서대로 그어가다가, 사이클이 발생해, 유니온이 불가하면 해당  수를 answer에 저장하고 함수 종료
#끝까지 이런 경우가 발생하지 않으면 그대로 answer를 반환

N,M=map(int,input().split())

#N개의 정점에 대한 부모배열을 만들자
parents=[i for i in range(N)]

for i in range(M):
    edgeList.append(list(map(int,input().split())))

# print(edgeList)

def find(a):
    parent=a
    while parents[parent]!=parent:
        parent=parents[parent]
    return parent

#부모끼리 비교하고, 부모의 부모를 바꿔줘야한다.
def union(a,b):
    pA=find(a)
    pB=find(b)
    if pA!=pB:
        parents[pB]=pA
        return True
    else:
        return False
#순서대로 유니온 파인드
for start,end in edgeList:
    #유니온 가능하면 유니온 하고, 안대면 answer에 현재 횟수 저장,break
    if union(start,end):
        reps+=1
    else:
        answer=reps
        break
print(answer)