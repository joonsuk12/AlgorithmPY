import sys
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

#만들어진 누적합 배열으로 일치하는 구간 찾기.
#같은 구간을 체크하면서 넘어가야하나.
#완탐으로 먼저 풀어보자
def findNumPair():
    global answer
    #모든 자리에서 모든 부분수열을 체크하기
    for i in range(0,N+1):
        for j in range(i+1,N+1):
            if range_sum_B[j]-range_sum_B[i]==range_sum_A[j]-range_sum_A[i]:
                answer+=1

#시간초과 로직을 해결합시다
#실행
def solution():
    madeSumList()
    findNumPair();
    print(answer)
    return

solution()