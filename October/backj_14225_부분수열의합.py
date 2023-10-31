import sys
input=sys.stdin.readline

N_out=int(input())
S_out=list(map(int,input().split()))
flag=False

#원소의 개수가 최대 20개이므로 powerSet으로 문제를 풀이해보자.
def solution(N,S):
    num_list=[]
    #숫자중 가장 작은수를 찾음, 해당 수보다 작은 수가 있으면 해당 수가 부분 수열의 합으로 나올 수 없는 가장 작은수
    if min(S)>1:
        print(1)
        exit(0)

    #시간제한 2초 완탐으로도 풀 수 있지 않았을까
    def Combination(visit, cnt, end_cnt, num):

        if cnt == end_cnt:
            num_list.append(num)
            return
        # 반복문 돌면서 아직 안고른 애들 중 하나 고르고 방문처리하고 다음으로 넘어가야 함
        for idx in range(cnt, end_cnt):
            if visit[idx]: continue
            visit[idx] = True
            Combination(visit, cnt + 1, end_cnt, num)
            visit[idx] = False

    # nC1~nCn까지 해보면서 목표한 num을 만들 수 있으면 true, 끝까지 없으면 false 반환
    for i in range(1, N):
        visited = [False for r in range(N)]
        Combination(visited, 0, N, 0)
        #정렬 하고 차이가 1 이상인데 작은 수가 1 개수를 모두 다 사용해 만든거라면 작은수 + 1을 반환.
    return




solution(N_out,S_out)