import sys
input=sys.stdin.readline

#크면 줄이고 작으면 늘리고 하는 식으로 찾으면 되지 않을까? 어차피 크기가 1이면 그만 찾아도 되잖아
#이 과정에서 범위 내에 들어오면 정답이랑 비교하는거지
N,S=map(int,input().split())
numList=[0]+list(map(int,input().split()))
start=0
answer=N+1
pos=False
end=1

#일단 누적합 배열로 만들어
for i in range(1,N+1):
    numList[i]+=numList[i-1]
# print(numList)

#start,end사이의 값을 temp로 두고
while start < end < N+1:
    temp = numList[end] - numList[start]
    if temp<S:
        end+=1
    else:
        pos=True
        answer=min(answer,end-start)
        start+=1
if pos: print(answer)
else: print(0)
