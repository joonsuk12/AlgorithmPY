import sys
from collections import defaultdict
input=sys.stdin.readline

'''
같은 크기,수열에서 같은 인덱스의 부분 수열을 추출해 이 수열의 합이
다른 수열의 합과 일치하는 구간의 정수쌍의 개수를 구하는 문제,
구간합을 저장하는 누적합 배열을 만들고, 완탐으로 구간을 잘라갈?
->기에는 너무 큰 시간복잡도인거같은데
100000*
'''
#입력부
N=int(input())
A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))

#선언부
answer=0
range_sum_A=[0 for i in range(N+1)]
range_sum_B=[0 for i in range(N+1)]
#함수부

#누적합배열을 만드는 메서드
def madeSumList():
    global range_sum_A,range_sum_B
    for i in range(1,N+1):
        range_sum_A[i]=range_sum_A[i-1]+A[i]
    for j in range(1,N+1):
        range_sum_B[j]=range_sum_B[j-1]+B[j]


#시간초과 로직을 해결합시다
#i번째 까지의 두 수열의 누적합의 차가 이전에 계산된 차가 있다면, 정답 1증가
#아니면, 딕셔너리의 키에 추가
def findPairTime():
    global answer
    sumdict=defaultdict(int)
    for i in range(1,N+1):
        gap=range_sum_A[i]-range_sum_B[i]
        if gap==0:
            sumdict[0]+=1
            answer+=sumdict[gap]
            continue
        if sumdict[gap]!=0:
            answer+=sumdict[gap]
            sumdict[gap]+=1
        else:
            sumdict[gap]=1

#실행
def solution():
    madeSumList()
    findPairTime()
    print(answer)
    return

solution()