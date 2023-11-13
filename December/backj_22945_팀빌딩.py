import sys
input=sys.stdin.readline

#10만명에 나머지 9만 9천명을 하나씩 묶어보면서 팀을 꾸려보는거임
#10만C2->무적권 시간초과

#완탐식 사고를 해결하는 방법->DP, 누적합, 백트래킹, 투포인터, 이진탐색
#범위 연산이 아니므로 누적합은 별로일듯?
#투포인터로 가자


N=int(input())

statList=list(map(int,input().split()))

#일단 완탐으로 풀이

# for st in range (N-2):
#     for end in range(st+2,N):
#         temp=min(statList[st],statList[end])*(end-st-1)
#         if answer<temp:
#             answer=temp
#             an_start=statList[st]
#             an_end=statList[end]

#처음에 제일 길때부터 양쪽으로 줄여나갈건데,
#뒤가 크거나 같으면 앞을 줄여서 키워본다
#앞이 크면 뒤를 줄여서 키워본다
start=0
end=N-1
answer=0
while start+1<end:
    temp=(end-start-1)*min(statList[start],statList[end])
    answer=max(temp,answer)
    if statList[start]>statList[end]:
        end-=1
    else:
        start+=1




print(answer)
