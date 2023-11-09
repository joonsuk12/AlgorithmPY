import sys
input=sys.stdin.readline

#최소횟수가 여러개일때 왼쪽부터라는말이 힌트
#맨 왼쪽부터 같은수를 찾아 바꿔가과
#끝까지 다 같아졌을때 횟수를 셈
#그걸 N번째까지 하면 댈듯

N,M=map(int,input().split())

color_list=[0]+list(map(int,input().split()))

for idx in range(0,N+1):
    temp_list=color_list[:]
    start_num=temp_list[idx]
    index=idx
    #다 짜맞추기 로직,인덱스가 N-1까지.
    while idx<N:
        #앞쪽 숫자가 뒤쪽과 같으면 자연스럽게 넘어가고

        #다르다면 숫자가 맞을때까지 더하고 횟수세기

        #누적합 적용해놓기