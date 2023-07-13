import sys
import itertools
input=sys.stdin.readline

'''
차의 절대값의 합이 최대
0-1 1-2 2-3
완탐식 사고-> N이 8개, 8개 중에 8개를 뽑아서 나열하는 8P8순열을 모두 구하고
그 중 최대를 찾기


예제 입력
20 1 15 8 4 10
20 15 10 8 4 1

'''

#입력
N=int(input())
numlist=list(map(int,input().split()))
selected=[False for _ in range(N)]

#선언
answer=0
def cal(arr):
    ans=0
    for i in range(0,N-1):
        ans+=abs(arr[i]-arr[i+1])
    return ans

def perm(cnt, arr):
    global answer
    #기저 조건
    if cnt==N:
        #N개 뽑았으면 최대와 비교한다
        temp=cal(arr)
        if temp>answer:
            answer=temp
        return
    #뽑아서 나열
    for i in range(0,N):
        if selected[i]:
            continue
        selected[i]=True
        perm(cnt+1,arr+[numlist[i]])
        selected[i]=False
#구현
perm(0,[])
print(answer)
